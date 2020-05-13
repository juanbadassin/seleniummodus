from behave import step
from re import sub
from decimal import Decimal

from hamcrest import equal_to, assert_that

from tests.page_objects.budget_page import BudgetPage
from tests.utils.generators import get_formated_value


@step('I navigate to the budget page')
def navigate_to_budget(context):
    context.budget_page = BudgetPage()
    context.budget_page.go_to(context)


@step('I add a new item of type {item_type}')
def add_new_item(context, item_type):
    if item_type == "inflow":
        context.budget_page.add_new_inflow(context)
    elif item_type == "outflow":
        context.budget_page.add_new_outflow(context)
    else:
        raise RuntimeError("Item type must be either inflow or outflow")


@step('The item is added to the table')
def assert_item_added_to_table(context):
    last_item = context.budget_page.get_last_item(context)
    assert last_item.find_elements_by_tag_name("td")[1].text == context.description
    assert last_item.find_elements_by_tag_name("td")[2].text == get_formated_value(context.item_value)


@step('The total inflow is correctly increased')
def assert_total_inflow_increased(context):
    current_total_inflow_value = Decimal(sub(r'[^\d.]', '', context.current_total_inflow))
    updated_total_inflow = current_total_inflow_value + context.item_value
    assert get_formated_value(updated_total_inflow) == context.budget_page.get_total_inflow(context).text


@step('I save the current total inflow amount')
def save_current_total_inflow(context):
    context.current_total_inflow = context.budget_page.get_total_inflow(context).text


@step('The total outflow is correctly decreased')
def assert_total_outflow_increased(context):
    current_total_outflow_value = Decimal(sub(r'[^\d.]', '', context.current_total_outflow))
    updated_total_outflow = current_total_outflow_value - context.item_value
    assert get_formated_value(updated_total_outflow) == context.budget_page.get_total_outflow(context).text


@step('I save the current total outflow amount')
def save_current_total_outflow(context):
    context.current_total_outflow = context.budget_page.get_total_outflow(context).text


@step('I count the amount of items in the table')
def count_items_in_table(context):
    context.count_items = context.budget_page.count_items(context)


@step('The amount of items has not change')
def assert_items_count_not_changed(context):
    assert_that(context.count_items, equal_to(context.budget_page.count_items(context)))


@step('I add a new item with 0 value')
def add_item_with_zero_value(context):
    context.browser.find_element(*context.budget_page.category_value_input_locator).send_keys("0")
    context.browser.find_element(*context.budget_page.category_add_btn_locator).click()