import time
from telnetlib import EC

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.base_page import BasePage


class mainPage(BasePage):
    BASKETBALL_NAV = (By.XPATH, "//button[@class='main-header-module-desktop-tab '][./div[contains(text(),'כדורסל')]]")
    TENNIS_NAV = (By.XPATH, "//button[@class='main-header-module-desktop-tab '][./div[contains(text(),'טניס')]]")
    HOKEY_NAV = (By.XPATH, "//button[@class='main-header-module-desktop-tab '][./div[contains(text(),'הוקי')]]")
    BASEBALL_NAV = (By.XPATH, "//button[@class='main-header-module-desktop-tab '][./div[contains(text(),'בייסבול')]]")
    SEARCH_FIELD = (By.XPATH, "//input[@class='main-header-module-desktop-search-input']")
    RESULT_PAGE_TEAM=(By.XPATH,"//a//div[contains(text(),'ריאל')]")
    VIDEO_TITLES = (By.ID, 'video-title')
    BACKGROUND_BLOCKER = (By.XPATH, "//div[@class='background-blocker']")

    def __init__(self, driver):
        super().__init__(driver)
        self._driver.fullscreen_window()
        self.wait_for_element_in_page_by_xpath(
            "//button[@class='main-header-module-desktop-tab ']//div[contains(text(),'כדורסל')]")

        self.basketball_navigate_button = self._driver.find_element(*self.BASKETBALL_NAV)
        self.tennis_navigate_button = self._driver.find_element(*self.TENNIS_NAV)
        self.hokey_navigate_button = self._driver.find_element(*self.HOKEY_NAV)
        self.search_field = self._driver.find_element(*self.SEARCH_FIELD)

    def navigate_to_basketball(self):
        self.basketball_navigate_button.send_keys(Keys.SPACE)

    def navigate_to_tennis(self):
        self.wait_for_element_in_page_by_xpath(self.TENNIS_NAV[1])

        self.tennis_navigate_button.send_keys(Keys.SPACE)

    def navigate_to_hokey(self):
        self.wait_for_element_in_page_by_xpath(self.HOKEY_NAV[1])

        self.hokey_navigate_button.send_keys(Keys.SPACE)
    def click_search_field(self):
        self.search_field.click()

    def choose_team_from_search_field(self,team):
        self.click_search_field()
        self
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(self.BACKGROUND_BLOCKER)).click()

        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,f"//a[./div[contains(text(),'{team}')]]"))).click()

    def init_teams_in_result_page(self,team):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH,f"//a//div[contains(text(),'{team}')]")))
        self.team= self._driver.find_elements(By.XPATH,f"//a//div[contains(text(),'{team}')]")


    def get_teams(self,team):
        self.init_teams_in_result_page(team)
        return len(self.team)>0
