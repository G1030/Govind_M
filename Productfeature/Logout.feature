Feature: Logout

  Scenario: User logs out and is redirected to the homepage
    Given I am logged in on the "https://www.demoblaze.com" website
    When I select the "Logout" option
    Then I should be logged out and redirected to the homepage
