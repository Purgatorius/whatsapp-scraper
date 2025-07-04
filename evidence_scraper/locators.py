from enum import Enum

class GoogleLocators(Enum):
    GOOGLE_URL = "https://www.whatsapp.com/?lang=pl_PL"
    ACCEPT_POLISH = "button:has-text('Zaakceptuj wszystko')"
    ACCEPT_ENGLISH = "button:has-text('Accept all')"
    SEARCH_BOX = '[name="q"]'

class WhatsAppLocators(Enum):
    HOME_URL = "https://www.whatsapp.com/?lang=pl_PL"
    WEB_LINK = "text=WhatsApp Web"
    CONTINUE_BUTTON = "text=Continue"
    CHAT_LIST_ITEM = '[aria-label="Chat list"] [role="listitem"]'
    CHAT_HEADER_NAME = 'header span[title]'
    MESSAGE_SPAN = 'span[dir="ltr"]'
    OK_BUTTON = 'button:has-text("OK")'
    CLOSE_BUTTON = '[aria-label="Close"]'
    CHAT_ARROW_DOWN = '[data-icon="ic-chevron-down-wide"]'
    MESSAGE_SPAN = 'span[dir="ltr"]'

