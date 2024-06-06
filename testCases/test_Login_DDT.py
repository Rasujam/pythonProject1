import time
import pytest

from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from pageObjects.myAccountPage import MyAccountPage
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os


class Test_Login_DDT:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    path = "/testData/Opencart_LoginData.xlsx"

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("**** Starting Login Data Driven Test")
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        list_status = []

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.homePage = HomePage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.myAccount = MyAccountPage(self.driver)

        for r in range(2, self.rows + 1):
            self.homePage.clickMyAccount()
            self.homePage.clickLogin()

            self.email = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.expectedResult = XLUtils.readData(self.path, "Sheet1", r, 3)
            self.loginPage.setEmail(self.email)
            self.loginPage.setPassword(self.password)
            self.loginPage.clickLogin()
            time.sleep(3)
            self.targetPage = self.loginPage.isMyAccountPageExist()

            if self.expectedResult == "Valid":
                if self.targetPage == True:
                    list_status.append('PASS')
                    self.myAccount.clickLogout()
                else:
                    list_status.append('FAIL')
            elif self.expectedResult == "Invalid":
                if self.targetPage == True:
                    list_status.append('FAIL')
                    self.myAccount.clickLogout()
                else:
                    list_status.append('PASS')
        self.driver.close()

        if "FAIL" not in list_status:
            assert True
        else:
            assert False
        self.logger.info("*****Login Date Driver Test Finished*****")
