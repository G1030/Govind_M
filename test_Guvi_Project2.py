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

    def testLogin_TC_PIM_01(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        search_box=self.driver.find_element(By.XPATH,"//input[@placeholder='Search']")
        print(search_box.is_displayed())
        print(search_box.is_enabled())
        search_box.send_keys("admin")
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").click()
        time.sleep(4)
        #Screenshot
        self.driver.save_screenshot("C:\\Users\\Bhavnish\\PycharmProjects\\pythonSelenium\\UpdateProject2_Screenshot\\TC_PIM_01.png")

    def testAdmin_TC_PIM_02(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        Admin_Link=self.driver.find_element(By.XPATH,"//span[normalize-space()='Admin']")
        print(Admin_Link.is_displayed())
        Admin_Link.click()

        #User Management
        self.driver.find_element(By.XPATH,"//span[normalize-space()='User Management']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//ul[@role='menu']//li").click()

        #Admin Select
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div").click()
        Element = self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]")
        for opt in Element:
            if opt.text == "Admin":
                opt.click()
                break

        #Enabled Select
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]").click()
        Status_Ele = self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]")
        for sta in Status_Ele:
            if sta.text == "Enabled":
                sta.click()
                break

        #ESS Select
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div").click()
        ess_Ele= self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]")
        for Es in ess_Ele:
            if Es.text=="ESS":
                Es.click()
                break

        #Disabled Select
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]").click()
        Status_dis = self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]")
        for sta_dis in Status_dis:
            if sta_dis.text == "Disabled":
                sta_dis.click()
                break
        time.sleep(5)
        #Screenshot
        self.driver.save_screenshot("C:\\Users\\Bhavnish\\PycharmProjects\\pythonSelenium\\UpdateProject2_Screenshot\\TC_PIM_02.png")

    def testPIM_TC_PIM_03(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        # PIM Details
        self.driver.find_element(By.XPATH,"//span[normalize-space()='PIM']").click()
        PIM_Ele=self.driver.find_element(By.XPATH, "//span[normalize-space()='PIM']")
        print(PIM_Ele.is_displayed())

        #+ADD Button
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()

        #Image Add
        # Image=self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/div/button/i")
        # Image.click()
        # time.sleep(3)
        #Image.send_keys("C:\SeleniumPractice\govind.jpg")

        # Add Employee
        self.driver.find_element(By.NAME, "firstName").send_keys("Govindharaj")
        self.driver.find_element(By.NAME, "lastName").send_keys("Muthu")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//span[@class='oxd-switch-input oxd-switch-input--active --label-right']").click()

        # Create Login Details
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input").send_keys("GovindM")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input").send_keys("Govind@10")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input").send_keys("Govind@10")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        time.sleep(5)
        #Screenshot
        self.driver.save_screenshot("C:\\Users\\Bhavnish\\PycharmProjects\\pythonSelenium\\UpdateProject2_Screenshot\\TC_PIM_03.png")

    def testPIM_TC_PIM_04(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        #My Info
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()

        Personal=self.driver.find_element(By.XPATH,"//a[normalize-space()='Personal Details']")
        print(Personal.is_displayed())
        print(Personal.is_enabled())
        Contact=self.driver.find_element(By.XPATH,"//a[normalize-space()='Contact Details']")
        print(Contact.is_displayed())
        Emergency=self.driver.find_element(By.XPATH,"//a[normalize-space()='Emergency Contacts']")
        print(Emergency.is_displayed())
        Dependents=self.driver.find_element(By.XPATH,"//a[normalize-space()='Dependents']")
        print(Dependents.is_displayed())
        Immigration=self.driver.find_element(By.XPATH,"//a[normalize-space()='Immigration']")
        print(Immigration.is_displayed())
        Job=self.driver.find_element(By.XPATH,"//a[normalize-space()='Job']")
        print(Job.is_displayed())
        print(Job.is_enabled())
        Salary=self.driver.find_element(By.XPATH,"//a[normalize-space()='Salary']")
        print(Salary.is_displayed())
        print(Salary.is_enabled())
        Tax=self.driver.find_element(By.XPATH,"//a[normalize-space()='Tax Exemptions']")
        print(Tax.is_displayed())
        print(Tax.is_enabled())
        Report=self.driver.find_element(By.XPATH,"//a[normalize-space()='Report-to']")
        print(Report.is_displayed())
        print(Report.is_enabled())
        Qualification=self.driver.find_element(By.XPATH,"//a[normalize-space()='Qualifications']")
        print(Qualification.is_displayed())
        Member=self.driver.find_element(By.XPATH,"//a[normalize-space()='Memberships']")
        print(Member.is_displayed())
        #Screenshot
        time.sleep(4)
        self.driver.save_screenshot("C:\\Users\\Bhavnish\\PycharmProjects\\pythonSelenium\\UpdateProject2_Screenshot\\TC_PIM_04.png")

    def testEmp_Personal_Details_05(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        # PIM Details
        self.driver.find_element(By.XPATH,"//span[normalize-space()='PIM']").click()

        #SearEmployee Name
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("Govindharaj Muthu")
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Search']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//div[@class='oxd-table-card-cell-checkbox']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div").click()

        #NicName
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input").send_keys("MG")

        # Nationality
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div").click()
        Nation = self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[2]")
        for Nat in Nation:
            if Nat.text == "Afghan":
                Nat.click()
                break

        #Marital Status
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div").click()
        Ma_sta=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[2]/i")
        for ma in Ma_sta:
            if ma.text=="Married":
                ma.click()
                break

        #Date of Birth
        time.sleep(5)
        Date = self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input")
        Date.clear()
        Date.send_keys("1987-03-10")

        #Gender
        self.driver.find_element(By.XPATH,"//label[normalize-space()='Male']").click()

        # Smoker
        #self.driver.find_element(By.XPATH, "//label[normalize-space()='Yes']").click()

        # Save Button
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button").click()

        # Blood Type
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div").click()
        Group = self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div/div[2]")
        for Bld in Group:
            if Bld.text == "A+":
                Bld.click()
                break

        #Save Button
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button").click()
        time.sleep(5)
        #Screenshot
        self.driver.save_screenshot("C:\\Users\\Bhavnish\\PycharmProjects\\pythonSelenium\\UpdateProject2_Screenshot\\TC_PIM_05.png")

    def testEmp_Contact_Details_06(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        # PIM Details
        self.driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()

        # SearEmployee Name
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("Govindharaj Muthu")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//div[@class='oxd-table-card-cell-checkbox']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div").click()

        #Contact Details
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Contact Details']").click()

        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("10 Street")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("Valasaravakkam")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input").send_keys("Chennai")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input").send_keys("Tamil Nadu")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input").send_keys("600087")

        #Country Select
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div").click()
        Con=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[2]")
        for co in Con:
            if co.text=="Afghanistan":
                co.click()
                break

        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input").send_keys("123456")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input").send_keys("7777777777")
        Email=self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input")
        Email.clear()
        Email.send_keys("G@gmail.com")
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
        time.sleep(5)
        #Screenshot
        self.driver.save_screenshot("C:\\Users\\Bhavnish\\PycharmProjects\\pythonSelenium\\UpdateProject2_Screenshot\\TC_PIM_06.png")

    def testEmergency_Contact_Details_07(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        # PIM Details
        self.driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()

        # SearEmployee Name
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("Govindharaj Muthu")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//div[@class='oxd-table-card-cell-checkbox']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div").click()

        #Emergency Contacts
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Emergency Contacts']").click()

        #Add Button
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button").click()

        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Rock")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("Friend")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input").send_keys("5555555555")
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
        time.sleep(5)
        #Screenshot
        self.driver.save_screenshot("C:\\Users\\Bhavnish\\PycharmProjects\\pythonSelenium\\UpdateProject2_Screenshot\\TC_PIM_07.png")

    def testEmp_Dependents_ContactDetails_08(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        # PIM Details
        self.driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()

        # SearEmployee Name
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("Govindharaj Muthu")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//div[@class='oxd-table-card-cell-checkbox']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div").click()

        #Dependents_ContactDetails
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Dependents']").click()

        #Add Button
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button").click()
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Vijay Govind")

        #DropDown
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div").click()
        Ele_Sel=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]")
        print(len(Ele_Sel))
        for Rel in Ele_Sel:
            if Rel.text=="Child":
                Rel.click()
                break

        #Date of Birth
        time.sleep(3)
        Cdate=self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div/div/div[2]/div/div/input")
        Cdate.click()
        Cdate.send_keys("2020-02-20")

        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
        time.sleep(5)
        #Screenshot
        self.driver.save_screenshot("C:\\Users\\Bhavnish\\PycharmProjects\\pythonSelenium\\UpdateProject2_Screenshot\\TC_PIM_08.png")

    def testEmp_Job_Details_09(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        # PIM Details
        self.driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()

        # SearEmployee Name
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("Govindharaj Muthu")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//div[@class='oxd-table-card-cell-checkbox']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div").click()

        #Job Button
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Job']").click()

        #Joined Date
        self.driver.find_element(By.XPATH,"//input[@placeholder='yyyy-mm-dd']").send_keys("2020-20-20")

        #Job Title
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div").click()
        Job_Ele=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]")
        for job in Job_Ele:
            if job.text=="Account Assistant":
                job.click()
                break

        #Job Category
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div").click()
        Job_Cate=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]")
        for jca in Job_Cate:
            if jca.text=="SOFTWARE ENGINEER":
                jca.click()
                break

        #Sub Unit
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div").click()
        sub_Ele=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div/div[2]")
        for s in sub_Ele:
            if s.text=="Administration":
                s.click()
                break

        #Location
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div").click()
        Loc_Ele=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[2]")
        for lo in Loc_Ele:
            if lo.text=="Canadian Regional HQ":
                lo.click()
                break

        #Employeement Status
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div").click()
        Emp_sta=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div/div[2]")
        for es in Emp_sta:
            if es.text=="Full-Time Contract":
                es.click()
                break

        #Button
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/label/span").click()

        #Contract start Date
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/div/div/input").send_keys("2015-10-20")

        #Contract End Date
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/div/div/input").send_keys("2022-10-20")

        #Save Button
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
        #Screenshot
        time.sleep(3)
        self.driver.save_screenshot("C:\\Users\\Bhavnish\\PycharmProjects\\pythonSelenium\\UpdateProject2_Screenshot\\TC_PIM_09.png")

    def testEmp_Job_Termination_10(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        # PIM Details
        self.driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()

        # SearEmployee Name
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("Govindharaj Muthu")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//div[@class='oxd-table-card-cell-checkbox']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div").click()

        #Job Button
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Job']").click()

        #Terminate Employment
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Terminate Employment']").click()
        #Termination Date
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[1]/div/div[2]/div/div/input").send_keys("2022-10-30")
        #Termination Reason
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div").click()
        Ter_Ele=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div/div[2]")
        for ter in Ter_Ele:
            if ter.text=="Contract Not Renewed":
                ter.click()
                break

        self.driver.find_element(By.XPATH,"//textarea[@placeholder='Type here']").send_keys("Software Testing")
        #Save Button
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[4]/button[2]").click()
        time.sleep(5)
        #Screenshot
        self.driver.save_screenshot("C:\\Users\\Bhavnish\\PycharmProjects\\pythonSelenium\\UpdateProject2_Screenshot\\TC_PIM_10.png")

    def testEmp_Job_Activation_11(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        # PIM Details
        self.driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()

        # SearEmployee Name
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("Govindharaj Muthu")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//div[@class='oxd-table-card-cell-checkbox']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div").click()

        #Job Button
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Job']").click()

        #Activate Employment
        time.sleep(5) 
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Activate Employment']").click()
        time.sleep(3)

        #Screenshot
        self.driver.save_screenshot("C:\\Users\\Bhavnish\\PycharmProjects\\pythonSelenium\\UpdateProject2_Screenshot\\TC_PIM_11.png")

    def testEmp_Salary_12(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        # PIM Details
        self.driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()

        # SearEmployee Name
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("Govindharaj Muthu")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//div[@class='oxd-table-card-cell-checkbox']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div").click()

        #Salary
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Salary']").click()

        #Add Button
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button").click()

        #Salary Component
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("10 Lakh")
        #Pay Grade
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div").click()
        Pay_Ele=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]")
        for pay in Pay_Ele:
            if pay.text=="Grade 1":
                pay.click()
                break

        #Pay Frequency
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/div/div").click()
        Pay_Fre=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]")
        for freq in Pay_Fre:
            if freq.text=="Hourly":
                freq.click()
                break
        #Currency
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div").click()
        Cur_Ele=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]")
        for curr in Cur_Ele:
            if curr.text=="United States Dollar":
                curr.click()
                break

        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input").send_keys("50000")

        #Deposit Details
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/label/span").click()

        #Account Number
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[1]/div/div[2]/input").send_keys("01234567890")
        #Account Type
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[2]/div/div[2]/div/div").click()
        Acc_Type=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[2]/div/div[2]/div/div/div[2]")
        for acc in Acc_Type:
            if acc.text=="Savings":
                acc.click()
                break

        #Routing Number
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[1]/div/div[2]/input").send_keys("11111")
        #Amount
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[2]/div/div[2]/input").send_keys(50000)
        #Save Button
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
        #Screenshot
        time.sleep(5)
        self.driver.save_screenshot("C:\\Users\\Bhavnish\\PycharmProjects\\pythonSelenium\\UpdateProject2_Screenshot\\TC_PIM_12.png")


    def testEmp_Tex_Exemptions_13(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        # PIM Details
        self.driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()

        # SearEmployee Name
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("Govindharaj Muthu")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//div[@class='oxd-table-card-cell-checkbox']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div").click()

        #Tax Exemptions
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Tax Exemptions']").click()
        #Status
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div").click()
        St_ele=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]")
        for st in St_ele:
            if st.text=="Married":
                st.click()
                break

        #Exemption
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("5000")
        #State
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div").click()
        Ex_sta=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div/div[2]")
        for ex in Ex_sta:
            if ex.text=="Alabama":
                ex.click()
                break

        #In State
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div").click()
        In_Sta=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div/div[2]")
        for Ins in In_Sta:
            if Ins.text=="Married":
                Ins.click()
                break

        #UnEmployee State
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/div/div").click()
        Un_Emp=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/div/div/div[2]")
        for un in Un_Emp:
            if un.text=="Alabama":
                un.click()
                break

        #Work State
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div").click()
        Wr_Sta=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div/div[2]")
        for wr in Wr_Sta:
            if wr.text=="Alabama":
                wr.click()
                break

        #Save Button
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()

        #Screenshot
        time.sleep(5)
        self.driver.save_screenshot("C:\\Users\\Bhavnish\\PycharmProjects\\pythonSelenium\\UpdateProject2_Screenshot\\TC_PIM_13.png")

























































