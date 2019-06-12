from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.selenium_driver import SeleniumDriver
import time

class LoginPage(SeleniumDriver):
 
    # Constructor will accept driver
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_id = "twotabsearchtextbox"
    _sign_in_xpath = "//*[@id='nav-link-accountList']/span[1]"
    _email_field = "ap_email"
    _pwd_field = "ap_password"
    _continue_button = "continue"
    _login_button ="signInSubmit"

    # def getSignIn(self):
    #     return self.find_element(By.LINK_TEXT,self._sign_in_link)
    #
    # def getEmail(self):
    #     return self.find_element(By.ID, self._email_field)
    #
    # def getPassword(self):
    #     return self.find_element(By.ID, self._pwd_field)
    #
    # def getContinueBtn(self):
    #     return self.find_element(By.ID, self._continue_button)
    #
    # def getLoginBtn(self):
    #     return self.find_element(By.ID, self._login_button)

    # Actions
    def search(self,data):
        self.sendKeys(data,self._search_id,locatorType="id")


    def clickSigninLink(self):
        self.elementClick(self._sign_in_xpath,locatorType="xpath")


    def enterEmail(self,email):
        self.sendKeys(email,self._email_field,locatorType="id")

      
    def clickContinueBtn(self):
        self.elementClick(self._continue_button,locatorType="id")


    def enterPassword(self, pwd):
        self.sendKeys(pwd, self._pwd_field, locatorType="id")


    def clickLoginBtn(self):
        self.elementClick(self._login_button,locatorType="id")



    def login(self,data,email,password):

        # self.clickSigninLink()

        self.enterEmail(email)
        self.clickContinueBtn()
        self.take_Screenshot(driver=self.driver)
        self.enterPassword(password)
        self.clickLoginBtn()
        time.sleep(5)
        self.search(data)
        time.sleep(5)


