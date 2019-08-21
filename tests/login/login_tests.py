
from pages.login.login_page import LoginPage
from pages.home.home_page import HomePage
from utilities.teststatus import TestStatus
from pages.address.address_page import AddressPage

import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.hp = HomePage(self.driver)
        # self.ap = AddressPage(self.driver)



    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.lp.login("stiku6033@gmail.com", "amazonapps")
        # Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in
        title = self.lp.verifyTitle("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")
        self.ts.mark(title, "Title mismatch!")
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin",result,"Login was not successful")
        self.hp.search("iphone 7")

    # @pytest.mark.run(order=3)
    # def test_invalidLogin(self):
    #     self.lp.inValidlogin()
    # #     result = self.lp.verifyLoginFailed()
    # #     self.ts.markFinal("test_invalidLogin", result, "Login was not successful")
