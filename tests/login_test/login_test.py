from pages.login_page.login_page import LoginPage
from base.basepage import BasePage
from utilities.testStatus import TestStatus
from utilities.util import Util
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.util = Util()
        self.basePage = BasePage(self.driver)

    def test_validLogin(self):
        self.lp.login("test", "test")
        self.lp.verifyPageTitle("Főoldal | Budapesti Állatkert Admin")

    def test_invalidLogin_emptyEmail(self):
        self.lp.login(password="test")
        