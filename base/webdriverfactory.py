"""
It creates a webdriver instance based on browser configuration

example:
    wdf = webDriverFactory(browser)
    wdf.getWebdriverInstance
"""
from selenium import webdriver
import os

class WebDriverFactory():

    def __init__(self, browser):
        """
        inits WebDriverFactory class

        returns:
            None
        """
        self.browser = browser
        """
        Set chrome driver env. based on OS
        """
        chromeDriverLocation = "C:\\Users\\Ger\\PycharmProjects\\Webdrivers\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromeDriverLocation

    def getWebdriverInstance(self):
        """
        Get webdriver instance based on the browser configuration
        Returns:
            WebDriver instance
        """
        baseURL = "http://sandbox.sensomedia.hu/allatkert-admin/login"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        else:
            self.browser == "chrome"
            chromeDriverLocation = "C:\\Users\\Ger\\PycharmProjects\\Webdrivers\\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = chromeDriverLocation
            self.driver = webdriver.Chrome(chromeDriverLocation)
        # Setting implicit wait
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get(baseURL)
        return self.driver


