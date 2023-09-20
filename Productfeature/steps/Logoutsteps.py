from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I am logged in on the "{url}" website')
def step_login(context, url):
    context.driver = webdriver.Chrome()  # You need to have the Selenium WebDriver installed.
    context.driver.get(url)

    # Implement login logic here (navigate to login page, enter credentials, and log in).
    # Ensure you are logged in before proceeding with the logout.

@when('I select the "Logout" option')
def step_select_logout(context):
    logout_link = context.driver.find_element(By.ID, 'logout2')
    logout_link.click()

@then('I should be logged out and redirected to the homepage')
def step_check_logout_and_homepage(context):

@then('I close the browser')
def step_close_browser(context):
    context.driver.quit()
