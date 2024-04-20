from behave import given, when, then

@given(u'user is on the home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given user is on the home page')


@when(u'user types query in the search bar')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user types query in the search bar')


@when(u'user presses serach icon')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user presses serach icon')


@then(u'result page with relevant contain is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then result page with relevant contain is displayed')


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

