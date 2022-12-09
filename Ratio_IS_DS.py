from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Register").click()
searchbox=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("Display Status:",searchbox.is_displayed())
print("Enabled Status:",searchbox.is_enabled())

#Ratio Buttons
rd_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female=driver.find_element(By.XPATH,"//input[@id='gender-female']")
print(rd_male.is_selected())
print(rd_female.is_selected())

print("After Selecting Male Ratio Button!!!!!!")
rd_male.click()
print(rd_male.is_selected())
print(rd_female.is_selected())




