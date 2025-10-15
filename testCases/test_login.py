import pytest
from pageObjects.LoginPage import LoginPageNew
from utilities.readProperties import ReadConfig
from utilities import XLUtilis
import os

class Test_Login():
    baseURL = ReadConfig.getApplicationURL()

    user = ReadConfig.getUseremail()
    pwd = ReadConfig.getPassword()

    @pytest.mark.sanity
    #pytest -s -v .\testCases\ -m "sanity"
    # pytest -s -v .\testCases\ -m "sanity and regression"

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPageNew(self.driver)
        self.lp.setLoginusr(self.user)
        self.lp.setLoginPassword(self.pwd)
        self.lp.clickLoginbtn()


        self.targetpage = self.lp.isMyAccountdipsplayed()
        if self.targetpage == "Logged In Successfully":
            assert True
            self.driver.close()
        else:
            screenshot_path = os.path.abspath(os.curdir) + "\\screenshots\\test_login.png"
            self.driver.save_screenshot(screenshot_path)

            self.driver.close()
            assert False






