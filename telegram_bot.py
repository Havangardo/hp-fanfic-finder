import telebot

from env import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

BOT = telebot.TeleBot(TELEGRAM_BOT_TOKEN, parse_mode=None)

# We do not escape * intentionally to simplify fanfic name formatting
ESCAPED_CHARACTERS = "_[]()~`>#+-=|{}.!"


def escape_text(text):
    for c in ESCAPED_CHARACTERS:
        text = text.replace(c, fr"\{c}")
    return text


def send_message_to_telegram(text):
    BOT.send_message(TELEGRAM_CHAT_ID, escape_text(text), parse_mode="MarkdownV2")
