from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Selenium_Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

Sliders=driver.find_elements(By.CLASS_NAME,"homeslider-description")
print(len(Sliders))
Links=driver.find_elements(By.TAG_NAME,"a")
print(len(Links))
driver.close()

