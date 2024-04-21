Feature: Buying items from the cart

# 9
Scenario: Personal details - mandatory fields not filled
Given user is on the checkout page with some products in the cart
When clicks on the "Continue" button
Then a warning is displayed

# 10
Scenario: Personal details - mandatory fields filled, Privacy Policy not accepted
Given user is on the checkout page with some products in the cart
When user fills all mandatory fields
And clicks on the "Continue" button
Then a warning is displayed

# 11
Scenario: Everything filled correctly
Given user is on the checkout page with some products in the cart
When user fills all mandatory fields
And user accepts the Privacy Policy
And clicks on the "Continue" button
Then a success message is displayed