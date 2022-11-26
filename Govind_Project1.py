import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

#Login Page
time.sleep(3)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

#driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

#PIM Details
driver.find_element(By.XPATH,"//span[normalize-space()='PIM']").click()
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Add Employee").click()

#Add Employee
driver.find_element(By.NAME,"firstName").send_keys("Govindharaj")
#driver.find_element(By.NAME,"middleName").send_keys("Raj")
driver.find_element(By.NAME,"lastName").send_keys("Muthu")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input").click()
driver.find_element(By.XPATH,"//span[@class='oxd-switch-input oxd-switch-input--active --label-right']").click()

#Create Login Details
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input").send_keys("GovindM")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input").send_keys("Govind@10")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input").send_keys("Govind@10")
time.sleep(5)
driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()

#Admin Details
driver.find_element(By.XPATH,"//span[normalize-space()='Admin']").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("GovindM")
driver.find_element(By.XPATH,"//button[normalize-space()='Search']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div/div/label/span/i").click()

#Add User
driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()

#Select Admin
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div").click()
Element=driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]")
print(len(Element))
for opt in Element:
    if opt.text=="Admin":
        opt.click()
        break

driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input").send_keys("Govindharaj  Muthu")

#Status Enabled
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div").click()
Status_Ele=driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]")
print(len(Status_Ele))
for sta in Status_Ele:
    if sta.text=="Enabled":
        sta.click()
        break

driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input").send_keys("MGovind10")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys("Govind@10")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("Govind@10")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/button[1]").click()

#Check Admin Users
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("MGovind10")
driver.find_element(By.XPATH,"//button[normalize-space()='Search']").click()
time.sleep(3)

#Logout
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a").click()

#Login Page
time.sleep(3)
driver.find_element(By.NAME,"username").send_keys("MGovind10")
driver.find_element(By.NAME,"password").send_keys("Govind@10")
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

















