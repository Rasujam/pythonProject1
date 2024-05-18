from selenium.webdriver.common.by import By
from selenium import webdriver


class MyAccountPage:
    def __init__(self, driver):
        self.driver = driver

    lnk_logout_xpath = "//div[@class='dropdown']/ul/li/a[text()='Logout']"

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.lnk_logout_xpath).click()




