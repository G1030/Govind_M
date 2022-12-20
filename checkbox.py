import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

#Select Specific Checkbox
#driver.find_element(By.XPATH,"//input[@id='wednesday']").click()

#Select All The CheckBox
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))
for checkbox in checkboxes:
    checkbox.click()

#Select Multiple Checkboxes bu Choice
# for checkbox in checkboxes:
#     weekname=checkbox.get_attribute('id')
#     if weekname=="monday" or weekname=="friday" or weekname=="sunday":
#         checkbox.click()

#Select Last 2 Checkboxes
# for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()

#Select First 2 Checkboxes
# for i in range(len(checkboxes)):
#     if i<2:
#         checkboxes[i].click()

#UnSelect All Checkboxes
time.sleep(5)
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()









