from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginPageNew:
    txtbox_emailaddress_id = "username"
    txtbox_loginpassword_id = "password"
    btn_submit_id = "submit"
    txt_login_xpath = "//h1[normalize-space()='Logged In Successfully']"

    def __init__(self, driver):
        self.driver = driver

    def setLoginusr(self, username):
        self.driver.find_element(By.ID, self.txtbox_emailaddress_id).send_keys(username)

    def setLoginPassword(self, password):
        self.driver.find_element(By.ID, self.txtbox_loginpassword_id).send_keys(password)

    def clickLoginbtn(self):
        self.driver.find_element(By.ID, self.btn_submit_id).click()

    def isMyAccountdipsplayed(self):
        try:
            return self.driver.find_element(By.XPATH,self.txt_login_xpath).text
        except:
            return self.driver
