
import time

import pytest
from selenium import webdriver

from selenium.common import NoSuchElementException as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from pageObjects.Login import LoginPage
from utilities.Logger import LogGenerator
# from utilities.Logger import LogGenerator
# from utilities.Logger import LogGenerator
from utilities.Readproperties import Readconfig



class Test_Login_Params:

    Url = Readconfig.geturl()
    Email = Readconfig.getEmail()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()
    @pytest.mark.sanity
    def test_params04(self,setup,getDataforlogin):
        self.driver = setup
        self.log.info("test login params 004 is started")
        self.log.info("opening browser")
        self.driver.get(self.Url)
        self.log.info("GO to this URL-->" + self.Url)
        self.lp = LoginPage(self.driver)
        self.lp.Enter_Email(getDataforlogin[0])
        self.log.info("Entering Email-->" + getDataforlogin[0])
        self.log.info("Entering Email-->" + self.Email)
        self.lp.Enter_Password(getDataforlogin[1])
        self.log.info("Entering password --->" + getDataforlogin[1])
        self.log.info("Entering password -->" + self.password)
        self.lp.Click_Login()
        self.log.info("click on login button")
        login_list = []
        if self.driver.title == "Dashboard / nopCommerce administration":
            if getDataforlogin[2] == "Pass":
                self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\non commerce\\Screenshot\\test_params.py-Pass.png")
                time.sleep(2)
                self.lp.Click_Logout()
                self.log.info("click on logout button")
                self.log.info("test param is passed")
                assert True
            else:
                self.log.info("test param is failed")
                self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\non commerce\\Screenshot\\test_params.py-Pass.png")
                assert False
        else:
            self.log.info("test login is failed")
            if getDataforlogin[2] == "Fail":
                assert True
            else:
                assert False
        print(login_list)
        self.driver.close()
        self.log.info("test param is completed")










































































































# #
#
#     def test_login_params_004(self,setup,getDataforlogin):
#         self.driver = setup
#         self.log.info("test_logins_param_004 is started")
#         self.log.info("Opening Browser")
#         self.driver.get(self.Url)
#         self.log.info("Go to this url-->" + self.Url)
#
#         self.lp = LoginPage(self.driver)
#         self.lp.Enter_Email(getDataforlogin[0])
#         self.log.info("Entering username-->" + getDataforlogin[0])
#         self.log.info("Entering username -->" + self.username)
#         self.lp.Enter_Password(getDataforlogin[1])
#         # self.log.info("Entering password-->" + getDataforlogin[1])
#         # self.log.info("Entering password-->" + self.password)
#         self.lp.Click_Login()
#         statusList =[]
#         if self.lp.Title() == "Dashboard":
#             if getDataforlogin[2] == "Pass":
#                 # self.log.info("Page Title -->" + self.driver.title)
#                 self.lp.Click_Menu_Button()
#                 # self.log.info("Clicking Menu Button")
#                 # self.driver.save_screenshot(
#                 #     "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\PhpTravel\\Screenshots"
#                 #     "\\" + getDataforlogin[0] + getDataforlogin[0] + "test_login_Params_003_pass.PNG")
#                 # # time.sleep(2)
#                 self.lp.Click_Logout()
#         #         # self.log.info("Clicking Logout Button")
#                 statusList.append("Pass")
#         #
#             elif getDataforlogin[2] == "Fail":
#         # #         self.log.info("Page Title -->" + self.driver.title)
#                 self.lp.Click_Menu_Button()
#         # #         self.log.info("Clicking Menu Button")
#         # #         self.driver.save_screenshot(
#         # #             "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\PhpTravel\\Screenshots"
#         # #             "\\" + getDataforlogin[0] + getDataforlogin[0] + "test_login_Params_003_fail.PNG")
#         # #         # time.sleep(2)
#                 self.lp.Click_Logout()
#         # #         self.log.info("Clicking Logout Button")
#                 statusList.append("Fail")
#         # #
#         else:
#             if getDataforlogin[2] == "Pass":
#         # #         self.log.info("Page Title -->" + self.driver.title)
#         # #         self.driver.save_screenshot(
#         # #             "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\PhpTravel\\Screenshots"
#         # #             "\\" + getDataforlogin[0] + getDataforlogin[0] + "test_login_Params_003_fail.PNG")
#                 statusList.append("Fail")
#         # #
#             elif getDataforlogin[2] == "Fail":
#         # #         self.log.info("Page Title -->" + self.driver.title)
#         # #         self.driver.save_screenshot(
#         # #             "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\PhpTravel\\Screenshots"
#         # #             "\\" + getDataforlogin[0] + getDataforlogin[0] + "test_login_Params_003_pass.PNG")
#                 statusList.append("Pass")
#         #
#         if "Fail" not in statusList:
#             assert True
#         #     # self.log.info("test_login_Params_003 is Passed")
#         else:
#             assert False
#         #     # self.log.info("test_login_Params_003 is Failed")
#         # self.log.info("test_login_Params_003 is Completed")
#
#         # self.log.info("Click on login button")
#         if self.lp.Login_Status() == True:
#             if getDataforlogin[2] == "Pass":
#         #         # self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\pythonpytest\\ScreenShots\\test_login_002-pass.png")
#         #
#                 self.lp.Click_Menu_Button()
#         #         # self.log.info("Click on Menu button")
#                 self.lp.Click_Logout()
#         #         # self.log.info("Click on logout button")
#         #         # self.log.info("test_login_002 is Passed")
#                 assert True
#             else:
#         #         # self.log.info("test_login_002 is Failed")
#         #         # self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\pythonpytest\\ScreenShots\\test_login_002-fail.png")
#         #
#                 assert False
#         else:
#             if getDataforlogin[2] == "Fail":
#                 assert True
#             else:
#         #         # self.log.info("test_login_002 is Failed")
#         #         # self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\pythonpytest\\ScreenShots\\test_login_002-fail.png")
#                 assert False
#         #
#         self.driver.close()
#         # # self.log.info("test_login_002 is Completed")
