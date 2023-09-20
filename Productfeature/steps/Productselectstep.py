from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I am on the "{url}" website')
def step_open_website(context, url):
    context.driver = webdriver.Chrome()  # You need to have the Selenium WebDriver installed.
    context.driver.get(url)

@when('I navigate to the "{category}" category')
def step_select_category(context, category):
    category_link = context.driver.find_element(By.LINK_TEXT, category)
    category_link.click()

@when('I click on a product to view its details')
def step_view_product_details(context):

@when('I add the product to the cart')
def step_add_to_cart(context):
    add_to_cart_button = context.driver.find_element(By.XPATH, "//button[contains(text(), 'Add to cart')]")
    add_to_cart_button.click()

@then('I should see a success message indicating the product is added to the cart')
def step_check_cart_success_message(context):
    success_message = context.driver.find_element(By.CLASS_NAME, 'alert-success')
    assert success_message.is_displayed()

@then('I close the browser')
def step_close_browser(context):
    context.driver.quit()
