from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

Mini_Slider=driver.find_element(By.XPATH,"//*[@id='slider-range']/span[1]")
Max_Slider=driver.find_element(By.XPATH,"//*[@id='slider-range']/span[2]")
print("Location of Slider After Moving!!!!!")
print(Mini_Slider.location)                   # {'x': 59, 'y': 250}
print(Max_Slider.location)                    # {'x': 510, 'y': 250}

act=ActionChains(driver)

act.drag_and_drop_by_offset(Mini_Slider,100,0).perform()
act.drag_and_drop_by_offset(Max_Slider,-110,0).perform()
print("Location of Slider Before Moving!!!!!")
print(Mini_Slider.location)                   # {'x': 159, 'y': 250}
print(Max_Slider.location)                    # {'x': 398, 'y': 250}



