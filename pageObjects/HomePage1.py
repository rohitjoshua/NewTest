from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePageV1:
    lnk_SignIn_xpath = "//a[contains(text(), 'Sign in')]"
    lnk_Register_xpath = "//a[contains(text(), 'Register')]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)  # wait up to 15 seconds

    def clicksignin(self):
        sign_in_element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.lnk_SignIn_xpath))
        )
        sign_in_element.click()

    def clickregister(self):
        register_element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.lnk_Register_xpath))
        )
        register_element.click()
