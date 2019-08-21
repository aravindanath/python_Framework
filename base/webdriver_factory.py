"""
WebDriver factory implementation
It creates a webdriver instance based on browser configuration

example:
    wdf= WebDriverFactory(browser)
    wdf.getWebDriverInstance()




"""

import traceback
from selenium import webdriver


class WebDriverFactory():


    def __init__(self,browser):

        """
        Inits WebDriverFactory class
        Return None:
        :param browser:
        """
        self.browser = browser

    """
        Set chrome driver and iexplorer env based on OS
        
    """
    def getWebDriverInstance(self):
        """
        Get webdriver instance based on the browser configuration

        :return:

            'webDriver Instance'

        """
        baseURL = "https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"

        if self.browser == "chrome":
            path = "/Users/aravindanathdm/Documents/Simple_Pom_py_fw/driver/chromedriver"
            driver = webdriver.Chrome(executable_path=path)
            print("running on chrome")
        elif self.browser == "firefox":
            path = "/Users/aravindanathdm/Documents/Simple_Pom_py_fw/driver/geckodriver"
            driver = webdriver.Firefox(executable_path=path)
            print("running on firefox")
        else:
            path = "/Users/aravindanathdm/Documents/Simple_Pom_py_fw/driver/geckodriver"
            driver = webdriver.Firefox(executable_path=path)
            print("running on firefox")

        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(30)
            # Maximize the window
        driver.fullscreen_window()
            # Loading browser with App URL
        driver.get(baseURL)
        return driver

