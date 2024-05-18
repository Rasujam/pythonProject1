from pageObjects.homePage import HomePage
from pageObjects.registerAccountPage import RegisterAccount
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen # for logging
import os





class Test_AccountReg:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen() # for logging

    def test_Account_Reg(self, setup):
        self.logger.info("****test_AccountReg started****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Launching Application")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.homePage = HomePage(self.driver)
        self.logger.info("clicking on MyAccount --> register")
        self.homePage.clickMyAccount()
        self.homePage.clickRegister()
        self.logger.info("Providing customer details for registration")
        self.regPage = RegisterAccount(self.driver)
        self.regPage.setFirstName("Omarr")
        self.regPage.setLastName("Ramoo")
        # self.email = randomString.random_string_generator()+'@gmail.com'
        self.regPage.setEmail(ReadConfig.getUserEmail())
        self.regPage.setPassword(ReadConfig.getPassword())
        self.regPage.setSubscribeButtonToYes()
        self.regPage.setPrivacyPolicy()
        self.regPage.clickContinueButton()
        actualTitle = self.driver.title
        print(actualTitle)
        self.confMessage = self.regPage.getConfirmationMsg()
        if self.confMessage == "Your Account Has Been Created!":
            self.logger.info("Account registration is passed..")
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\rasul\\PycharmProjects\\pythonProject\\OpencartV1\\pythonProject1\\screenShots\\"+"test_AccountReg.png")
            self.logger.error("Account registration is failed..")
            self.driver.close()
            assert False
        self.logger.info("****test_AccountReg finished****")
