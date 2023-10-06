from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


class Search_Employee:
    Click_Customers_button_XPATH = (By.XPATH, "//a[@href='#']//p[contains(text(),'Customers')]")
    click_Customers_button_XPATH = (By.XPATH, "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]")
    click_Email_button_XPATH = (By.XPATH,"//input[@id='SearchEmail']")
    Search_Email_XPATH = (By.XPATH,"//td[normalize-space()='steve_gates@nopCommerce.com']")
    Click_Search_button = (By.XPATH,"//button[@id='search-customers']")


    def __init__(self, driver):
            self.driver = driver
            self.wait = WebDriverWait(self.driver, 10)

    def click_Customers(self):
        time.sleep(2)
        self.driver.find_element(*Search_Employee.Click_Customers_button_XPATH).click()

    def click_inside_button(self):
        self.driver.find_element(*Search_Employee.click_Customers_button_XPATH).click()
        time.sleep(2)

    def Click_Email(self,Email):
        self.driver.find_element(*Search_Employee.Search_Email_XPATH).send_keys(Email)

    def Search_Email(self,Email):
        self.driver.find_element(*Search_Employee.Search_Email_XPATH).click()

    def Click_Search(self):
        self.driver.find_element(*Search_Employee.Click_Search_button).click()
        time.sleep(2)





