from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

class CustomerRegistration:
    txtbox_fname_id = "first_name"
    txtbox_lname_id = "last_name"
    txtbox_dob_id = "dob"
    txtbox_street_id = "street"
    txtbox_zipcode_id = "postal_code"
    txtbox_city_id = "city"
    txtbox_state_id = "state"
    dropdown_country_id = "country"
    txtbox_phnum_id = "phone"
    txtbox_email_id = "email"
    txtbox_pswd_id = "password"
    btn_newregister_xpath = "//button[normalize-space()='Register']"


    def __init__(self, driver):
        self.driver = driver

    def setFname(self,fname):
        self.driver.find_element(By.ID, self.txtbox_fname_id).send_keys(fname)

    def setLname(self,lname):
        self.driver.find_element(By.ID, self.txtbox_lname_id).send_keys(lname)

    def setdob(self,dob):
        self.driver.find_element(By.ID, self.txtbox_dob_id).send_keys(dob)

    def setStreet(self,street):
        self.driver.find_element(By.ID, self.txtbox_street_id).send_keys(street)

    def setZipCd(self,zipcode):
        self.driver.find_element(By.ID, self.txtbox_zipcode_id).send_keys(zipcode)

    def setCity(self, city):
        self.driver.find_element(By.ID, self.txtbox_city_id).send_keys(city)

    def setState(self, state):
        self.driver.find_element(By.ID, self.txtbox_state_id).send_keys(state)

    def setCountry(self,country):
        dropdown_element = self.driver.find_element(By.ID, self.dropdown_country_id)
        ctry1 = Select(dropdown_element)
        ctry1.select_by_visible_text(country)

    def setPhone(self,phonenum):
        self.driver.find_element(By.ID, self.txtbox_phnum_id).send_keys(phonenum)

    def setEmail(self,email):
        self.driver.find_element(By.ID, self.txtbox_email_id).send_keys(email)

    def setPswd(self, pswd):
        self.driver.find_element(By.ID, self.txtbox_pswd_id).send_keys(pswd)

    def clickRegisterNew(self):
        self.driver.find_element(By.XPATH, self.btn_newregister_xpath).click()

