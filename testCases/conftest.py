import os.path
from datetime import datetime
import pytest
from selenium import webdriver



@pytest.fixture
def setup(browser):
    if browser == "chrome":
        from selenium.webdriver.chrome.service import Service
        serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
    elif browser == "edge":
        from selenium.webdriver.edge.service import Service
        serv_obj = Service("C:\Drivers\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service=serv_obj)
    elif browser == "firefox":
        from selenium.webdriver.firefox.service import Service
        serv_obj = Service("C:\Drivers\geckodriver-v0.34.0-win64\geckodriver.exe")
        driver = webdriver.Firefox(service=serv_obj)
    else:
        from selenium.webdriver.chrome.service import Service
        serv_obj = Service()
        driver = webdriver.Chrome(service=serv_obj)
    return driver


def pytest_addoption(parser):  # This will get the value from CLI
    parser.addoption("--browser")

@pytest.fixture() # This will return the Browser value to setup method
def browser(request):
    return request.config.getoption("--browser")


# customizing reHTML Report
# It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config.metadata['Project Name'] = 'Opencart'
#     config.metadata['Module Name'] = 'AccountRegistration'
#     config.metadata['Tester Name'] = 'Pavan'



# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = "C:\\Users\\rasul\\PycharmProjects\\pythonProject\\OpencartV1\\pythonProject1\\reports\\" + datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"




