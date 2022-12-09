from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()

Emailbox=driver.find_element(By.XPATH,"//input[@id='Email']")
Emailbox.clear()
Emailbox.send_keys("abc@gmail.com")

print("Result of Text:",Emailbox.text)
print("Result of Get Attributes:",Emailbox.get_attribute('value'))

#Login Button
Button=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
print("Result of Text:",Button.text)
print("Result of Get Attributes:",Button.get_attribute('value'))

driver.close()


