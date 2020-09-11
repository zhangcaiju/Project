from selenium import webdriver
import time
import os
from selenium.webdriver import ActionChains


class Base():
    def setup(self):
        browser = os.getenv('browser')
        if browser == 'ie':
            self.driver = webdriver.Ie()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        pass
        # self.driver.quit()
