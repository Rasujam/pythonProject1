from selenium import webdriver
from selenium.webdriver.common.by import By




class RegisterAccount:

    def __init__(self, driver):
        self.driver = driver

    first_Name_Input_Box_id = "input-firstname"
    last_Name_Input_Box_id = "input-lastname"
    email_Input_Box_id = "input-email"
    password_Input_Box_id = "input-password"
    subscribe_Yes_Button_id = "input-newsletter-yes"
    subscribe_No_Button_id = "input-newsletter-no"
    continueButton_xpath = "//button[text()='Continue']"
    privacyPolicyCheckBox_xpath = "//input[@type='checkbox']"
    text_Msg_Conf_xpath = "//div[@id='content']/h1"

    def setFirstName(self, firstName):
        txt_First_Name = self.driver.find_element(By.ID, self.first_Name_Input_Box_id)
        txt_First_Name.clear()
        txt_First_Name.send_keys(firstName)

    def setLastName(self, lastName):
        txt_Last_Name = self.driver.find_element(By.ID, self.last_Name_Input_Box_id)
        txt_Last_Name.clear()
        txt_Last_Name.send_keys(lastName)

    def setEmail(self, email):
        txt_Email = self.driver.find_element(By.ID, self.email_Input_Box_id)
        txt_Email.clear()
        txt_Email.send_keys(email)

    def setPassword(self, password):
        txtPassword = self.driver.find_element(By.ID, self.password_Input_Box_id)
        txtPassword.clear()
        txtPassword.send_keys(password)

    def setSubscribeButtonToYes(self):
        self.driver.find_element(By.ID, self.subscribe_Yes_Button_id).click()

    def setPrivacyPolicy(self):
        self.driver.find_element(By.XPATH, self.privacyPolicyCheckBox_xpath).click()

    def clickContinueButton(self):
        self.driver.find_element(By.XPATH, self.continueButton_xpath).click()

    def getConfirmationMsg(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_Msg_Conf_xpath).text
        except:
            None

