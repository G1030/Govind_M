from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given('I am on the "{url}" website')
def step_open_website(context, url):
    context.driver = webdriver.Chrome()  # You need to have the Selenium WebDriver installed.
    context.driver.get(url)

@when('I add the product to the cart')
def step_add_to_cart(context):

@when('I click on the cart to go to the cart page')
def step_go_to_cart_page(context):
    cart_button = context.driver.find_element(By.ID, 'cartur')
    cart_button.click()

@when('I review the items in the cart')
def step_review_cart(context):

@when('I click on the "Place Order" button')
def step_click_place_order(context):
    place_order_button = context.driver.find_element(By.XPATH, "//button[contains(text(), 'Place Order')]")
    place_order_button.click()

@when('I fill the shipping details and purchase the item')
def step_fill_shipping_details(context):

@then('I should see a success message indicating the order is placed')
def step_check_order_success(context):
    success_message = context.driver.find_element(By.CLASS_NAME, 'sweet-alert')
    assert "Order" in success_message.text
    # Perform additional assertions as needed.

@then('I close the browser')
def step_close_browser(context):
    context.driver.quit()
