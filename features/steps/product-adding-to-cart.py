from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

SUT_URL = "http://opencart:8080"

# 4
@when (u'user clicks on the cart icon under the item listing')
def step_impl(context):
    element = context.driver.find_element(By.XPATH, "//html/body/main/div[2]/div/div/div[2]/div[1]/div/div[2]/form/div/button[1]")
    element.location_once_scrolled_into_view
    sleep(0.2)
    element.click()

@then (u'the item is added to the cart')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".alert").is_displayed()

@given (u'user is on the result page')
def step_impl(context):
    context.driver.get(SUT_URL)
    context.driver.find_element(By.CSS_SELECTOR, ".col:nth-child(1) > .product-thumb .img-fluid").click()
    

# 5
@when (u'user clicks on the button "Add to Cart"')
def step_impl(context):
    element = context.driver.find_element(By.XPATH, "//html/body/main/div[2]/div/div/div[1]/div[2]/div[1]/form/div/button")
    element.location_once_scrolled_into_view
    sleep(0.1)
    element.click()

# 6
@when(u'user sets quantity to 0')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#content > .row").click()
    context.driver.find_element(By.ID, "input-quantity").send_keys(Keys.BACKSPACE)
    context.driver.find_element(By.ID, "input-quantity").send_keys("0")


@when(u'user presses "Add to Cart" button')
def step_impl(context):
    context.driver.find_element(By.ID, "button-cart").click()


@then(u'item is not added to the cart')
def step_impl(context):
    inCart = context.driver.find_element(By.CSS_SELECTOR, ".btn-inverse").text
    assert inCart == '0 item(s) - $0.00'

@given (u'user is on the result page #2')
def step_impl(context):
    context.driver.get(SUT_URL)
    element = context.driver.find_element(By.CSS_SELECTOR, ".col:nth-child(4) > .product-thumb .img-fluid")
    element.location_once_scrolled_into_view
    sleep(0.2)
    element.click()

# 7
@when(u'user doesn\'t fill mandatory fields')
#do nothing


@when(u'user clicks on "Add to Cart" button')
def step_impl(context):
    context.driver.find_element(By.ID, "button-cart").click()

# 8
@when(u'user fill all mandatory fields')
def step_impl(context):
    element = context.driver.find_element(By.ID, "input-option-226").click()
    dropdown = context.driver.find_element(By.ID, "input-option-226")
    dropdown.find_element(By.XPATH, "//option[@value='15']").click()

@then(u'item is added to the cart')
def step_impl(context):
    inCart = context.driver.find_element(By.CSS_SELECTOR, ".btn-inverse").text
    assert inCart == '1 item(s) - $98.00'