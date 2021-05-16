import typing

from selenium.webdriver.remote.webelement import WebElement

from browser import remote_browser
from pages.login_page import LoginPage
from pages.popular_page import PopularPage
from pages.locators import PopularPageLocators
from telegram_bot import send_message_to_telegram

LOGIN_LINK = "https://ficbook.net/login"
POPULAR_LINK = "https://ficbook.net/fanfiction/books/harri_potter/popular"


def main():
    try:
        with remote_browser() as browser:
            process_popular_fanfics(browser)
    except Exception as e:
        send_message_to_telegram(str(e))


def process_popular_fanfics(browser):
    login_page = LoginPage(browser, LOGIN_LINK)
    login_page.open()
    login_page.login_user()

    popular_page = PopularPage(browser, POPULAR_LINK)
    popular_page.open()
    tr_elements: typing.List[WebElement] = browser.find_elements(*PopularPageLocators.FANFIC)
    for tr_element in tr_elements:
        if popular_page.is_fanfic_suitable(tr_element):
            name = tr_element.find_element(*PopularPageLocators.NAME).text
            link = tr_element.find_element(*PopularPageLocators.LINK).get_attribute("href")
            likes = tr_element.find_element(*PopularPageLocators.LIKES).text
            elements = tr_element.find_elements(*PopularPageLocators.PAIRINGS_CHARACTERS)
            characters = []
            for elem in elements:
                characters.append(elem.get_attribute("textContent"))
            characters_text = ", ".join(characters)
            description = tr_element.find_element(*PopularPageLocators.DESCRIPTION).get_attribute("textContent")
            description = description.strip()
            fanfic = f"*{name}*\n\n{link}\nLikes: {likes}\nPairing: {characters_text}\n\n{description}"
            send_message_to_telegram(fanfic)


if __name__ == "__main__":
    main()
