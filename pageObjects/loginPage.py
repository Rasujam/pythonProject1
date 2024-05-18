from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    txt_email_xpath = "//input[@id='input-email']"
    txt_password_xpath = "//input[@id='input-password']"
    login_button_xpath = "//button[text()='Login']"
    msg_my_account_xpath = "//h2[contains(text(),'My Account')]"

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def isMyAccountPageExist(self):
        try:
            return self.driver.find_element(By.XPATH, self.msg_my_account_xpath).is_displayed()
        except:
            return False


