from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

SUT_URL = "http://opencart:8080"

@given(u'user is on the home page')
def step_impl(context):
    context.driver.get(SUT_URL)

# 1
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

# 2
@when(u'user clicks on the "Categorioes" list')
# not necessary in when screen is big enough


@when(u'user clicks on chosen category')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Phones & PDAs").click()


@then(u'result page with relevant results is displayed"')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//img[@alt='iPhone']").is_displayed()

# 3
@when(u'user clicks on the picture in the animation')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".col-12 > a > .img-fluid").click()


@then(u'page with previously shown product is displayed')
def step_impl(context):
    assert not  context.driver.find_element(By.XPATH, "//img[@alt='Samsung Galaxy Tab 10.1']").is_displayed()