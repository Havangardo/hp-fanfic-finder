from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from pages.locators import PopularPageLocators


class PopularPage(BasePage):
    def is_fanfic_suitable(self, fanfic_element: WebElement):
        return (self.is_category_gen_or_get(fanfic_element) and self.is_fanfic_finished(fanfic_element) and
                self.is_fanfic_read(fanfic_element) and self.is_fanfic_in_collection(fanfic_element))

    def is_category_gen_or_get(self, fanfic_element: WebElement):
        return self.is_element_present(*PopularPageLocators.CATEGORY_JEN, root=fanfic_element) or \
               self.is_element_present(*PopularPageLocators.CATEGORY_GET, root=fanfic_element)

    def is_fanfic_finished(self, fanfic_element: WebElement):
        return self.is_element_present(*PopularPageLocators.FINISHED_MARKER, root=fanfic_element)

    def is_fanfic_read(self, fanfic_element: WebElement):
        return not self.is_element_present(*PopularPageLocators.READ_MARKER, root=fanfic_element)

    def is_fanfic_in_collection(self, fanfic_element: WebElement):
        fanfic_element.find_element(*PopularPageLocators.MORE_ACTIONS).click()
        fanfic_element.find_element(*PopularPageLocators.TO_COLLECTION).click()
        collected_fanfic = self.is_element_present(*PopularPageLocators.CLOSE_ICON)
        self.browser.find_element(*PopularPageLocators.CLOSE_BUTTON).click()
        return not collected_fanfic
