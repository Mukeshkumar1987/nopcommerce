# import time
# from selenium.webdriver.support import expected_conditions as EC
import time

from pageObjects.AddCustomers import AddCustomer
from pageObjects.Login import LoginPage
from utilities.Logger import LogGenerator
from utilities.Readproperties import Readconfig
class Test_Customer:
    Url = Readconfig.geturl()
    Email = Readconfig.getEmail()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()
    def test_AddCust003(self,setup):
        self.driver = setup
        self.log.info(" test 003 is staretd")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("GO to this Url-->" + self.Url)
        self.lp = LoginPage(self.driver)
        self.lp.Enter_Email(self.Email)
        self.log.info("Enterting the Email" + self.Email)
        self.lp.Enter_Password(self.password)
        self.log.info("Entering the Password" + self.password)
        self.lp.Click_Login()
        self.log.info("click the login Button")
        self.ca = AddCustomer(self.driver)
        self.ca.click_Customers()
        self.log.info("Click the Customer Buttion")
        # time.sleep(2)
        self.ca.click_inside_button()
        self.log.info("click inside button")
        # time.sleep(2)
        self.ca.Click_AddNew()
        self.log.info("click new add")
        # time.sleep(2)
        self.ca.Enter_Email("anupama@gmail.com")
        self.log.info("click the new Email")
        self.ca.Enter_Password("rajamohan")
        self.log.info("Click the new Password")
        # time.sleep(2)
        self.ca.Enter_First_name("kaja")
        self.log.info("click the first name")
        self.ca.Enter_Last_name("sign")
        self.log.info("click the last name")
        self.ca.Enter_Gender()
        self.log.info("Enter the Gender")
        self.ca.Click_Date_Of_Birth("06/20/2000")
        self.log.info("Enter the DOB")
        # self.ca.Click_Calender()
        self.log.info("Click the Calender")
        self.ca.Click_save()
        # time.sleep(2)
        self.log.info("click the save")
        if self.ca.AddEmloyee_Status() == True:
            self.lp.Click_Menu_Button()
            self.lp.Click_Logout()
            assert True
        else:
            assert False
        self.driver.close()




        # if self.driver.title == "Customers / nopCommerce administration":
        #     self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\non commerce\\Screenshot\\test_Addnew.py-Pass.png")
        #     # time.sleep(2)
        #     self.lp.Click_Logout()
        #     assert True
        # else:
        #     self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\non commerce\\Screenshot\\test_Addnew.py-Fail.png")
        #
        #     assert False
        #
        #
















# quantityp1 = Select(driver.find_element(By.XPATH,"//tbody/tr[1]/td[3]/select[1]"))
# quantityp1.select_by_index(2)
#
# quantityp2 = Select(driver.find_element(By.XPATH,"//tbody/tr[2]/td[3]/select[1]"))
# quantityp2.select_by_index(3)
#
# time.sleep(2)



