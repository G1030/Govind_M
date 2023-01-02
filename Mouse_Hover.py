import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

#Login
time.sleep(5)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

Admin_Ele=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span")
User_Manage=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]")
Users=driver.find_element(By.XPATH,"//ul[@role='menu']")

act=ActionChains(driver)
act.move_to_element(Admin_Ele).move_to_element(User_Manage).move_to_element(Users).click().perform()
