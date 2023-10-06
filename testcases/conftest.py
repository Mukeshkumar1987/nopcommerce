# import pytest
# from selenium import webdriver
#
#
# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     driver.get("https://admin-demo.nopcommerce.com/")
#     return driver

import pytest

from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser")


# Define the browser fixture function with a single argument, request.
# Within the browser function, use the request.config.getoption() method to get the value of the --browser option passed to pytest on the command line.
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    elif browser == 'edge':
        print("Launching Edge Browser")
        driver = webdriver.Edge()
    else:
        print("Headless mode")
        chrome_options = webdriver.FirefoxOptions()
        # chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver







@pytest.fixture(params=[
    ("admin@yourstore.com","admin", "Pass"),
    ("admin@yourstore.com1", "admin", "Fail"),
    ("admin@yourstore.com", "admin1","Fail"),
    ("admin@yourstore.com2", "admin1231", "Fail")
])
def getDataforlogin(request):
    return request.param
