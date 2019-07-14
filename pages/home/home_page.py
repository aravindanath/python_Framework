from base.selenium_driver import SeleniumDriver
import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class HomePage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    # Constructor will accept driver
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

#     Locators

    _search_id = "twotabsearchtextbox"

    # Actions


    def search(self, data):
        self.sendKeysWithEnter(data, self._search_id, locatorType="id")


    def searchProduct(self,data=""):
        self.search(data)



