from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from traceback import print_stack
import utilities.custom_logger as cl
import logging
import time
import os
# Reusable methods

class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    # Constructor

    def __init__(self,driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()

    def getTitle(self):
        return self.driver.title


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

    def getElementList(self, locator, locatorType="id"):
        """
        Get list of elements
        """
        locatorType = locatorType.lower()
        byType = self.getByType(locatorType)
        elements = self.driver.find_elements(byType, locator)
        if len(elements) > 0:
            self.log.info("Element list FOUND with locator: " + locator +
                          " and locatorType: " + locatorType)
        else:
            self.log.info("Element list NOT FOUND with locator: " + locator +
                          " and locatorType: " + locatorType)
        return elements


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

    def elementClick(self, locator="", locatorType="id", element=None):
        """
        Click on an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator="", locatorType="id", element=None):
        """
        Send keys to an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def clearField(self, locator="", locatorType="id"):
        """
        Clear an element field
        """
        element = self.getElement(locator, locatorType)
        element.clear()
        self.log.info("Clear field with locator: " + locator +
                      " locatorType: " + locatorType)

    def getText(self, locator="", locatorType="id", element=None, info=""):
        """
        NEW METHOD
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def isElementPresent(self, locator="", locatorType="id", element=None):
        """
        Check if element is present -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            print("Element not found")
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed")
            else:
                self.log.info("Element not displayed")
            return isDisplayed
        except:
            print("Element not found")
            return False



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

    # def assertTitle(self,pgTile,locator,locatorType):
    #
    #     titles= self.getElement(locator,locatorType)
    #     result = titles.text
    #     self.assertEqual(pgTile, result, "Title mis match")

    def verifyTitle(self,titleTxt):
        """

        :param titleTxt:
        :return:
        """

        if titleTxt in self.getTitle():
            return  True
        else:
            return False

    def webScroll(self, direction="up"):
        """
        NEW METHOD
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -800);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 800);")

    def switchToFrame(self, id="", name="", index=None):
        """
        Switch to iframe using element locator inside iframe
        Parameters:
            1. Required:
                None
            2. Optional:
                1. id    - id of the iframe
                2. name  - name of the iframe
                3. index - index of the iframe
        Returns:
            None
        Exception:
            None
        """
        if id:
            self.driver.switch_to.frame(id)
        elif name:
            self.driver.switch_to.frame(name)
        else:
            self.driver.switch_to.frame(index)

    def switchToDefaultContent(self):
        """
        Switch to default content
        Parameters:
            None
        Returns:
            None
        Exception:
            None
        """
        self.driver.switch_to.default_content()

    def getElementAttributeValue(self, attribute, element=None, locator="", locatorType="id"):
        """
        Get value of the attribute of element
        Parameters:
            1. Required:
                1. attribute - attribute whose value to find
            2. Optional:
                1. element   - Element whose attribute need to find
                2. locator   - Locator of the element
                3. locatorType - Locator Type to find the element
        Returns:
            Value of the attribute
        Exception:
            None
        """
        if locator:
            element = self.getElement(locator=locator, locatorType=locatorType)
        value = element.get_attribute(attribute)
        return value

    def isEnabled(self, locator, locatorType="id", info=""):
        """
        Check if element is enabled
        Parameters:
            1. Required:
                1. locator - Locator of the element to check
            2. Optional:
                1. locatorType - Type of the locator(id(default), xpath, css, className, linkText)
                2. info - Information about the element, label/name of the element
        Returns:
            boolean
        Exception:
            None
        """
        element = self.getElement(locator, locatorType=locatorType)
        enabled = False
        try:
            attributeValue = self.getElementAttributeValue(element=element, attribute="disabled")
            if attributeValue is not None:
                enabled = element.is_enabled()
            else:
                value = self.getElementAttributeValue(element=element, attribute="class")
                self.log.info("Attribute value From Application Web UI --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is not enabled")
        except:
            self.log.error("Element :: '" + info + "' state could not be found")
        return enabled
