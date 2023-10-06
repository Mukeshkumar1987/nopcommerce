import time

from pageObjects.Login import LoginPage
from pageObjects.Products import Product
from utilities.Readproperties import Readconfig


class Test_Products:

    url = Readconfig.geturl()
    email = Readconfig.getEmail()
    password = Readconfig.getpassword()

    def test_Add_Products(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.lp = LoginPage(self.driver)
        self.lp.Enter_Email(self.email)
        self.lp.Enter_Password(self.password)
        self.lp.Click_Login()
        self.ap = Product(self.driver)
        self.ap.click_Catalog()
        time.sleep(6)
        self.ap.click_Product()
        time.sleep(6)
        self.ap.click_AddNew()
        time.sleep(4)
        self.ap.Enter_Product_Name("Apple iCam")
        self.ap.Short_Desc("this is very unique  produts you will never got this other than this")
        self.ap.Drop_down_Category(2)