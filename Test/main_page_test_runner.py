# test_runner.py

import unittest
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

from main_page_test import *# Import the test case
from infra.browser_wrapper import BrowserWrapper


def run_tests_for_browser(browser):
    mainPageTest.browser = browser

    test_suite = unittest.TestLoader().loadTestsFromTestCase(mainPageTest)
    print(test_suite, browser)

    unittest.TextTestRunner().run(test_suite)


if __name__ == "__main__":
    browser_wrapper = BrowserWrapper()
    is_parallel = browser_wrapper.is_parallel()
    is_grid = browser_wrapper.is_grid()
    if is_grid:
        browsers = browser_wrapper.get_browsers()

        if is_parallel:
            with ThreadPoolExecutor(max_workers=len(browsers)) as executor:
                executor.map(run_tests_for_browser, browsers)
        else:
            for browser in browsers:
                run_tests_for_browser(browser)

    else:
        browser = browser_wrapper.get_browser()
        run_tests_for_browser(browser)

