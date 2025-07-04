from evidence_scraper.locators import WhatsAppLocators
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

    def go_to_WhatsAppWeb(self):
        self.page.goto(WhatsAppLocators.HOME_URL.value)

    def accept_cookie_popup(self):
        self.page.wait_for_selector(WhatsAppLocators.CONTINUE_BUTTON.value) 
        self.page.locator(WhatsAppLocators.CONTINUE_BUTTON.value).click()

    def select_chat(self):
        # TODO: implement logic
        pass

    def extract_messages(self):
        def extract_messages(self):
    print('[INFO] Scraping messages...')
    conversations = {}
    chat_list = self.page.locator(WhatsAppLocators.CHAT_LIST_ITEMS.value)
    total_chats = chat_list.count()

    for i in range(total_chats):
        try:
            print(f"[INFO] Opening chat {i+1}/{total_chats}")
            chat = chat_list.nth(i)
            chat.click()
            self.page.wait_for_timeout(3000)

            try:
                contact_name = self.page.locator(WhatsAppLocators.CHAT_HEADER_NAME.value).first.inner_text()
            except:
                contact_name = f"contact_{i+1}"

            messages = self.page.locator(WhatsAppLocator.MESSAGE_SPAN.value)
            message_count = messages.count()
            print(f"[INFO] I have found {message_count} messages for {contact_name}")

            msg_list = []
            for j in range(message_count):
                msg_text = messages.nth(j).inner_text()
                if msg_text.strip():
                    msg_list.append(msg_text)

            conversations[contact_name] = msg_list

            os.makedirs("data/conversations", exist_ok=True)
            with open(f"data/conversations/{contact_name}.json", "w", encoding='utf-8') as f:
                json.dump(msg_list, f, ensure_ascii=False, indent=2)

        except Exception as e:
            print(f"[WARN] I could not process this chat {i+1}: {e}")
            continue

    return conversations

