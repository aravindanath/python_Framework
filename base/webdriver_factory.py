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
        baseURL = "https://www.amazon.in/"

        if self.browser == "chrome":
            path = "/Users/aravindanathdm/Documents/PythonPOM_FW/driver/chromedriver"
            driver = webdriver.Chrome(executable_path=path)
            print("running on chrome")
        elif self.browser == "firefox":
            path = "/Users/aravindanathdm/Documents/PythonPOM_FW/driver/geckodriver"
            driver = webdriver.Firefox(executable_path=path)
            print("running on firefox")
        else:
            path = "/Users/aravindanathdm/Documents/PythonPOM_FW/driver/geckodriver"
            driver = webdriver.Firefox(executable_path=path)
            print("running on firefox")

        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
            # Maximize the window
        driver.maximize_window()
            # Loading browser with App URL
        driver.get(baseURL)
        return driver

