from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I open the website "{url}"')
def step_open_website(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)

@then('the homepage loads successfully')
def step_homepage_loads_successfully(context):
    assert "DemoBlaze" in context.driver.title

@then('the website logo is present')
def step_website_logo_present(context):
    logo_element = context.driver.find_element(By.ID, "logo")
    assert logo_element.is_displayed()

@then('the navigation menu is present')
def step_navigation_menu_present(context):
    menu_element = context.driver.find_element(By.ID, "menu")
    assert menu_element.is_displayed()

@then('at least one featured product is displayed')
def step_featured_product_displayed(context):
    featured_products = context.driver.find_elements(By.CLASS_NAME, "featured-product")
    assert len(featured_products) > 0

@then('I close the browser')
def step_close_browser(context):
    context.driver.quit()
