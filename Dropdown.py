from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Selenium_Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()
#drpcountry_ele=driver.find_element(By.XPATH,"//select[@id='input-country']")
drpcountry=Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))

# SELECT OPTION FOR THE DROPDOWN
#drpcountry.select_by_visible_text("India")
#drpcountry.select_by_value("10")
#drpcountry.select_by_index(13)

#Capture All The Options And Print
Alloptions=drpcountry.options
print("Total Number Of Options:",len(Alloptions))
for opt in Alloptions:
     print(opt.text)

# SELECT OPTIONS FROM DROPDOWN WITHOUT USING BUILD-IN METHOD
for opt in Alloptions:
    if opt.text=="India":
        opt.click()

