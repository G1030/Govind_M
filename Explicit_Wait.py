
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()

#mywait=WebDriverWait(driver,10)        # Explicit Wait Declaration

mywait=WebDriverWait(driver,10,ignored_exceptions=[NoSuchElementException,
                                                   ElementNotVisibleException,
                                                   ElementNotSelectableException])     #Or Exception

driver.get("https://www.google.com/")
driver.maximize_window()

searchbox=driver.find_element(By.NAME,"q")
searchbox.send_keys("selenium")
searchbox.submit()

searchlink=mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[normalize-space()='Selenium']")))
searchlink.click()


