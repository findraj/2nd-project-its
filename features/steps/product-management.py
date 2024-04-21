from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys

SUT_URL = "http://opencart:8080/administration"
LOGIN = "user"
PASSWORD = "bitnami"

@given(u'admin is on the products page')
def step_impl(context):
    context.driver.get(SUT_URL)
    context.driver.find_element(By.NAME, "username").click()
    context.driver.find_element(By.NAME, "username").send_keys("user")
    context.driver.find_element(By.NAME, "password").click()
    context.driver.find_element(By.NAME, "password").send_keys("bitnami")
    context.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    context.driver.find_element(By.LINK_TEXT, "Catalog").click()
    context.driver.find_element(By.LINK_TEXT, "Products").click()

# 12
@when(u'admin clicks on the checkbox next to a product')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[1]/table/tbody/tr[1]/td[1]/input").click()


@when(u'admin clicks on the "Delete" button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//html/body/div/div[2]/div[1]/div/div/button[3]").click()


@when(u'admin accept the pop-up window')
def step_impl(context):
    assert context.driver.switch_to.alert.text == "Are you sure?"
    context.driver.switch_to.alert.accept()


@then(u'the product is removed from the list')
def step_impl(context):
    sleep(0.1)
    deletedProduct = context.driver.find_element(By.XPATH, "//html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[1]/table/tbody/tr[1]/td[4]").text
    assert deletedProduct != 'Product 15'

# 13
@when(u'admin chooses a product name')
def step_impl(context):
    context.driver.find_element(By.ID, "input-name").click()
    context.driver.find_element(By.ID, "input-name").send_keys("iphone")


@when(u'admin press button "Filter"')
def step_impl(context):
    context.driver.find_element(By.ID, "button-filter").click()


@then(u'only matching items are displayed')
def step_impl(context):
    sleep(0.1)
    filteredProduct = context.driver.find_element(By.XPATH, "//html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[1]/table/tbody/tr[1]/td[4]").text
    assert filteredProduct == "product 11"

# 14
@when(u'admin clicks on "Add New" button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn > .fa-plus").click()


@when(u'admin clicks on the "Save" button')
def step_impl(context):
    element = context.driver.find_element(By.CSS_SELECTOR, ".fa-floppy-disk")
    element.location_once_scrolled_into_view
    sleep(1)
    element.click()


@then(u'warning appears')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".alert-danger").is_displayed()

# 15
@when(u'admin fills all mandatory fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-name-1").click()
    context.driver.find_element(By.ID, "input-name-1").send_keys("asdf")
    context.driver.find_element(By.ID, "input-meta-title-1").click()
    context.driver.find_element(By.ID, "input-meta-title-1").send_keys("asdf")
    context.driver.find_element(By.LINK_TEXT, "Data").click()
    context.driver.find_element(By.ID, "input-model").click()
    context.driver.find_element(By.ID, "input-model").send_keys("asdf")
    context.driver.find_element(By.LINK_TEXT, "SEO").click()
    context.driver.find_element(By.ID, "input-keyword-0-1").click()
    context.driver.find_element(By.ID, "input-keyword-0-1").send_keys("asdf")


@then(u'new product is added to the list')
def step_impl(context):
    sleep(0.1)
    context.driver.find_element(By.CSS_SELECTOR, ".fa-reply").click()
    filteredProduct = context.driver.find_element(By.XPATH, "//html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[1]/table/tbody/tr[1]/td[4]").text
    assert filteredProduct == "asdf"

# 16
@when(u'admin clicks on the "Copy" button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".fa-copy").click()


@then(u'a copy of the element is in the list')
def step_impl(context):
    sleep(0.1)
    copiedProduct = context.driver.find_element(By.XPATH, "//html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[1]/table/tbody/tr[2]/td[4]").text
    assert copiedProduct == "asdf"


@then(u'the copy is "Disabled"')
def step_impl(context):
    sleep(0.1)
    copiedProduct = context.driver.find_element(By.XPATH, "//html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[1]/table/tbody/tr[2]/td[3]/small").text
    assert copiedProduct == 'Disabled'

# 17
@when(u'admin clicks on the "Edit" button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .fa-pencil").click()


@when(u'admin clicks on the "Data"')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Data").click()


@when(u'admin changes "Quantity"')
def step_impl(context):
    element =  context.driver.find_element(By.ID, "input-quantity")
    element.location_once_scrolled_into_view
    sleep(0.5)
    element.click()
    element.send_keys(Keys.BACKSPACE)
    element.send_keys(Keys.BACKSPACE)
    element.send_keys(Keys.BACKSPACE)
    element.send_keys("1")


@then(u'the quantity of the product changes in the list')
def step_impl(context):
    sleep(7) # waiting for the warning to disappear
    context.driver.find_element(By.CSS_SELECTOR, ".fa-reply").click()
    sleep(0.1)
    newAmount = context.driver.find_element(By.XPATH, "//html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[1]/table/tbody/tr[1]/td[6]/span").text
    assert newAmount == '1'

# 18
@when(u'admin turns off "Status"')
def step_impl(context):
    element = context.driver.find_element(By.ID, "input-status")
    element.location_once_scrolled_into_view
    sleep(0.5)
    element.click()


@then(u'the product is "Disabled"')
def step_impl(context):
    sleep(7) # waiting for the warning to disappear
    context.driver.find_element(By.CSS_SELECTOR, ".fa-reply").click()
    sleep(0.1)
    copiedProduct = context.driver.find_element(By.XPATH, "//html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[1]/table/tbody/tr[1]/td[3]/small").text
    assert copiedProduct == 'Disabled'