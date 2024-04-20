Feature: Product searching

# 1
Scenario: Searching for a product using search bar
Given user is on the home page
When user types query in the search bar
And user presses serach icon
Then result page with relevant contain is displayed

# 2
Scenario: Serching for a product using Categories
Given user is on the home page
When user clicks on the "Categorioes" list
And user clicks on chosen category
Then result page with relevant results is displayed"

# 3
Scenario: Check the product in the animation
Given user is on the home page
When user clicks on the picture in the animation
Then page with previously shown product is displayed