Feature: Managing product as an admin

# 12
Scenario: Delete a product
Given admin is on the products page
When admin click on the checkbox next to a product
And admin clicks on the "Delete" button
And admin accept the pop-up window
Then the product is removed from the list

# 13
Scenario: Filter by product name
Given admin is on the products page
When admin clicks on button "Filter"
And admin chooses a product name
And admin press button "Filter"
Then only matching items are displayed

# 14
Scenario: Adding new product without filling mandatory fields
Given admin is on the products page
When admin clicks on "Add New" button
And admin clicks on the "Save" button
Then warning appears

# 15
Scenario: Adding new product with filling all mandatory fields
Given admin is on the product page
When admin clicks on "Add New" button
And admin fills all mandatory fields
And admin clicks on "Save" button
Then new product is added to the list

# 16
Scenario: Copying a product
Given admin is on the product page
When admin clicks on the checkbox next to a product
And admin clicks on the "Copy" button
Then a copy of the element is in the list
And the copy is "Disabled"

# 17
Scenario: Changing quantity of a product
Given admin is on the products page
When admin clicks on the "Edit" button
And admin clicks on the "Data"
And admin changes "Quantity"
And admin clicks on "Save"
Then the quantity of the product changes in the list

# 18
Scenario: Disabling a product
Given admin is on the products page
When admin clicks on the "Edit" button
And admin clicks on the "Data"
And admin turns off "Status"
And admin clicks on "Save"
Then the product is "Disabled"