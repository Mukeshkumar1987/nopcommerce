

class Test_Page_title():


    def test_title(self, setup):
        self.driver = setup

        if self.driver.title == "Your store. Login":
            print("condtion is True")
            assert True
        else:
            assert False
        self.driver.close()

