import pytest
import os
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customlogger import LogGen

class Test_001_login():

    baseurl = ReadConfig.getAppilicationUrl()
    username = ReadConfig.getusername()
    password = ReadConfig.getPassword()
    log = LogGen.test_logger()

    def test_home_page(self,setup):

        self.driver = setup

        self.log.critical("************* TC001*********")
        self.log.critical("************* Home Page Title Test is passed*********")

        self.driver.get(self.baseurl)

        act_title = self.driver.title

        if act_title == "Your store. Login":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_home_page.jpg")
            self.driver.close()
            assert False

    def test_Login(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.jpg")
            self.driver.close()
            assert False
