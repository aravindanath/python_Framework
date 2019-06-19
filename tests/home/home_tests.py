from selenium import webdriver
from pages.login.login_page import LoginPage
from pages.home.home_page import HomePage
from utilities.teststatus import TestStatus
import unittest
from ddt import ddt, data, unpack
import pytest
from utilities.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp")
@ddt
class HomeTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.hp = HomePage(self.driver)



    # @pytest.mark.run(order=1)
    # @data(("stiku6033@gmail.com", "amazonapps", "iphone 7"))
    # @unpack
    # def test_validLogin(self,email,password,search):
    #     self.lp.login(email, password)
    #     # Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in
    #     title = self.lp.verifyTitle("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")
    #     self.ts.mark(title, "Title mismatch!")
    #     result = self.lp.verifyLoginSuccessful()
    #     self.ts.markFinal("test_validLogin",result,"Login was not successful")
    #     self.hp.search(search)


    @pytest.mark.run(order=1)
    # * -- means mutiple args
    @data(*getCSVData("/Users/aravindanathdm/Documents/Simple_Pom_py_fw/testdata.csv"))
    @unpack
    def test_validLogin(self,email,password,search):
        self.lp.login(email, password)
        # Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in
        title = self.lp.verifyTitle("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")
        self.ts.mark(title, "Title mismatch!")
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin",result,"Login was not successful")
        self.hp.search(search)

