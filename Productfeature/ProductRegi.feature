Feature: Registration with Valid Data

  Scenario: Register with valid data
    Given I am on the "https://www.demoblaze.com" website
    When I click on the "Sign Up" button
    And I fill out the registration form with valid data
    And I click on the "Sign Up" button
    Then I should see a registration success message
