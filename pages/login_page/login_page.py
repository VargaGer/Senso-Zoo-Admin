import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from utilities.util import Util
from utilities.testStatus import TestStatus

class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)
    util = Util()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Login Datas
    login_userName = "test"
    login_password = "test"

    # Locators
    ### Login ###
    _userName_field = "user-name"
    _password_field = "password"
    _login_button = "login-user"

    ### Forget password ###


    # Actions
    def enterUserName(self, email):
        self.sendKeys(email, self._userName_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, "id")


    # Main Functions
    def login(self, userName="", password=""):
        self.enterUserName(self.login_userName)
        self.enterPassword(self.login_password)
        self.clickLoginButton()

    def verifySuccesfulLogin(self, mainPageTitle):
        self.verifyPageTitle(mainPageTitle)

