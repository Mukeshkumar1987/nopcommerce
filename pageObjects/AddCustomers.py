import time

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

from pageObjects.Login import LoginPage


from pageObjects.Login import LoginPage

class AddCustomer:


    Click_Customers_button_XPATH = (By.XPATH,"//a[@href='#']//p[contains(text(),'Customers')]")
    click_Customers_button_XPATH = (By.XPATH,"//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]")
    Click_AddNew_XPATH = (By.XPATH,"//a[@class='btn btn-primary']")
    Text_Email_XPATH = (By.CSS_SELECTOR,"#Email")
    Text_Password_XPATH = (By.XPATH,"//input[@id='Password']")
    Text_First_name_XPATH = (By.XPATH,"//input[@id='FirstName']")
    Text_Last_name_XPATH = (By.XPATH,"//input[@id='LastName']")
    Text_Gender_XPATH = (By.XPATH,"//label[@for='Gender_Male']")
    Click_Date_Of_Birth_XPATH = (By.XPATH,"//input[@id='DateOfBirth']")
    Click_Calender_XPATH = (By.XPATH,"//span[@class='k-icon k-i-calendar']")
    Click_save_XPATH = (By.XPATH,"//button[@name='save']")
    Click_AddNeww_XPATH = (By.XPATH,"//a[@class='btn btn-primary']")
    Export_Detail_XPATH = (By.XPATH,"//button[@class='btn btn-success']")

    def  __init__(self,driver):
     self.driver = driver
     self.wait = WebDriverWait(self.driver,10)
#
    def click_Customers(self):
        time.sleep(2)
        self.driver.find_element(*AddCustomer.Click_Customers_button_XPATH).click()
    def click_inside_button(self):
     self.driver.find_element(*AddCustomer.click_Customers_button_XPATH).click()
    def Click_AddNew(self):
     self.driver.find_element(*AddCustomer.Click_AddNew_XPATH).click()
    time.sleep(2)
    def Enter_Email(self,Email):
      self.driver.find_element(*AddCustomer.Text_Email_XPATH).send_keys(Email)
    time.sleep(2)

    def Enter_Password(self,Password):
        self.driver.find_element(*AddCustomer.Text_Password_XPATH).send_keys(Password)
        time.sleep(2)
        # self.wait.until(EC.presence_of_element_located((By.XPATH, "//i[@class='fas fa-cogs']


    def Enter_First_name(self,firstname):
        self.driver.find_element(*AddCustomer.Text_First_name_XPATH).send_keys(firstname)
    def Enter_Last_name(self,lastname):
        self.driver.find_element(*AddCustomer.Text_Last_name_XPATH).send_keys(lastname)

    def Enter_Gender(self):
        self.driver.find_element(*AddCustomer.Text_Gender_XPATH).click()


    def Click_Date_Of_Birth(self,dateOfbirth):
        self.driver.find_element(*AddCustomer.Click_Date_Of_Birth_XPATH).send_keys(dateOfbirth)

    def Click_Calender(self):
        self.driver.find_element(*AddCustomer.Click_Calender_XPATH).click()
    def  Click_save(self):
        self.driver.find_element(*AddCustomer.Click_save_XPATH).click()
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//i[@class='fas fa-cogs']")))

    def Click_AddNeww(self):
        self.driver.find_element(*AddCustomer.Click_AddNeww_XPATH).click()

    def AddEmloyee_Status(self):
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element(*AddCustomer.Export_Detail_XPATH)
            return True
        except:
            return False



# //input[@id='DateOfBirth']
# //a[normalize-space()='18']
# //a[normalize-space()='May 2023']