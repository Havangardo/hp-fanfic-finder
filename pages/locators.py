from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.XPATH, '//div[@class="col-sm-11"]/input[@name="login"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#login-password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.btn-block")


class PopularPageLocators:
    FANFIC = (By.XPATH, "//*[@id='main']//tr")
    # selectors inside <tr>:
    CATEGORY_JEN = (By.CSS_SELECTOR, ".direction-before-gen")
    CATEGORY_GET = (By.CSS_SELECTOR, ".direction-before-het")
    FINISHED_MARKER = (By.CSS_SELECTOR, ".badge-status-finished")
    READ_MARKER = (By.CSS_SELECTOR, ".read-decoration-text")

    MORE_ACTIONS = (By.CSS_SELECTOR, ".ic_nav-dots")
    TO_COLLECTION = (By.CSS_SELECTOR, ".dropdown-menu-element")
    CLOSE_ICON = (By.CSS_SELECTOR, ".ic_cancel-circle")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "button.close")

    RATING_NUMBER = (By.CSS_SELECTOR, ".rating-nr") #.text
    NAME = (By.XPATH, ".//h3/a") #.text
    LINK = (By.XPATH, ".//h3/a") #.get_attribute("href")
    LIKES = (By.XPATH, ".//span[contains(@class,'badge-like')]//span[@class='badge-text']") #.text
    PAIRINGS_CHARACTERS = (By.XPATH, ".//dl//a[contains(@class,'pairing-link')]") #.text
    DESCRIPTION = (By.XPATH, ".//div[contains(@class,'fanfic-description-text')]") #.text
