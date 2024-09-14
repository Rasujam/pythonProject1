import os.path
from datetime import datetime
import pytest
from selenium import webdriver



@pytest.fixture
def setup(browser):
    if browser == "chrome":
        from selenium.webdriver.chrome.service import Service
        serv_obj = Service()
        driver = webdriver.Chrome(service=serv_obj)
    elif browser == "edge":
        from selenium.webdriver.edge.service import Service
        serv_obj = Service()
        driver = webdriver.Edge(service=serv_obj)
    elif browser == "firefox":
        from selenium.webdriver.firefox.service import Service
        serv_obj = Service()
        driver = webdriver.Firefox(service=serv_obj)
    else:
        from selenium.webdriver.chrome.service import Service
        serv_obj = Service()
        driver = webdriver.Chrome(service=serv_obj)
    yield driver
    driver.close()


def pytest_addoption(parser):  # This will get the value from CLI
    parser.addoption("--browser")

@pytest.fixture() # This will return the Browser value to setup method
def browser(request):
    return request.config.getoption("--browser")


# customizing reHTML Report
# It is hook for Adding Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([extras.html('<p>Project Name: Orange HRM</p>')])
    prefix.extend([extras.html('<p>Module Name: Login Module</p>')])
    prefix.extend([extras.html('<p>Tester Name: Rasul</p>')])

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    # metadata.pop("Python", None)
    # metadata.pop("Platform", None)
    metadata.pop("Plugins",None)
    metadata.pop("JAVA_HOME",None)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = "C:\\Users\\rasul\\PycharmProjects\\pythonProject\\OpencartV1\\pythonProject1\\reports\\" + datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"




