from pageObjects.HomePage1 import HomePageV1
from pageObjects.CustomerReg import CustomerRegistration
from pageObjects.LoginPage import LoginPageNew
from utilities import randomString
import os
from utilities.customerlogger import LogGen
from utilities.readProperties import ReadConfig


class Test_customerregistartion:

    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()


    def test_accn_reg(self, setup):
        self.logger.info("****test_customer started*****")
        self.driver = setup
        self.logger.info("****Launching application*****")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()


        self.hpv1 = HomePageV1(self.driver)
        self.hpv1.clicksignin()
        self.hpv1.clickregister()

        self.creg = CustomerRegistration(self.driver)
        self.creg.setFname("Rohit")
        self.creg.setLname("Hero")
        self.creg.setdob("1997-06-02")
        self.creg.setStreet("Arogyanagara H Block, RK Nagar")
        self.creg.setZipCd("570022")
        self.creg.setCity("Mysuru")
        self.creg.setState("Karnataka")
        self.creg.setCountry("India")
        self.creg.setPhone("8792882773")

        self.email = randomString.random_string_generator() + "@gmail.com"
        self.password = "IndiaIsMyCountry@0206"

        self.creg.setEmail(self.email)
        self.creg.setPswd(self.password)
        print(self.email)
        self.creg.clickRegisterNew()

        current_url = self.driver.current_url
        print(current_url)

        self.logger.info("****test_customer finished*****")

        self.driver.close()




















