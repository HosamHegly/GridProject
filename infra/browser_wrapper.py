import json
from os.path import dirname, join

from selenium import webdriver


class BrowserWrapper:
    FILE_PATH = "config.json"

    def __init__(self):
        self.driver = None
        filename = self.get_filename("config.json")
        with open(filename, 'r') as file:
            self.config = json.load(file)
        self.parallel = self.config["parallel"]

    def get_driver(self, browser):
        browser_type = self.config["browser"]
        if self.config["grid"]:
            options = self.set_up_capabilities(browser)
            self.driver = webdriver.Remote(command_executor=self.config["hub"], options=options)
        else:
            if browser_type.lower() == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser_type.lower() == 'firefox':
                self.driver = webdriver.Firefox()
            elif browser_type.lower() == 'edge':
                self.driver = webdriver.Edge()
            url = self.config["url"]
            self.driver.get(url)
        return self.driver

    def close_browser(self):
        if self.driver:
            self.driver.quit()

    def set_up_capabilities(self, browser_type):
        if browser_type.lower() == 'chrome':
            options = webdriver.ChromeOptions()
        elif browser_type.lower() == 'firefox':
            options = webdriver.FirefoxOptions()
        elif browser_type.lower() == 'edge':
            options = webdriver.EdgeOptions()
        platform_name = self.config["platform"]
        options.add_argument(f'--platformName={platform_name}')
        return options
    def is_parallel(self):
        return self.parallel
    def close_browser(self):
        if self.driver:
            self.driver.quit()
    def get_browsers(self):
        return self.config["browser_types"]

    from os.path import dirname, join

    def get_filename(self,filename):
        here = dirname(__file__)
        output = join(here, filename)
        return output