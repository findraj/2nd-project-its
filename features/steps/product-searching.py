from behave import *
from selenium.webdriver.common.by import By

SUT_URL = "http://opencart:8080"
# given for scenarios starting on the home page (1, 2, 3, 4)
@given(u'user is on the home page')
def step_impl(context):
    """OpenCart home page is displayed"""
    context.driver.get(SUT_URL)

# Scenario 1
@when(u'user types query in the search bar')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click() # search bar is clicked
    context.driver.find_element(By.NAME, "search").send_keys("iphone")


@when(u'user presses serach icon')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn-light").click()


@then(u'result page with relevant contain is displayed')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//img[@alt='iPhone']").is_displayed()

# Scenario 2
@when(u'user clicks on the "Categorioes" list')
# Not necessary, because when page is big enough, the list is always visible


@when(u'user clicks on chosen category')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Phones & PDAs").click()


@then(u'result page with relevant results is displayed"')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//img[@alt='iPhone']").is_displayed()

# Scenario 3
@when(u'user clicks on the picture in the animation')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".col-12 > a > .img-fluid").click()


@then(u'page with previously shown product is displayed')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//img[@alt='Samsung Galaxy Tab 10.1']").is_displayed()