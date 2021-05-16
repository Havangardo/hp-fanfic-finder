from contextlib import contextmanager

from selenium import webdriver

from env import WEBDRIVER_URL

DESIRED_CAPS = {
    "browserName": "chrome",
}


@contextmanager
def remote_browser():
    web_browser = webdriver.Remote(WEBDRIVER_URL, desired_capabilities=DESIRED_CAPS)
    try:
        yield web_browser
    finally:
        web_browser.quit()
