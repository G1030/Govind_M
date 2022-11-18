#SELENIUM 4.X
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

serv_obj=Service("C:\Selenium_Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://admin-demo.nopcommerce.com/")

driver.find_element(By.ID,"Email").clear()
driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
driver.find_element(By.NAME,"Password").clear()
driver.find_element(By.NAME,"Password").send_keys("admin")
driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
driver.maximize_window()
act_title=driver.title
exp_title="Dashboard / nopCommerce administration"
if act_title==exp_title:
    print("Login Test Passed!!!")
else:
    print("Login Test Failed!!!")
driver.close()
