from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture()
def setup():
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

def pytest_configure (config):
    config._metadata = {
        "Project Name": "Hybrid Framework Practice",
        "Module Name": "Customers",
        "Tester": "Sachin"
    }
    metadata = config._metadata
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugin", None)


