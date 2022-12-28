import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

Button=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
act=ActionChains(driver)
act.context_click(Button).perform()

#Copy
driver.find_element(By.XPATH,"//span[normalize-space()='Copy']").click()
time.sleep(3)
driver.switch_to.alert.accept()

