import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

act=ActionChains(driver)

Sourse_Rome=driver.find_element(By.ID,"box6")
Target_Italy=driver.find_element(By.ID,"box106")
time.sleep(3)
act.drag_and_drop(Sourse_Rome,Target_Italy).perform()

Sourse_Washington=driver.find_element(By.ID,"box3")
Target_US=driver.find_element(By.ID,"box103")
time.sleep(3)
act.drag_and_drop(Sourse_Washington,Target_US).perform()

Sourse_Oslo=driver.find_element(By.ID,"box1")
Target_Norway=driver.find_element(By.ID,"box101")
time.sleep(3)
act.drag_and_drop(Sourse_Oslo,Target_Norway).perform()
