import unittest
from selenium import webdriver


class FlixsterQATestCase(unittest.TestCase):
    def setUp(self):
        cls = self.__class__
        self.base_url = self.__class__.base_url
        if cls.browserType == "chrome":
            self.driver = webdriver.Chrome()
        elif cls.browserType == "firefox":
            self.driver = webdriver.Firefox()
        elif cls.browserType == "ie":
            self.driver = webdriver.Ie()
        elif cls.browserType == "none":
            self.driver = None
        else:
            raise RuntimeError("Browser type not supported")
        self.pages = self.loadPages()

    def tearDown(self):
        cls = self.__class__
        if cls.browserType == "none":
            pass
        else:
            self.driver.quit()

    def loadPages(self):
        pass
