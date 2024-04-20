from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

SUT_URL = "http://opencart:8080"

@given(u'user is on the home page')
def step_impl(context):
    context.driver.get(SUT_URL)
    assert context.driver.title == "Your Store"


@when(u'user types query in the search bar')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("iphone")


@when(u'user presses serach icon')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn-light").click()


@then(u'result page with relevant contain is displayed')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//img[@alt='iPhone']").is_displayed()


@when(u'user clicks on the "Categorioes" list')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user clicks on the "Categorioes" list')


@when(u'user clicks on chosen category')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user clicks on chosen category')


@then(u'result page with relevant results is displayed"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then result page with relevant results is displayed"')


@when(u'user clicks on the picture in the animation')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user clicks on the picture in the animation')


@then(u'page with previously shown product is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then page with previously shown product is displayed')