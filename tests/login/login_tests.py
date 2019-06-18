from selenium import webdriver
from pages.login.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)


    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.lp.login("stiku6033@gmail.com", "amazonapps")

        title = self.lp.verifyTitle("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")
        self.ts.mark(title, "Title mismatch!")
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin",result,"Login was not successful")



    # @pytest.mark.run(order=1)
    # def test_invalidLogin(self):
    #     self.lp.inValidlogin("test@email.com","dummy")
    #     result = self.lp.verifyLoginFailed()
    #     assert result == True