import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# Windowid=driver.current_window_handle
# print("Current Window ID:",Windowid)

time.sleep(3)
driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()
WindowIDs=driver.window_handles
ParentWindowID=WindowIDs[0]
ChildWindowID=WindowIDs[1]
print(ParentWindowID,ChildWindowID)

driver.switch_to.window(ChildWindowID)
print("Title of the Childwindow:",driver.title)

driver.switch_to.window(ParentWindowID)
print("Title of the Childwindow:",driver.title)

#More Than 2 Browser Windows
for wind in WindowIDs:
    driver.switch_to.window(wind)
    print(driver.title)

#Close Specfic Windows
for windid in WindowIDs:
    driver.switch_to.window(windid)
    if driver.title=="OrangeHRM":
        driver.close()






