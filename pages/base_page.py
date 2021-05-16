import typing

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what, root: typing.Optional[WebElement] = None):
        """Tries to find element on the page or inside other element"""
        if root is None:
            root = self.browser
        try:
            root.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
