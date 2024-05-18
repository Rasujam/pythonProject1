from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    button_MyAccount_xpath = "//span[text()='My Account']"
    reg_button_link_text = "Register"
    login_button_link_text = "Login"

    def clickMyAccount(self):
        myAccountButton = self.driver.find_element(By.XPATH, self.button_MyAccount_xpath)
        myAccountButton.click()

    def clickRegister(self):
        registerButton = self.driver.find_element(By.LINK_TEXT, self.reg_button_link_text)
        registerButton.click()

    def clickLogin(self):
        loginButton = self.driver.find_element(By.LINK_TEXT, self.login_button_link_text)
        loginButton.click()
