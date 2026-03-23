import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Railway Chrome fix
chrome_options = Options()
chrome_options.binary_location = "/usr/bin/google-chrome-stable"
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--window-size=1920,1080")

def main():
    print("🚀 Starting FIXED Telegram Monitor...")
    
    # Use Railway's pre-installed Chrome
    driver = webdriver.Chrome(options=chrome_options)
    
    print("🔐 STEP 1: Go to https://web.telegram.org")
    driver.get("https://web.telegram.org")
    print("📱 MANUAL LOGIN: Scan QR code with Telegram app")
    input("Login done & on target group? Press ENTER...")
    
    print("✅ MONITORING 24/7...")
    
    while True:
        try:
            # Check recent messages
            messages = driver.find_elements(By.CSS_SELECTOR, "[data-message-id]")
            for msg in messages[-3:]:
                msg_text = msg.text.lower()
                
                # Triggers
                if any(word in msg_text for word in ["entry", "buy", "sell", "signal"]):
                    buttons = msg.find_elements(By.TAG_NAME, "button")
                    for btn in buttons:
                        btn_text = btn.text.lower()
                        if "click" in btn_text or "join" in btn_text:
                            print(f"🖱️ CLICKING: {btn.text}")
                            btn.click()
                            time.sleep(2)
                            
                            # Get result
                            result = messages[-1].text if messages else ""
                            print(f"📋 COPIED: {result}")
                            
                            # Website submit (customize later)
                            print(f"🌐 WOULD SUBMIT: {result[:50]}...")
                            break
            
            time.sleep(5)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
