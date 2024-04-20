from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

SUT_URL = "http://opencart:8080/administration"
LOGIN = "user"
PASSWORD = "bitnami"

@given(u'admin is on the products page')
def step_impl(context):
    context.driver.find_element(By.ID, "input-username").click()
    context.driver.find_element(By.ID, "input-username").send_keys("user")
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys("bitnami")
    context.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    context.driver.find_element(By.LINK_TEXT, "Catalog").click()
    context.driver.find_element(By.LINK_TEXT, "Products").click()


@when(u'admin click on the checkbox next to a product')
def step_impl(context):
    raise NotImplementedError(u'STEP: When admin click on the checkbox next to a product')


@when(u'admin clicks on the "Delete" button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When admin clicks on the "Delete" button')


@when(u'admin accept the pop-up window')
def step_impl(context):
    raise NotImplementedError(u'STEP: When admin accept the pop-up window')


@then(u'the product is removed from the list')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the product is removed from the list')


@when(u'admin clicks on button "Filter"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When admin clicks on button "Filter"')


@when(u'admin chooses a product name')
def step_impl(context):
    raise NotImplementedError(u'STEP: When admin chooses a product name')


@when(u'admin press button "Filter"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When admin press button "Filter"')


@then(u'only matching items are displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then only matching items are displayed')


@when(u'admin clicks on "Add New" button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When admin clicks on "Add New" button')


@when(u'admin clicks on the "Save" button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When admin clicks on the "Save" button')


@then(u'warning appears')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then warning appears')


@given(u'admin is on the product page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given admin is on the product page')


@when(u'admin fills all mandatory fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: When admin fills all mandatory fields')


@when(u'admin clicks on "Save" button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When admin clicks on "Save" button')


@then(u'new product is added to the list')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then new product is added to the list')


@when(u'admin clicks on the checkbox next to a product')
def step_impl(context):
    raise NotImplementedError(u'STEP: When admin clicks on the checkbox next to a product')


@when(u'admin clicks on the "Copy" button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When admin clicks on the "Copy" button')


@then(u'a copy of the element is in the list')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a copy of the element is in the list')


@then(u'the copy is "Disabled"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the copy is "Disabled"')


@when(u'admin clicks on the "Edit" button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When admin clicks on the "Edit" button')


@when(u'admin clicks on the "Data"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When admin clicks on the "Data"')


@when(u'admin changes "Quantity"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When admin changes "Quantity"')


@when(u'admin clicks on "Save"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When admin clicks on "Save"')


@then(u'the quantity of the product changes in the list')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the quantity of the product changes in the list')


@when(u'admin turns off "Status"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When admin turns off "Status"')


@then(u'the product is "Disabled"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the product is "Disabled"')