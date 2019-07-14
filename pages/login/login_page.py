from base.selenium_driver import SeleniumDriver
import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)
    # Constructor will accept driver
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _title_xpath ="(//i[starts-with(@class,'a-icon')])[1]"
    _search_id = "twotabsearchtextbox"
    _sign_in_xpath = "//span[text()='Hello, Sign in']"
    _email_field_id = "ap_email"
    _pwd_field_id = "ap_password"
    _continue_button_id = "continue"
    _login_button_id ="signInSubmit"
    _create_Account_Button_id ="createAccountSubmit"



    # Actions


    def assertLoginPgTitle(self):
        self.assertTitle("Amazon",self._title_xpath,locatorType="xpath")


    def search(self,data):
        self.sendKeysWithEnter(data,self._search_id,locatorType="id")


    def clickSigninLink(self):
        self.elementClick(self._sign_in_xpath,locatorType="xpath")



      
    def clickContinueBtn(self):
        self.elementClick(self._continue_button_id)


    def clickLoginBtn(self):
        self.elementClick(self._login_button_id)


    def enterEmail(self, email):
        self.sendKeys(email, self._email_field_id)

    def enterPassword(self, password):
        self.sendKeys(password, self._pwd_field_id)

    def createNewAccount(self):
        self.elementClick(self._create_Account_Button_id)



    # Business logic


    # def login(self,data,email,password):
    #     time.sleep(2)
    #     self.clickSigninLink()
    #     bool=self.isElementPresent(self._title_xpath, locatorType="xpath")
    #     print(bool)
    #     self.enterEmail(email)
    #     self.clickContinueBtn()
    #     self.take_Screenshot(driver=self.driver)
    #     self.enterPassword(password)
    #     self.clickLoginBtn()
    #     time.sleep(2)
    #     self.search(data)
    #     time.sleep(5)

    def login(self, email="", password=""):
        print(self.verifyPageTitle("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"))
        time.sleep(2)
        self.clickSigninLink()
        bool=self.isElementPresent(self._title_xpath, locatorType="xpath")
        print(bool)
        self.enterEmail(email)
        self.clickContinueBtn()
        self.take_Screenshot(driver=self.driver)
        self.enterPassword(password)
        self.clickLoginBtn()

    def inValidlogin(self):
        time.sleep(2)
        print(self.util.getUniqueMobileNo())
        self.verifyPageTitle
        ("google")
        # self.clickSigninLink()
        # self.enterEmail(email)
        # self.clickContinueBtn()
        # self.clickLoginBtn()


    def verifyLoginSuccessful(self):
        result = self.isElementPresent("twotabsearchtextbox",
                                       locatorType="id")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//*[@id='auth-email-missing-alert']/div/div]",
                                       locatorType="xpath")
        return result

    def createNewAc(self):
        self.createNewAccount()