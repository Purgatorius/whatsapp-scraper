from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto("https://www.google.com")

    # Obsługa zgody (różne wersje językowe)
    try:
        page.locator("button:has-text('Zaakceptuj wszystko')").click(timeout=2000)
    except:
        try:
            page.locator("button:has-text('Accept all')").click(timeout=2000)
        except:
            print("Nie znaleziono przycisku zgody – kontynuuję.")

    # Wyszukiwanie
    search_box = page.locator('[name="q"]')
    search_box.fill("WhatsApp Web")
    search_box.press("Enter")


    page.wait_for_timeout(1000)  # poczekaj na wyniki

    page.goto("https://www.google.com")
     # 1. Otwórz stronę WhatsApp
    page.goto("https://www.whatsapp.com/?lang=pl_PL", timeout=60000)

    # 2. Scrolluj na dół strony
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    # 3. Kliknij „WhatsApp Web”
    page.wait_for_selector("text=WhatsApp Web", timeout=5000)
    page.locator("text=WhatsApp Web").click()

    # 4. zamknięcie wyskakującego info okna
    page.wait_for_selector("text=Continue", timeout=60000)
    page.locator("text=Continue").click()

    page.wait_for_selector('[aria-label="Chat list"] [role="listitem"]', timeout=60000)
    page.locator('[aria-label="Chat list"] [role="listitem"]').first.click()
    page.wait_for_timeout(3000);


    # Znajdź wszystkie widoczne wiadomości
    messages = page.locator('span[dir="ltr"]')

    count = messages.count()
    print(f"[INFO] Znalazłem {count} wiadomości.")

    for i in range(count - 1, 0, -1):
        msg = messages.nth(i)
        print(f"[INFO] Klikam wiadomość nr {i}")
        try:
            msg.scroll_into_view_if_needed()
            msg.click()  # Możesz też pominąć kliknięcie, jeśli niepotrzebne
            time.sleep(1)
        except Exception as e:
            print(f"[WARN] Nie udało się kliknąć: {e}")

    # overlay click ok
    try:
        ok_button = page.locator('button:has-text("OK")')
        if ok_button.is_visible():
             print("[INFO] Klikam przycisk OK...")
        ok_button.click()
        time.sleep(1)
    except Exception as e:
         print(f"[WARN] Nie udało się kliknąć OK: {e}")

    # close turn on notification message
    close_button = page.locator('[aria-label="Close"]')
    close_button.click()

    # click arrow to scroll down to the last chatted message
    chatArrow_down = page.locator('[data-icon="ic-chevron-down-wide"]')
    chatArrow_down.click()


    # WAIT BEFORE closing an app
    print(f"KONIEC - PROGRAM ZAKONCZYL DZIALANIE - WAITING FOR TIMEOUT 1:30 min")
    page.wait_for_timeout(90000);


    browser.close()

