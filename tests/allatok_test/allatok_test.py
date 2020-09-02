from pages.login_page.login_page import LoginPage
from pages.allatok_page.allatok_page import AllatokPage
from base.basepage import BasePage
from utilities.testStatus import TestStatus
from utilities.util import Util
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class AllatokTests(unittest.TestCase):

    animalName = "karfiol"

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.loginPage = LoginPage(self.driver)
        self.allatokPage = AllatokPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.util = Util()
        self.basePage = BasePage(self.driver)

    def test_addNewAnimal(self):
        self.allatokPage.openAddNewAnimalMenu()
        self.allatokPage.addNewAnimal(self.animalName, "AutomataLatinNev_1")
        self.basePage.logout()

    def test_deleteAnimal(self):
        self.allatokPage.openAddNewAnimalMenu()
        self.allatokPage.addNewAnimal("delAnimal", "AutomataLatinNev_1")
        self.allatokPage.deleteAnimal("delAnimal")
        self.basePage.logout()

    def test_nameMaxLenght(self):
        self.allatokPage.openAddNewAnimalMenu()
        self.basePage.checkFieldMaxLenght(50, 51, self.allatokPage._nev_field, "id")

    def test_LatinNameMaxLenght(self):
        self.allatokPage.openAddNewAnimalMenu()
        self.basePage.checkFieldMaxLenght(50, 51, self.allatokPage._latinNev_field, "id")

    def test_orszagMaxLenght(self):
        self.allatokPage.openAddNewAnimalMenu()
        self.basePage.checkFieldMaxLenght(35, 36, self.allatokPage._orszag_field, "id")

    def test_torzsMaxLenght(self):
        self.allatokPage.openAddNewAnimalMenu()
        self.basePage.checkFieldMaxLenght(35, 36, self.allatokPage._torzs_field, "id")

    def test_osztalyMaxLenght(self):
        self.allatokPage.openAddNewAnimalMenu()
        self.basePage.checkFieldMaxLenght(35, 36, self.allatokPage._osztaly_field, "id")

    def test_rendMaxLenght(self):
        self.allatokPage.openAddNewAnimalMenu()
        self.basePage.checkFieldMaxLenght(35, 36, self.allatokPage._rend_field, "id")

    def test_csaladMaxLenght(self):
        self.allatokPage.openAddNewAnimalMenu()
        self.basePage.checkFieldMaxLenght(35, 36, self.allatokPage._csalad_field, "id")

    def test_fajMaxLenght(self):
        self.allatokPage.openAddNewAnimalMenu()
        self.basePage.checkFieldMaxLenght(35, 36, self.allatokPage._faj_field, "id")

    def test_jellemzok(self):
        self.allatokPage.openAddNewAnimalMenu()
        self.allatokPage.isJellemzokClickable("True")
        self.allatokPage.isJellemzokEmpty("True")
        self.allatokPage.pressJellemzokButton(6)
        self.allatokPage.isJellemzokClickable("False")
        self.allatokPage.isJellemzokEmpty("False")