

import time

import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from pageObjects.Login import LoginPage
from utilities.Logger import LogGenerator
from utilities.Readproperties import Readconfig


class Test_Login:
    Url = Readconfig.geturl()
    Email = Readconfig.getEmail()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()


    @pytest.mark.sanity
    def test_login002(self, setup):
        self.driver = setup
        self.log.info("test login 02 is stared")
        self.log.info("opening Browser")
        self.driver.get(self.Url)
        self.log.info("GO to this Url -->" + self.Url)
        self.lp = LoginPage(self.driver)
        self.lp.Enter_Email(self.Email)
        self.log.info("Entering Email-->" + self.Email)
        self.lp.Enter_Password(self.password)
        self.log.info("Entering Password-->" + self.password)
        self.lp.Click_Login()
        self.log.info("click on login Button")
        # if self.driver.title == "Dashboard / nopCommerce administration":
        if self.lp.login_Status()==True:
            self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\non commerce\\Screenshot\\test_login.py-Pass.png")
            time.sleep(2)
            self.lp.Click_Menu_Button()
            self.lp.Click_Logout()
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\non commerce\\Screenshot\\test_login.py-Fail.png")
            assert False







