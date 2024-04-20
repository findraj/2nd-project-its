from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

@given(u'user is on the checkout page with some products in the cart')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given user is on the checkout page with some products in the cart')

# 9
@when(u'clicks on the "Continue" button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When clicks on the "Continue" button')


@then(u'a warning is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a warning is displayed')

# 10
@when(u'user fills all mandatory fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user fills all mandatory fields')

# 11
@when(u'user clicks on the "Confirm order" button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user clicks on the "Confirm order" button')


@then(u'order is placed and confirming page is loaded')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then order is placed and confirming page is loaded')