import pytest
from utils.constants import *

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in your browser name e,g chrome, Firefox")

@pytest.fixture(scope='class')
def test_launch_browser(request):
    from selenium import webdriver
    driver=request.config.getoption("--browser")
    #global driver
    if driver == "chrome":
        driver = webdriver.Chrome(executable_path="C:/Users/Dell/PycharmProjects/Automation_POM_Framework2/drivers/chromedriver.exe")
        #driver = webdriver.Chrome(executable_path=PATH)
    elif driver == "ff":
        driver = webdriver.Firefox(executable_path="C:/Users/Dell/PycharmProjects/Automation_POM_Framework2/drivers/geckodriver.exe")
    driver.get(URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver=driver
    yield
    driver.quit()