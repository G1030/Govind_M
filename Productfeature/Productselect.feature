Feature: Product Selection and Cart Interaction

  Scenario: Add a product to the cart
    Given I am on the "https://www.demoblaze.com" website
    When I navigate to the "Laptops" category
    And I click on a product to view its details
    And I add the product to the cart
    Then I should see a success message indicating the product is added to the cart
