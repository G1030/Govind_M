from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I am on the "{url}" website')
def step_open_website(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)

@when('I click on the "{button_text}" button')
def step_click_button(context, button_text):
    button = context.driver.find_element(By.LINK_TEXT, button_text)
    button.click()

@when('I fill out the registration form with valid data')
def step_fill_registration_form(context):
    username_field = context.driver.find_element(By.ID, 'sign-username')
    password_field = context.driver.find_element(By.ID, 'sign-password')

    username_field.send_keys('your_valid_username')
    password_field.send_keys('your_valid_password')

@when('I click on the "{button_text}" button')
def step_click_button(context, button_text):
    button = context.driver.find_element(By.XPATH, f"//button[contains(text(), '{button_text}')]")
    button.click()

@then('I should see a registration success message')
def step_check_registration_success_message(context):
    success_message = context.driver.find_element(By.CLASS_NAME, 'alert-success')
    assert success_message.is_displayed()

@then('I close the browser')
def step_close_browser(context):
    context.driver.quit()
