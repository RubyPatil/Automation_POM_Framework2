import time
import os
from selenium import webdriver
import pytest
from pages.loginpage import LoginPage
from pages.homepage import HomePage

class TestLogin:
    @pytest.fixture(scope='class')
    def test_launch_browser(self):
        global driver
        driver=webdriver.Chrome(executable_path="C:/Users/Dell/PycharmProjects/Automation_POM_Framework/drivers/chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get("http://localhost:9001/login.do")

    def test_login(self,test_launch_browser):
        lp=LoginPage(driver)
        lp.enter_user_name()
        lp.enter_password()
        lp.click_on_login_btn()

        # driver.find_element_by_name("username").send_keys("admin")
        # driver.find_element_by_name("pwd").send_keys("manager")
        # driver.find_element_by_xpath("//*[text()='Login ']").click()

    def test_logout(self,test_launch_browser):

        time.sleep(5)
        hp=HomePage(driver)
        hp.click_on_logout_btn()
        # driver.find_element_by_xpath("//*[text()='Logout']").click()

