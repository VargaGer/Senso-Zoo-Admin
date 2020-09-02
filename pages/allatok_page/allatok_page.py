import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from utilities.util import Util
from pages.login_page.login_page import LoginPage
from utilities.testStatus import TestStatus

class AllatokPage(BasePage):
    log = cl.customLogger(logging.DEBUG)
    util = Util()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.loginPage = LoginPage(self.driver)
        self.basePage = BasePage(self.driver)

    # Locators
    _addNewAnimal_button = "Új állat hozzáadása"

    ### Add new / modify animal page locators
    # Alapveto adatok
    _nev_field = "name"
    _latinNev_field = "latin-name"

    # Fejlec elemei
    _ujJellemzo_button = "new-attribute"
    _uresJellemzo_text = "//td[contains(text(), 'Nincs megadva jellemző')]"
    _jellemzoTorles_button = "//input[@title='Törlés']"

    # Információs panel
    _emlosok_checkBox = "food-mammals"
    _halak_checkBox = "food-fishes"
    _madarak_checkBox = "food-birds"
    _termeszetVedelmiStatus_dropDown = "endangered-status"

    # Rendszertani besorolás
    _orszag_field = "kingdom"
    _torzs_field = "phylum"
    _osztaly_field = "class"
    _rend_field = "order"
    _csalad_field = "family"
    _faj_field = "species"

    # Leírás iFrame
    _leiras_iFrameField = ""

    # Gyerek nezet
    _erdekesseg_field = "trivia"
    _tudtad_iFrameField = ""
    _figyeld_iFrameField = ""

    # Other
    _mentes_button = ".save-confirmed-item"
    _cancel_button = "cancel-edit"
    _confirmMentes_button = "//button[@data-bb-handler='confirm']"
    _confirmCancel_button = "//button[@data-bb-handler='cancel']"

    # Alerts
    _succesfullyAdded_alert = "//div[@class='alert alert-success']"


    # Actions
    def clickAddNewAnimalButton(self):
        self.elementClick(self._addNewAnimal_button, "link")

    def addNewAnimal(self, name, latinName):
        self.sendKeys(name, self._nev_field)
        self.sendKeys(latinName, self._latinNev_field)
        self.webScrollToElement(self._mentes_button, "css")
        self.elementClick(self._mentes_button, "css")
        self.elementClick(self._confirmMentes_button, "xpath")
        if self.isElementPresent(self._succesfullyAdded_alert, "xpath"):
            self.log.info("Animal with name: '" + name + "' succesfully added")
        else:
            self.log.info("Animal with name: '" + name + "' was NOT added succesfully added")

    def deleteAnimal(self, name):
        self.elementClick("//td[contains(text(),'{}')]//following::input[2]".format(name), "xpath")
        self.elementClick(self._confirmMentes_button, "xpath")

    def openAddNewAnimalMenu(self):
        self.loginPage.login(userName=self.loginPage.login_userName, password=self.loginPage.login_password)
        self.basePage.openAllatokMenu()
        self.clickAddNewAnimalButton()

    ### Jellemzok actions
    def pressJellemzokButton(self, clickNumber, secBetweenClicks=0):
        self.elementClick(self._ujJellemzo_button, "id", clickNumber=clickNumber, secBetweenClicks=secBetweenClicks)

    def isJellemzokClickable(self, status):
        isClickable = self.isElementEnabled(self._ujJellemzo_button, "id")
        self.log.debug("Locator: " + self._ujJellemzo_button + " IsClickable = " + str(isClickable))
        self.log.debug("condition: " + status)
        if str(isClickable) == status:
            self.log.info("Kattintás rendben van")
        else:
            self.log.error("Valami van a kattintással")

    def isJellemzokEmpty(self, status):
        """
        True ha üres, False ha nem üres
        :param status:
        :return:
        """
        jellemzokStatus = self.isElementPresent(self._uresJellemzo_text, "xpath")
        self.log.debug("Jellemzönél várt státusz (True = üres, False = nem üres): " + status)
        #jellemzokStatus = (jellemzokStatus & False)
        self.log.debug("Jellemzök aktuális statusza: " + str(jellemzokStatus))
        assert str(jellemzokStatus) == status

    #def deleteJellemzo(self, deleteNumber=1):


