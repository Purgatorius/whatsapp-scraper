from playwright.sync_api import sync_playwright


class PlaywrightRunner:
    def __init__(self, headless=True):
        self.headless = headless
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=self.headless)
        self.contex = self.browser.new_contex()
        self.page = self.contex.new_page()

    def close(self):
        self.browser.close()
        self.playwright.stop()


