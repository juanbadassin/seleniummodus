import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.config.config import get_config
from tests.utils.generators import get_random_string, get_random_value


class BudgetPage:

    def __init__(self):
        self.url = "budget"
        self.category_select_locator = (By.NAME, "categoryId")
        self.category_description_input_locator = (By.NAME, "description")
        self.category_value_input_locator = (By.NAME, "value")
        self.category_add_btn_locator = (By.TAG_NAME, "button")
        self.items_table_locator = (By.TAG_NAME, "table")
        self.total_balance_locator = (By.CLASS_NAME, "_3S2Fs")

    def go_to(self, context):
        budget_url = "{}/{}".format(get_config().get("application", "url"), self.url)
        context.browser.get(budget_url)

    def add_new_inflow(self, context):
        select_element = context.browser.find_element(*self.category_select_locator)
        select_element.click()
        category_id_options = select_element.find_elements_by_tag_name("option")
        income_option = [option for option in category_id_options if option.text == "Income"][0]
        income_option.click()
        context.category = income_option.text
        self.add_item(context)

    def add_new_outflow(self, context):
        select_element = context.browser.find_element(*self.category_select_locator)
        select_element.click()
        category_id_options = select_element.find_elements_by_tag_name("option")

        option_index = -1
        while option_index < 0:
            option_index = random.randint(0, len(category_id_options))
            if category_id_options[option_index].text == "Income":
                option_index = -1
        context.category = category_id_options[option_index].text
        category_id_options[option_index].click()
        self.add_item(context)

    def add_item(self, context):
        context.description = get_random_string()
        context.browser.find_element(
            *self.category_description_input_locator).send_keys(context.description)

        context.item_value = get_random_value()
        context.browser.find_element(
            *self.category_value_input_locator).send_keys(context.item_value)
        context.item_value = context.item_value * -1 if context.category != "Income" else context.item_value

        WebDriverWait(context.browser, 30).until(
            EC.element_to_be_clickable(self.category_add_btn_locator))
        context.browser.find_element(*self.category_add_btn_locator).click()

    def get_last_item(self, context):
        items_table = context.browser.find_element(*self.items_table_locator)
        return items_table.find_elements_by_tag_name("tr")[-2]

    def get_total_inflow(self, context):
        totals = context.browser.find_elements(*self.total_balance_locator)
        total_inflow = [total for total in totals if "Inflow" in total.text][0]
        return [element for element in total_inflow.find_elements_by_tag_name("div") if "$" in element.text][0]

    def get_total_outflow(self, context):
        totals = context.browser.find_elements(*self.total_balance_locator)
        total_outflow = [total for total in totals if "Outflow" in total.text][0]
        return [element for element in total_outflow.find_elements_by_tag_name("div") if "$" in element.text][0]

    def count_items(self, context):
        items_table = context.browser.find_element(*self.items_table_locator)
        return len(items_table.find_elements_by_tag_name("tr"))
