import os

FICBOOK_LOGIN = os.environ["FICBOOK_LOGIN"]
FICBOOK_PASSWORD = os.environ["FICBOOK_PASSWORD"]
TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_TOKEN"]
TELEGRAM_CHAT_ID = int(os.environ["TELEGRAM_CHAT_ID"])
WEBDRIVER_URL = os.getenv("WEBDRIVER_URL", "http://127.0.0.1:4444/wd/hub")
KNOWN_LINKS_FILE_PATH = os.getenv("KNOWN_LINKS_FILE_PATH", "./fanfic_links.txt")
