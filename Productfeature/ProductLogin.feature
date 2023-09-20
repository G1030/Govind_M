Feature: User Login

  Scenario: Login with valid credentials
    Given I am on the "https://www.demoblaze.com" website
    When I click on the "Login" button
    And I enter valid login credentials
    And I click the login button
    Then I should be logged in successfully
