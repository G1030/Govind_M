from selenium import webdriver
import os
driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#driver.save_screenshot("C:\\Users\\Bhavnish\\PycharmProjects\\PythonTraining\\day23_ScreenCookieHeadleass\\homepage.png")

#WITHOUT GIVE PATH
driver.save_screenshot(os.getcwd()+"\\homepage.png")
#driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")

