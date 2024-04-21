from behave import *
from selenium.webdriver.common.by import By
from time import sleep

SUT_URL = "http://opencart:8080"

# given for scenarios starting on the checkout page (9, 10, 11)
@given(u'user is on the checkout page with some products in the cart')
def step_impl(context):
    context.driver.get(SUT_URL)
    # add item to the cart
    element = context.driver.find_element(By.XPATH, "//html/body/main/div[2]/div/div/div[2]/div[1]/div/div[2]/form/div/button[1]")
    element.location_once_scrolled_into_view
    sleep(0.2)
    element.click()
    sleep(7) # wait for the warning to disappear
    element = context.driver.find_element(By.CSS_SELECTOR, ".btn-inverse")
    element.location_once_scrolled_into_view
    sleep(0.5)
    element.click()
    context.driver.find_element(By.CSS_SELECTOR, "a:nth-child(2) > strong").click()

# Scenario 9
@when(u'clicks on the "Continue" button')
def step_impl(context):
    element = context.driver.find_element(By.ID, "button-register")
    element.location_once_scrolled_into_view
    sleep(0.2)
    element.click()


@then(u'a warning is displayed')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".alert-danger").is_displayed()

# Scenario 10
@when(u'user fills all mandatory fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").click()
    context.driver.find_element(By.ID, "input-firstname").send_keys("asdf")
    context.driver.find_element(By.ID, "input-lastname").click()
    context.driver.find_element(By.ID, "input-lastname").send_keys("asdf")
    context.driver.find_element(By.ID, "input-email").click()
    context.driver.find_element(By.ID, "input-email").send_keys("asdf@asdf.asdf")
    context.driver.find_element(By.ID, "input-shipping-address-1").click()
    context.driver.find_element(By.ID, "input-shipping-address-1").send_keys("asdf")
    context.driver.find_element(By.ID, "input-shipping-city").click()
    context.driver.find_element(By.ID, "input-shipping-city").send_keys("asdf")
    context.driver.find_element(By.ID, "input-shipping-postcode").click()
    context.driver.find_element(By.ID, "input-shipping-postcode").send_keys("asdf")
    element = context.driver.find_element(By.ID, "input-shipping-zone")
    element.location_once_scrolled_into_view
    sleep(0.5)
    dropdown = context.driver.find_element(By.ID, "input-shipping-zone")
    dropdown.location_once_scrolled_into_view
    sleep(0.5)
    dropdown.find_element(By.XPATH, "//option[. = 'Aberdeenshire']").click()
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys("asdf")

# Scenario 11
@when(u'user accepts the Privacy Policy')
def step_impl(context):
    context.driver.find_element(By.ID, "input-register-agree").click()

@then(u'a success message is displayed')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".alert-success").is_displayed()