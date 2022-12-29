import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

#Scroll Down page by Pixel
# driver.execute_script("window.scrollBy(0,3000)","")
# value=driver.execute_script("return window.PageYOffset;")
# print("Number of Pixels Moved:",value)

#Scroll Down Page still the Element is Visible
# Flag=driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
# value=driver.execute_script("arguments[0].scrollIntoView();",Flag)
# print("Number of Pixels Moved:",value)

#Scroll Down Page Still End
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.PageYOffset;")
print("Number of Pixels Moved:",value)

#Scroll Up to Staring Position
time.sleep(3)
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value_ele=driver.execute_script("return window.PageYOffset;")
print("Number of Pixels Moved:",value_ele)






