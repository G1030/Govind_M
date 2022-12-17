import time

from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class TestOrangeHRM():

    @pytest.fixture()
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_HomePageTitle(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        assert self.driver.title=="OrangeHRM"

    def test_Login(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        assert self.driver.title=="OrangeHRM"

    def test_PIM_AddEmp(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Add Employee").click()

        # Add Employee
        self.driver.find_element(By.NAME, "firstName").send_keys("Govindharaj")
        # driver.find_element(By.NAME,"middleName").send_keys("Raj")
        self.driver.find_element(By.NAME, "lastName").send_keys("Muthu")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input").click()
        self.driver.find_element(By.XPATH,"//span[@class='oxd-switch-input oxd-switch-input--active --label-right']").click()

        # Create Login Details
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input").send_keys("GovindM")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input").send_keys("Govind@10")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input").send_keys("Govind@10")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        # Admin Details
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Admin']").click()
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("GovindM")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div/div/label/span/i").click()

        # Add User
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()

        # Select Admin
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div").click()
        Element = self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]")
        #print(len(Element))
        for opt in Element:
            if opt.text == "Admin":
                opt.click()
                break

        # Select Employee Name
        act = ActionChains(self.driver)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input").send_keys("Govindharaj Muthu")
        act.move_to_element(self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[@role='listbox']"))
        time.sleep(3)
        Search_Ele =self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[@role='listbox']/div")
        for tye in Search_Ele:
            if tye.text == "Govindharaj Muthu":
                tye.click()
                break

        # Status Enabled
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div").click()
        Status_Ele = self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]")
        #print(len(Status_Ele))
        for sta in Status_Ele:
            if sta.text == "Enabled":
                sta.click()
                break

        # User Name & Password
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input").send_keys("MGovind10")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys("Govind@10")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("Govind@10")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click()
        #self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/button[1]").click()

        # #Check Admin Users
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("MGovind10")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div").click()
        time.sleep(3)

        # Logout
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p").click()
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a").click()

    def test_MyLogin(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("MGovind10")
        self.driver.find_element(By.NAME, "password").send_keys("Govind@10")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(3)








