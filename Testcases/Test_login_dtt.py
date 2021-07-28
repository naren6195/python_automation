import pytest
import os

import self as self
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customlogger import LogGen
from Utilities import XLUtils
import time


class Test_002_DTT_login():

    baseurl = ReadConfig.getAppilicationUrl()
    path=".//TestData/LoginData.xlsx"
    username = ReadConfig.getusername()

    password = ReadConfig.getPassword()
    log = LogGen.logger()

    def test_home_page_dtt(self,setup):

        self.driver = setup
        self.log.info("From DtT")

        self.log.critical("************* TC001*********")
        self.log.critical("************* Home Page Title Test is INITIATED*********")






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
        lst_status=[]
        self.driver = setup
        self.driver.get(self.baseurl)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("No of Rows in Excel Sheet", self.rows)
        self.column = XLUtils.getColumnCount(self.path, 'Sheet1')
        act_title = self.driver.title
        exp_title = "Dashboard / nopCommerce administration"
        if act_title == exp_title:
            if self.exp=='Pass':
                self.log.info("**** passed ****")
                self.lp.clickLogout();
                lst_status.append("Pass")
            elif self.exp=='Fail':
                self.log.info("**** failed ****")
                self.lp.clickLogout();
                lst_status.append("Fail")

            elif act_title!=exp_title:
                if self.exp == 'Pass':
                    self.log.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.log.info("**** passed ****")
                    lst_status.append("Pass")
            print(lst_status)
        if "Fail" not in lst_status:
            self.log.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.log.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        self.log.info("******* End of Login DDT Test **********")
        self.log.info("**************** Completed  TC_LoginDDT_002 ************* ")