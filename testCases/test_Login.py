import pytest

from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

import os

class TestLogin:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    user = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_Login(self, setup):
        self.logger.info("*****Starting test_002_login*****")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.homePage = HomePage(self.driver)
        self.logger.info("clicking on MyAccount --> Login")
        self.homePage.clickMyAccount()
        self.homePage.clickLogin()
        self.logger.info("Landed on the Login Page to provide UserName and Password")
        self.login = LoginPage(self.driver)
        self.login.setEmail(ReadConfig.getUserEmail())
        self.login.setPassword(ReadConfig.getPassword())
        self.login.clickLogin()
        self.targetPageMessage = self.login.isMyAccountPageExist()
        if self.targetPageMessage == "My Account":
            self.logger.info("User successfully logged in ")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\rasul\\PycharmProjects\\pythonProject\\OpencartV1\\pythonProject1\\screenShots\\"+"test_Login.png")
            self.logger.info("Login is failed!")
            self.driver.close()
            assert False
        self.logger.info("*****Login Test Finished*****")


