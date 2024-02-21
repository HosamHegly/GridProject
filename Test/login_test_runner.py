# test_runner.py

import unittest
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

from login_test import *# Import the test case
from infra.browser_wrapper import BrowserWrapper


def run_tests_for_browser(browser):
    loginTest.browser = browser

    test_suite = unittest.TestLoader().loadTestsFromTestCase(loginTest)

    unittest.TextTestRunner().run(test_suite)


if __name__ == "__main__":
    browser_wrapper = BrowserWrapper()
    browsers = browser_wrapper.get_browsers()
    is_parallel = browser_wrapper.config.get("parallel", False)

    if is_parallel:
        with ThreadPoolExecutor() as executor:
            executor.map(run_tests_for_browser, browsers)
    else:
        for browser in browsers:
            run_tests_for_browser(browser)
