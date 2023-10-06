import time

from pageObjects.Login import LoginPage
from pageObjects.Sales import SalesA
from utilities.Readproperties import Readconfig


class Test_Sales:
    Url = Readconfig.geturl()
    Email = Readconfig.getEmail()
    password = Readconfig.getpassword()


    def test_sales01(self,setup):
        self.driver = setup
        self.driver.get(self.Url)
        self.lp = LoginPage(self.driver)
        self.lp.Enter_Email(self.Email)
        self.lp.Enter_Password(self.password)
        self.lp.Click_Login()
        self.sa = SalesA(self.driver)
        time.sleep(2)
        self.sa.Sales()
        time.sleep(2)
        self.sa.Shiping()
        self.sa.Startdate("5/11/2020")
        self.sa.Calender()



