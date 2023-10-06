import time
from selenium.common import NoSuchElementException, NoAlertPresentException, TimeoutException, \
    ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Product:
    click_Catalog_XPATH = (By.XPATH,"//p[normalize-space()='Catalog']")
    Click_Product_XPATH = (By.XPATH,"//p[normalize-space()='Products']")
    Click_ADD_New_XPATH = (By.XPATH,"//i[@class='fas fa-plus-square']")
    Text_Product1_Name_XPATH = (By.XPATH,"//input[@id='Name']")
    Text_short_Desc_XPATH = (By.XPATH,"//textarea[@id='ShortDescription']")
    Dropdown_XPATH = (By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(3) > form:nth-child(2) > section:nth-child(4) > div:nth-child(1) > div:nth-child(1) > nop-cards:nth-child(2) > nop-card:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > span:nth-child(1)")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10,poll_frequency=0.1)

    def click_Catalog(self):
        self.driver.find_element(*Product.click_Catalog_XPATH).click()
        self.wait.until(expected_conditions.visibility_of_element_located(self.click_Catalog_XPATH))
        # wait = WebDriverWait(self.driver, 5)

    def click_Product(self):
        self.driver.find_element(*Product.Click_Product_XPATH).click()
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_Product_XPATH))

    def click_AddNew(self):
        self.driver.find_element(*Product.Click_ADD_New_XPATH).click()
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_ADD_New_XPATH))
        # time.sleep(2)

    def Enter_Product_Name(self,products):
        self.driver.find_element(*Product.Text_Product1_Name_XPATH).send_keys(products)
        # time.sleep(2)

    def Short_Desc(self,short):
        self.driver.find_element(*Product.Text_short_Desc_XPATH).send_keys(short)

    def Drop_down_Category(self,categories):
        Categories = Select(self.driver.find_element(*Product.Dropdown_XPATH))
        Categories.select_by_index(2)





