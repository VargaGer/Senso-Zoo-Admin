from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from utilities.util import Util
import utilities.custom_logger as cl
import logging
import time
import os


class SeleniumDrivers():
    log = cl.customLogger(logging.DEBUG)


    def __init__(self, driver):
        self.driver = driver
        self.util = Util()

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current page:
        """
        filename = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenShotDir = "../screenshots/"
        # Mindig a jelenlegi mappából számol
        relativeFileName = screenShotDir + filename
        # Get the directory name of the current file
        currentDir = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDir, relativeFileName)
        destinationDir = os.path.join(currentDir, screenShotDir)

        try:
            # Check if destinationDir is exist
            if not os.path.exists(destinationDir):
                # Ha nincs ilyen mappa, létrehozza
                os.makedirs(destinationDir)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot saved to directory: " + destinationFile)
        except:
            self.log.error("### Screenshot error Occured")
            print_stack()

    def getElementList(self, locator, locatorType="xpath"):
        """
        Get list of elements
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element


    def getByType(self, locatorType="xpath"):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: " + locator + " and locator type: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator + " and locator type: " + locatorType)
        return element

    def elementClick(self, locator="", locatorType="id", clickNumber=1, secBetweenClicks=0, element=None):
        """
        Click on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # locator is not empty
                element = self.getElement(locator, locatorType)
            for i in range(clickNumber):
                element.click()
                self.util.sleep(secBetweenClicks)
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()
            self.screenShot(locator + " not found")

    def sendKeys(self, data, locator="", locatorType="id", element=None):
        """
        Send keys to an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # locator is not empty
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()

    def sendKeysWithEnter(self, data, locator="", locatorType="xpath", element=None):
        """
        Send keys to an element then press enter at the end
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            element.send_keys(Keys.ENTER)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()

    def getText(self, locator="", locatorType="xpath", element=None, info=""):
        """
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator: # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
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


    def clearKeys(self, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            element.clear()
        except:
            self.log.info("Cannot clear data on the element: " + locator + " LocatorType: " + locatorType)


    def isElementPresent(self, locator="", locatorType="xpath", element=None):
        """
        Check if element is present
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

    def isElementDisplayed(self, locator="", locatorType="xpath", element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            else:
                self.log.info("Element not displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            return isDisplayed
        except:
            print("Element not found")
            return False


    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element presence is Found with locator: " + locator + "with type: " + byType)
                return True
            else:
                self.log.info("Element not found with locator: " + locator + "with type: " + byType)
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="xpath",
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element


    def isElementEnabled(self, locator, locatorType):
        """
        Megnézi egy elem-ben van-e 'disabled' parameter
        :param locator:
        :param locatorType:
        :return: Boolean
        """
        element = self.getElement(locator, locatorType)
        elementStatus = element.is_enabled()
        if elementStatus == True:
            self.log.info("Element with locator: " + locator + " is enabled.")
        elif elementStatus == False:
            self.log.info("Element with locator: " + locator + " is NOT enabled.")
        return elementStatus


    def getPageTitle(self):
        return self.driver.title


    def webScroll(self, value, direction="down"):
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, {}});".format(value))

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, {});".format(value))

    def mouseHover(self, locator, locatorType="xpath", sec=0):
        actions = ActionChains(self.driver)
        elementToHover = self.getElement(locator)
        actions.move_to_element(elementToHover).perform()

    def selectFromDropDownWithKeys(self, element, selection):
        self.elementClick(element)
        dropDown = self.getElement(element)
        try:
            for i in range(0, selection):
                dropDown.send_keys(Keys.ARROW_DOWN)
                self.log.info("Moving down on dropdown by: " + str(i + 1))
            dropDown.send_keys(Keys.ENTER)
        except:
            self.screenShot("DropDownSelectionFailed")
            self.log.error("Moving down on dropdown list failed")


    def webScrollToElement(self, locator, locatoryType="xpath"):
        element = self.getElement(locator, locatoryType)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)


    def getAttributeValue(self, attribute, locator, locatorType="xpath"):
        element = self.getElement(locator, locatorType)
        elementAttributeValue = element.get_attribute(attribute)
        self.log.info("Locator: '" + locator + "' attribute value = " + elementAttributeValue)
        return elementAttributeValue


    def checkFieldMaxLenght(self, maxLenght, charNumber, locator, locatorType="xpath"):
        """
        Létrehoz egy 'maxlenght' hosszú random karaktersorozatot + 1 karaktert (a plusz karatkernek nem szabadna belekerülnie az input mezőbe)
        összehasonlítja a maxHossz + 1 karakterek hosszát a beírt karakterek hosszával
        maxLenght: Field max hossza, bussinnes logic alapján
        charNumber: Beütni kívánt karakterek száma
        """
        inputChars = self.util.getAlphaNumeric(charNumber, "mix")
        self.sendKeys(inputChars, locator, locatorType)
        self.log.info("Random chars: " + inputChars)
        # With attribute "value" it gives back the characters in the input field
        wroteText = self.getAttributeValue("value", locator, locatorType)
        self.log.info("Wrote chars: " + wroteText)
        assert maxLenght == len(wroteText)


