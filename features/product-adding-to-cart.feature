# Feature: Adding product to the cart

# # 4
# Scenario: Adding an item to the cart on the home page
# Given user is on the home page
# When user clicks on the cart icon under the item listing
# Then the item is added to the cart

# # 5
# Scenario: Adding an item to the cart on the product page
# Given user is on the result page
# When user clicks on the button "Add to Cart"
# Then the item is added to the cart

# # 6
# Scenario: Adding 0 items to the cart on the product page
# Given user is on the result page
# When user sets quantity to 0
# And user presses "Add to Cart" button
# Then item is not added to the cart

# # 7
# Scenario: Adding an item with options - not filled
# Given user is on the result page
# When user doesn't fill mandatory fields
# And user clicks on "Add to Cart" button
# Then item is not added to the cart
# And a warning is shown

# # 8
# Scenario: Adding an item with options - filled
# Given user is on the result page
# When user fill all mandatory fields
# And user presses "Add to Cart" button
# Then item is added to the cart