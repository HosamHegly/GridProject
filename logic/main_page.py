import time
from telnetlib import EC

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from infra.base_page import BasePage


class mainPage(BasePage):
    BASKETBALL_NAV = (By.XPATH, "//button[@class='main-header-module-desktop-tab '][./div[contains(text(),'כדורסל')]]")
    TENNIS_NAV = (By.XPATH, "//button[@class='main-header-module-desktop-tab '][./div[contains(text(),'טניס')]]")
    HOKEY_NAV = (By.XPATH, "//button[@class='main-header-module-desktop-tab '][./div[contains(text(),'הוקי')]]")
    BASEBALL_NAV = (By.XPATH, "//button[@class='main-header-module-desktop-tab '][./div[contains(text(),'בייסבול')]]")




    VIDEO_TITLES = (By.ID, 'video-title')



    def __init__(self, driver):
        super().__init__(driver)
        self._driver.fullscreen_window()
        self.wait_for_element_in_page_by_xpath("//button[@class='main-header-module-desktop-tab ']//div[contains(text(),'כדורסל')]")

        self.basketball_navigate_button = self._driver.find_element(*self.BASKETBALL_NAV)
        self.tennis_navigate_button = self._driver.find_element(*self.TENNIS_NAV)
        self.hokey_navigate_button = self._driver.find_element(*self.HOKEY_NAV)



    def navigate_to_basketball(self):

        self.basketball_navigate_button.send_keys(Keys.SPACE)
    def navigate_to_tennis(self):
        self.wait_for_element_in_page_by_xpath(self.TENNIS_NAV[1])

        self.tennis_navigate_button.send_keys(Keys.SPACE)
    def navigate_to_hokey(self):
        self.wait_for_element_in_page_by_xpath(self.HOKEY_NAV[1])

        self.hokey_navigate_button.send_keys(Keys.SPACE)












