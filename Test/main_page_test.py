import concurrent.futures.thread
import time

import selenium
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import unittest
import json

from infra.browser_wrapper import BrowserWrapper
from logic.main_page import mainPage


class mainPageTest(unittest.TestCase):

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        self.driver = self.browser_wrapper.get_driver(browser=self.__class__.browser)
        self.main_page=mainPage(self.driver)



    def test_navigate_to_basketball(self):
        self.main_page.navigate_to_basketball()
        url = self.main_page.get_current_url()
        self.assertEqual(url, "https://www.365scores.com/he/basketball")

    def test_navigate_to_tennis(self):
        self.main_page.navigate_to_tennis()
        url = self.main_page.get_current_url()
        self.assertEqual(url, "https://www.365scores.com/he/tennis")

    def test_navigate_to_hokey(self):
        self.main_page.navigate_to_hokey()
        url = self.main_page.get_current_url()
        self.assertEqual(url, "https://www.365scores.com/he/hockey")

    def test_search_field_result_madrid(self):
        self.main_page.choose_team_from_search_field('ריאל')
        self.assertTrue(self.main_page.get_teams('ריאל'))

    def test_search_field_result_israel(self):
        self.main_page.choose_team_from_search_field('ישראל')
        self.assertTrue(self.main_page.get_teams('ישראל'))




    def tearDown(self):
        self.driver.quit()
