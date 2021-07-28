import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):
    if browser=="chrome":
        driver = webdriver.Chrome()
    else:
        driver=webdriver.Firefox()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return  request.config.getoption("--browser")


####PYTEST HTML REPORT######

def pytest_configure(config):
    config._metadata['Project name']="NOP COMMERCE"
    config._metadata['Module name']='customer'
    config._metadata['Tester'] = 'NArendra'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


