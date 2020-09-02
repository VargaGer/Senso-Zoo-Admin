"""
@package base

Base Page class implementation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
    Class LoginPage(BasePage)
"""
from base.selenium_drivers import SeleniumDrivers
from traceback import print_stack
from utilities.util import Util


class BasePage(SeleniumDrivers):
    ### Locators ###
    # Homepage Logo
    _homeLogo_img = "//a[@id='logo-big']"

    # Menu buttons
    _profil_button = "Profil"
    _logout_button ="Kilépés"
    _allatok_button = "//a[@href='/allatkert-admin/animals']"
    _mozaikOldalak_button ="Mozaik oldalak"
    _cikkek_button = "Cikkek"
    _terkep_button = "Térkép"


    def __init__(self, driver):
        """
        Inits BasePage class

        Returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page Title

        Parameters:
            titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.getPageTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to verify " + titleToVerify + " title")
            print_stack()
            return False

    # Menu actions
    def openAllatokMenu(self):
        self.elementClick(self._allatok_button, "xpath")

    def goToHomepage(self):
        self.elementClick(self._homeLogo_img)

    def logout(self):
        self.elementClick(self._logout_button, "link")
        self.elementClick("//button[@data-bb-handler='confirm']", "xpath")

