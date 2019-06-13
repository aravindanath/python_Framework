from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from traceback import print_stack
import utilities.logger_Utility as cl
import logging
import time

# Reusable methods

class SeleniumDriver():

    log = cl.CustomLogger(logging.DEBUG)

    # Constructor

    def __init__(self,driver):
        self.driver = driver


    def getByType(self, loctorType):
            loctorType = loctorType.lower()
            if(loctorType == "id"):
                 return By.ID
            elif(loctorType == "xpath"):
                 return By.XPATH
            elif (loctorType == "name"):
                 return By.NAME
            elif(loctorType == "class"):
                 return By.CLASS_NAME
            elif(loctorType == "css"):
                 return By.CSS_SELECTOR
            elif(loctorType == "link"):
                 return By.LINK_TEXT
            elif(loctorType == "plink"):
                 return By.PARTIAL_LINK_TEXT
            else:
                self.log.info("Locator Type " + loctorType + "not correct / supported!")
                # print("Locator Type " + loctorType + "not correct / supported!")
            return False


    def getElement(self,locator,locatorType="id"):
        element = None

        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType,locator)
            self.log.info("Element found")
        except:
            self.log.exception("Element not found")
        return element




    def elementClick(self,locator,locatorType="id"):
        try:
            element = self.getElement(locator,locatorType)
            element.click()
            self.log.info(" Clicked  on element " + locator + "locator type: "+locatorType)
        except:
            self.log.exception(" Cannot click  on element " + locator + "locator type: " + locatorType)
            print_stack()


    def sendKeys(self,data ,locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info(" Send data  on element " + locator + "locator type: " + locatorType)
        except:
            self.log.exception(" Cannot send data  on element " + locator + "locator type: " + locatorType)
            print_stack()


    def sendKeysWithEnter(self,data ,locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data, Keys.ENTER)

            self.log.info(" Send data  on element " + locator + "locator type: " + locatorType)
        except:
            self.log.exception(" Cannot send data  on element " + locator + "locator type: " + locatorType)
            print_stack()



    def elementPresentCheck(self,locator,byType):

        try:
            elementlist = self.driver.find_elements(byType,locator)
            if(len(elementlist)>0):
                self.log.info("Element found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.exception("Element not found")
            return False


    def isElementPresent(self,locator,locatorType="id"):

        try:
            element = self.getElement(locator,locatorType)
            if element is not None:
                self.log.info("Element found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.exception("Element not found")
            return False


    def waitForElement(self,locator,locatorType="id",timeout=10,pollFreq=0.5):
        element = None

        try:

            byType = self.getByType(locatorType)
            self.log.info("waiting for maximum :: "+ str(timeout)+ ":: seconds for element to be clickable")

            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFreq,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])

            element = wait.until(EC.element_to_be_clickable((byType, locator)))

            self.log.info("Element appered on the web page ")
        except:
            self.log.exception("Element not appeared on the web page")
            print_stack()
        return element



    def take_Screenshot(self, driver):
        """

        :param driver:
        :return:
        """
        # fileName = str(round(time.time() * 1000)) + ".png"
        fileName = "snapShot.png"
        dir = "../screenshots/"
        driver.save_screenshot(dir + fileName)



    def mouseHover(self,locator,locatorType="id"):
        """

        :param locator:
        :param locatorType:
        :return:
        """
        try:
            element = self.getElement(locator, locatorType)
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
            self.log.info(" Mouse hover on element " + locator + "locator type: " + locatorType)
        except:
            print(" Cannot Mouse hover  on element " + locator + "locator type: " + locatorType)
            print_stack()

    def scrollToElement(self,locator,locatorType="id"):
        """

        :param locator:
        :param locatorType:
        :return:
        """
        try:
            element = self.getElement(locator,locatorType)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            self.log.info(" Scroll to element " + locator + "locator type: " + locatorType)
        except:
            print(" Cannot scroll to element " + locator + "locator type: " + locatorType)
            print_stack()

    def assertTitle(self,pgTile,locator,locatorType):

        titles= self.getElement(locator,locatorType)
        result = titles.text
        self.assertEqual(pgTile, result, "Title mis match")