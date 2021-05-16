from env import FICBOOK_LOGIN, FICBOOK_PASSWORD
from pages.locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def login_user(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_FIELD).send_keys(FICBOOK_LOGIN)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(FICBOOK_PASSWORD)
        self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
