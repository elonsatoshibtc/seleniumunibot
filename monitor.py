from playwright.sync_api import sync_playwright
import time

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(
        viewport={'width': 1920, 'height': 1080},
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    )
    page = context.new_page()
    
    print("🚀 Playwright Telegram Monitor Starting...")
    page.goto("https://web.telegram.org")
    
    print("🔐 LOGIN: Scan QR code with Telegram app...")
    print("📱 Navigate to target group...")
    input("On target group? Press ENTER...")
    
    print("✅ 24/7 MONITORING ACTIVE!")
    
    while True:
        try:
            # Scroll to load messages
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(2)
            
            # Get recent messages
            messages = page.query_selector_all("[data-message-id]")
            
            for msg in messages[-5:]:
                msg_text = msg.inner_text().lower()
                
                if any(word in msg_text for word in ["entry", "buy", "sell", "signal"]):
                    buttons = msg.query_selector_all("button")
                    for btn in buttons:
                        btn_text = btn.inner_text().lower()
                        if any(x in btn_text for x in ["click", "join", "tap"]):
                            print(f"🖱️ CLICKED: {btn_text}")
                            btn.click()
                            time.sleep(3)
                            
                            # Get result
                            new_messages = page.query_selector_all("[data-message-id]")
                            result = new_messages[-1].inner_text()
                            print(f"📋 COPIED: {result[:100]}...")
                            
                            # Website submit later
                            print("🌐 READY FOR WEBSITE!")
                            break
            
            time.sleep(5)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)
    
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
