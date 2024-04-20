from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def get_webdriver():
    # Get Chrome/Firefox driver from Selenium Hub
    try:
        driver = webdriver.Remote(
                command_executor="http://localhost:4444/wd/hub",
                desired_capabilities=DesiredCapabilities.FIREFOX,
                )
    except WebDriverException:
        driver = webdriver.Remote(
                command_executor="http://localhost:4444/wd/hub",
                desired_capabilities=DesiredCapabilities.CHROME,
                )
    driver.implicitly_wait(5)
    return driver


def before_all(context):
    context.driver = get_webdriver()

def after_all(context):
    context.driver.quit()