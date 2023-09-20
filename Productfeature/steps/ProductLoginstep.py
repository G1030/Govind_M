from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I am on the "{url}" website')
def step_open_website(context, url):
    context.driver = webdriver.Chrome()  # You need to have the Selenium WebDriver installed.
    context.driver.get(url)

@when('I click on the "{button_text}" button')
def step_click_button(context, button_text):
    button = context.driver.find_element(By.LINK_TEXT, button_text)
    button.click()

@when('I enter valid login credentials')
def step_enter_login_credentials(context):
    username_field = context.driver.find_element(By.ID, 'loginusername')
    password_field = context.driver.find_element(By.ID, 'loginpassword')

    username_field.send_keys('your_valid_username')  # Replace with a valid username
    password_field.send_keys('your_valid_password')  # Replace with a valid password

@when('I click the login button')
def step_click_login_button(context):
    login_button = context.driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]")
    login_button.click()

@then('I should be logged in successfully')
def step_check_login_success(context):

@then('I close the browser')
def step_close_browser(context):
    context.driver.quit()
