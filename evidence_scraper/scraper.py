from evidence_scraper.locators import Locators
from evidence_scraper.playwright_runner import PlaywrightRunner

class WhatsAppScraper:
    def __init__(self, headless=True):
        self.runner = PlaywrightRunner(headless=headless)
        self.page = self.runner.page

    def run(self):
        self.go_to_WhatsAppWeb()
        self.accept_coockie_popup()
        self.select_chat()
        self.extract_messages()
        self.runner.close()

    def go_to_WhatsAppWeb()
    def accept_cookie_popupi()
    def select_chat()
    def extract_messages()
