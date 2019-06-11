from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login.login_page import LoginPage

import unittest

class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseURL = "https://www.amazon.in"
        path = "/Users/aravindanathdm/Documents/PythonPOM_FW/driver/chromedriver"
        driver =  webdriver.Chrome(executable_path=path)
        driver.fullscreen_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)


        lp = LoginPage(driver)
        lp.login("stiku6033@amazon.com","amazonapps")






if __name__ == "__main__":
    unittest.main(verbosity=2)

