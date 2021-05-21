import typing

from selenium.webdriver.remote.webelement import WebElement

from browser import remote_browser
from pages.login_page import LoginPage
from pages.popular_page import PopularPage
from pages.locators import PopularPageLocators
from telegram_bot import send_message_to_telegram

LOGIN_LINK = "https://ficbook.net/login"
POPULAR_LINK = "https://ficbook.net/fanfiction/books/harri_potter/popular"

KNOWN_LINKS_FILE_PATH = "./fanfic_links.txt"


def main():
    try:
        known_links = load_known_links()
        with remote_browser() as browser:
            process_popular_fanfics(browser, known_links)
    except Exception as e:
        send_message_to_telegram(str(e))


def load_known_links():
    """Load known links from the file"""
    known_links = set()
    with open(KNOWN_LINKS_FILE_PATH, "r") as f:
        for link in f.readlines():
            link = link.strip()
            known_links.add(link)
    return known_links


def save_known_link_to_file(url):
    """Save a link to the fanfic to file"""
    with open(KNOWN_LINKS_FILE_PATH, "a") as f:
        f.write(url + "\n")


def process_popular_fanfics(browser, known_links):
    login_page = LoginPage(browser, LOGIN_LINK)
    login_page.open()
    login_page.login_user()

    popular_page = PopularPage(browser, POPULAR_LINK)
    popular_page.open()
    tr_elements: typing.List[WebElement] = browser.find_elements(*PopularPageLocators.FANFIC)
    for tr_element in tr_elements:
        if popular_page.is_fanfic_suitable(tr_element):
            link = tr_element.find_element(*PopularPageLocators.LINK).get_attribute("href")
            if link in known_links:
                continue

            number = tr_element.find_element(*PopularPageLocators.RATING_NUMBER).text
            name = tr_element.find_element(*PopularPageLocators.NAME).text
            likes = tr_element.find_element(*PopularPageLocators.LIKES).text
            elements = tr_element.find_elements(*PopularPageLocators.PAIRINGS_CHARACTERS)
            characters = []
            for elem in elements:
                characters.append(elem.get_attribute("textContent"))
            characters_text = ", ".join(characters)
            description = tr_element.find_element(*PopularPageLocators.DESCRIPTION).get_attribute("textContent")
            description = description.strip()
            fanfic = f"*{number}. {name}*\n\n{link}\nLikes: {likes}\nPairing: {characters_text}\n\n{description}"
            save_known_link_to_file(link)
            send_message_to_telegram(fanfic)


if __name__ == "__main__":
    main()
