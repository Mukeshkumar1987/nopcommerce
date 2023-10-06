from selenium.webdriver.common.by import By


class  SalesA:
    click_Sales_XPATH = (By.XPATH,"//p[normalize-space()='Sales']")
    # click_Orders_XPATH  = (By.XPATH,"//p[normalize-space()='Orders']")
    click_Shiping_XPATH = (By.XPATH,"//p[normalize-space()='Shopping carts and wishlists']")
    clicK_Start_Date_XPATH = (By.XPATH,"//input[@id='StartDate']")
    click_Calender_XPATH = (By.XPATH,"//span[@aria-controls='StartDate_dateview']//span[@class='k-icon k-i-calendar']")

    def __init__(self,driver):
        self.driver = driver


    def Sales(self):
        self.driver.find_element(*SalesA.click_Sales_XPATH).click()
    def Shiping(self):
        self.driver.find_element(*SalesA.click_Shiping_XPATH).click()

    def Startdate(self,date):
        self.driver.find_element(*SalesA.clicK_Start_Date_XPATH).send_keys(date)

    def Calender(self):
        self.driver.find_element(*SalesA.click_Calender_XPATH).click()



