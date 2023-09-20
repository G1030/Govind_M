Feature: Placing an Order

  Scenario: Place an order for a product
    Given I am on the "https://www.demoblaze.com" website
    When I add the product to the cart
    And I click on the cart to go to the cart page
    And I review the items in the cart
    And I click on the "Place Order" button
    And I fill the shipping details and purchase the item
    Then I should see a success message indicating the order is placed
