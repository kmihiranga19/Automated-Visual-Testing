from unittest import TestCase

from applitools.selenium import Eyes
from selenium import webdriver

from automation.config.base import APPLI_TOOLS_API_KEY


class BaseTest:

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.initialize_eyes()
        self.driver.get("")

    def tearDown(self):
        self.driver.quit()

    def initialize_eyes(self):
        self.eyes = Eyes()
        self.eyes.api_key = APPLI_TOOLS_API_KEY
        return self.eyes
