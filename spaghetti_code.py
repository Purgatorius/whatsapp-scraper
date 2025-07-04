from playwright.sync_api import sync_playwright
import os
import time
import json

SCROLL_SIZE = 500


def get_messages(page):
    print('>>> Getting messages from all visible chats...')
    conversations = {}

    chat_list = page.locator('[aria-label="Chat list"] [role="listitem"]')
    total_chats = chat_list.count()

    for i in range(total_chats):
        try:
            print(f"[INFO] Otwieram czat {i+1}/{total_chats}")
            chat = chat_list.nth(i)
            chat.click()
            page.wait_for_timeout(3000)

            # Spróbuj wyciągnąć nazwę kontaktu (jeśli dostępna)
            try:
                contact_name = page.locator('header span[title]').first.inner_text()
            except:
                contact_name = f"contact_{i+1}"

            # Scrapowanie wiadomości
            messages = page.locator('span[dir="ltr"]')
            message_count = messages.count()
            print(f"[INFO] Znalazłem {message_count} wiadomości dla {contact_name}")

            msg_list = []
            for j in range(message_count):
                msg_text = messages.nth(j).inner_text()
                if msg_text.strip():
                    msg_list.append(msg_text)

            conversations[contact_name] = msg_list

            # Zapisz do pliku
            os.makedirs("data/conversations", exist_ok=True)
            with open(f"data/conversations/{contact_name}.json", "w", encoding='utf-8') as f:
                json.dump(msg_list, f, ensure_ascii=False, indent=2)

        except Exception as e:
            print(f"[WARN] Nie udało się przetworzyć czatu nr {i+1}: {e}")
            continue

    return conversations



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.google.com")

    try:
        page.locator("button:has-text('Zaakceptuj wszystko')").click(timeout=2000)
    except:
        try:
            page.locator("button:has-text('Accept all')").click(timeout=2000)
        except:
            print("Nie znaleziono przycisku zgody – kontynuuję.")

    search_box = page.locator('[name="q"]')
    search_box.fill("WhatsApp Web")
    search_box.press("Enter")

    page.wait_for_timeout(1000)

    page.goto("https://www.google.com")
    page.goto("https://www.whatsapp.com/?lang=pl_PL", timeout=60000)

    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    page.wait_for_selector("text=WhatsApp Web", timeout=5000)
    page.locator("text=WhatsApp Web").click()

    page.wait_for_selector("text=Continue", timeout=60000)
    page.locator("text=Continue").click()

    page.wait_for_selector('[aria-label="Chat list"] [role="listitem"]', timeout=60000)
    page.locator('[aria-label="Chat list"] [role="listitem"]').first.click()
    page.wait_for_timeout(3000)

    messages = page.locator('span[dir="ltr"]')
    count = messages.count()
    print(f"[INFO] Znalazłem {count} wiadomości.")

    for i in range(count - 1, 0, -1):
        msg = messages.nth(i)
        print(f"[INFO] Klikam wiadomość nr {i}")
        try:
            msg.scroll_into_view_if_needed()
            msg.click()
            time.sleep(1)
        except Exception as e:
            print(f"[WARN] Nie udało się kliknąć: {e}")

    try:
        ok_button = page.locator('button:has-text("OK")')
        if ok_button.is_visible():
            print("[INFO] Klikam przycisk OK...")
            ok_button.click()
            time.sleep(1)
    except Exception as e:
        print(f"[WARN] Nie udało się kliknąć OK: {e}")

    try:
        close_button = page.locator('[aria-label="Close"]')
        close_button.click()
    except Exception as e:
        print(f"[WARN] Nie udało się kliknąć Close: {e}")

    try:
        chatArrow_down = page.locator('[data-icon="ic-chevron-down-wide"]')
        chatArrow_down.click()
    except Exception as e:
        print(f"[WARN] Nie udało się kliknąć strzałki w dół: {e}")

    # wywołujemy scrapowanie wiadomości dla kontaktów
    get_messages(page)

    print(f"KONIEC - PROGRAM ZAKONCZYL DZIALANIE - WAITING FOR TIMEOUT 0:30 min")
    page.wait_for_timeout(30000)

    browser.close()

