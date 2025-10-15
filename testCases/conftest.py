import os.path

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        driver = webdriver.Edge()
        print("Edge launched")

    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Firefox launched")

    else:
        driver = webdriver.Chrome()
        print("Chrome launched")

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

    #driver = webdriver.Chrome()
    #return driver

##########PyTest HTML Report#########

# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Customer Reg'
#     config._metadata['Module Name'] = 'Customer registration'
#     config._metadata['Tester'] = 'Rohit joshua'
#
# ##hook for delete/modify
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)

