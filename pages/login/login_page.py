from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.selenium_driver import SeleniumDriver
class LoginPage(SeleniumDriver):
 
    # Constructor will accept driver
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _sign_in_link = "Hello, Sign in"
    _email_field = "ap_email"
    _pwd_field = "ap_password"
    _continue_button = "continue"
    _login_button ="signInSubmit"

    def getSignIn(self):
        return self.find_element(By.LINK_TEXT,self._sign_in_link)

    def getEmail(self):
        return self.find_element(By.ID, self._email_field)

    def getPassword(self):
        return self.find_element(By.ID, self._pwd_field)

    def getContinueBtn(self):
        return self.find_element(By.ID, self._continue_button)

    def getLoginBtn(self):
        return self.find_element(By.ID, self._login_button)

    # Actions

    def clickSigninLink(self):
        self.getSignIn().click()

    def enterEmail(self,email):
        self.getEmail().send_keys(email)
      
    def clickContinueBtn(self):
        self.getContinueBtn().click()

    def enterPassword(self, pwd):
        self.getPassword().send_keys(pwd)

    def clickLoginBtn(self):
        self.getLoginBtn().click()



    def login(self,email,password):
        self.clickSigninLink()
        self.enterEmal(email)
        self.clickContinueBtn()
        self.enterPassword(password)
        self.clickLoginBtn()



