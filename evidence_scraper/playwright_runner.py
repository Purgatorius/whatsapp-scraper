from playwright.sync_api import sync_playwright


class PlaywrightRunner:
    def __init__(self, headless=True):
        self.headless = headless
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=self.headless)
        self.context = self.browser.new_contex()
        self.page = self.contex.new_page()

    def close(self):
        self.browser.close()
        self.playwright.stop()

    def click_element(self, selector: str, scroll: bool = False, timeout: int = 5000):
    """
    Clicks an element specified by the given selector.
    
    Optionally scrolls the element into view before clicking and waits for the element to be ready.

    Args:
        selector (str): The Playwright-compatible selector (CSS, text=, xpath=, etc.).
        scroll (bool): Whether to scroll the element into view before clicking. Default is False.
        timeout (int): Maximum time to wait for the element in milliseconds. Default is 5000ms.
    """
    locator = self.page.locator(selector)
    locator.wait_for(timeout=timeout)

    if scroll:
        locator.scroll_into_view_if_needed(timeout=timeout)

    locator.click(timeout=timeout)



