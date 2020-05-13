import os
from os.path import join
from time import time
from pathlib import Path

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

from tests.config.config import get_config


def before_all(context):
    p = Path(__file__).parents[2]
    context.screenshots_dir = join(str(p), "screenshots", os.getenv("BROWSER"))


def before_scenario(context, scenario):
    context.cleanup_tasks = []
    options = Options()
    browser = os.getenv("BROWSER")
    context.browser = WebDriver("http://{}:4444/wd/hub".format(get_config().get(browser, "host")),
                                desired_capabilities={"browserName": browser},
                                options=options)
    context.browser.set_page_load_timeout(15)
    context.browser.implicitly_wait(15)

    os.makedirs(join(context.screenshots_dir, scenario.name.replace(" ", "_")), exist_ok=True)
    context.screenshots_dir = join(context.screenshots_dir, scenario.name.replace(" ", "_"))


def after_step(context, step):
    context.browser.get_screenshot_as_file(join(context.screenshots_dir, "{}.png".format(step.name)))


def after_scenario(context, scenario):
    if scenario.status == "failed":
        context.browser.save_screenshot(
            join(context.screenshots_dir, "{}_failed.png".format(scenario.name)))

    context.browser.quit()
