from base.selenium_driver import SeleniumDriver
import time
import utilities.custom_logger as cl
import logging
from utilities.utils import Util
from base.basepage import BasePage


class AddressPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    # Constructor will accept driver
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #     Locators

    _accounts_xpath = "//*[@id='nav-link-accountList']/span[2]"
    _yourAccount_link ="Your Account"
    _yourAddress_xpath = "//h2[contains(text(),'Your Addresses')]"
    _addAddress_xpath ="//h2[contains(text(),'Add address')]"
    _fullname_id="address-ui-widgets-enterAddressFullName"
    _mobile_number_id="address-ui-widgets-enterAddressPhoneNumber"

    #Actions


    def mouseHoverOnAccout(self):
        self.mouseHover(self._accounts_xpath,locatorType="xpath")

    def clickOnYourAccount(self):
        self.elementClick(self._yourAccount_link,locatorType="link")

    def clickOnAddressTab(self):
        self.elementClick(self._yourAddress_xpath,locatorType="xpath")

    def clickOnAddAddress(self):
        self.elementClick(self._addAddress_xpath,locatorType="xpath")

    def sendFullName(self,data):
        self.sendKeys(data,self._fullname_id,locatorType="id")

    def mobileNum(self,data):
        self.sendKeys(data,self._mobile_number_id,locatorType="id")


    # Logic

    def addNewAddress(self,fullname=""):
        self.mouseHoverOnAccout()
        self.clickOnYourAccount()
        time.sleep(2)
        self.clickOnAddressTab()
        self.clickOnAddAddress()
        self.sendFullName(fullname)
        mobile = Util.getUniqueMobileNo()
        self.mobileNum(mobile)



