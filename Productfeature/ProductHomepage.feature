Feature: Homepage Verification

  Scenario: Verify the homepage of the website
    Given I open the website "https://www.demoblaze.com"
    Then the homepage loads successfully
    And the website logo is present
    And the navigation menu is present
    And at least one featured product is displayed
