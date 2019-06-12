from selenium import webdriver
from pages.login.login_page import LoginPage

import unittest

class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        path = "/Users/aravindanathdm/Documents/PythonPOM_FW/driver/chromedriver"
        driver =  webdriver.Chrome(executable_path=path)
        driver.fullscreen_window()
        driver.implicitly_wait(30)
        baseURL ="https://www.amazon.in"
        driver.get(baseURL)


        lp = LoginPage(driver)
        lp.login("iphone","stiku6033@gmail.com","amazonapps")



# py.test -s -v /Users/aravindanathdm/Documents/Simple_Pom_py_fw/tests/login/login_tests.py --html=../screenshots/demo.html


if __name__ == "__main__":
    unittest.main(verbosity=2)

