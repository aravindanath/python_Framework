
from pages.login.login_page import LoginPage
from pages.home.home_page import HomePage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time




@pytest.mark.usefixtures("oneTimeSetUp")
class CreateAccountTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.hp = HomePage(self.driver)

    @pytest.mark.run(order=1)
    def test_CreateAccount(self):
        self.lp.createNewAccount()
        time.sleep(6)