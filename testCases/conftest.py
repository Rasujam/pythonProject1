import os.path
from datetime import datetime
import pytest
from selenium import webdriver
from pytest_html import extras
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService



# @pytest.fixture
# def setup(browser):
#     if browser == "chrome":
#         from selenium.webdriver.chrome.service import Service
#         serv_obj = Service()
#         driver = webdriver.Chrome(service=serv_obj)
#     elif browser == "edge":
#         from selenium.webdriver.edge.service import Service
#         serv_obj = Service()
#         driver = webdriver.Edge(service=serv_obj)
#     elif browser == "firefox":
#         from selenium.webdriver.firefox.service import Service
#         serv_obj = Service()
#         driver = webdriver.Firefox(service=serv_obj)
#     else:
#         from selenium.webdriver.chrome.service import Service
#         serv_obj = Service()
#         driver = webdriver.Chrome(service=serv_obj)
#     yield driver
#     driver.close()

@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
    elif browser == 'firefox':
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    else:  # default to Chrome
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()



def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to use for tests"
    )

@pytest.fixture() # This will return the Browser value to setup method
def browser(request):
    return request.config.getoption("--browser")


# customizing reHTML Report
# It is hook for Adding Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([extras.html('<p>Project Name: Open Cart</p>')])
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
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\" + datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"




