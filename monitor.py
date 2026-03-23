from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def setup_driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return driver

def main():
    print("🚀 Telegram Group Monitor Starting...")
    driver = setup_driver()
    
    # LOGIN (ONE TIME ONLY)
    driver.get("https://web.telegram.org")
    print("🔐 STEP 1: Scan QR code with Telegram app...")
    input("Login done? Press ENTER...")
    
    print("📱 STEP 2: Click your target group...")
    input("On target group? Press ENTER...")
    
    print("✅ 24/7 MONITORING ACTIVE!")
    
    while True:
        try:
            messages = driver.find_elements(By.CSS_SELECTOR, "[data-message-id]")
            
            for msg in messages[-5:]:
                msg_text = msg.text.lower()
                
                # TRIGGER WORDS (edit these later)
                if any(word in msg_text for word in ["entry", "buy", "sell", "signal"]):
                    buttons = msg.find_elements(By.TAG_NAME, "button")
                    for btn in buttons:
                        if any(x in btn.text.lower() for x in ["click", "join", "tap"]):
                            print(f"🖱️ CLICKED: {btn.text}")
                            btn.click()
                            time.sleep(3)
                            
                            # COPY RESULT
                            result = driver.find_elements(By.CSS_SELECTOR, "[data-message-id]")[-1].text
                            print(f"📋 COPIED: {result}")
                            
                            # SEND TO WEBSITE
                            submit_to_website(driver, result)
                            break
            
            time.sleep(3)
        except:
            time.sleep(5)

def submit_to_website(driver, text):
    print(f"🌐 SENDING: {text[:50]}...")
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://your-website.com")  # CHANGE THIS
    
    try:
        driver.find_element(By.ID, "signal").send_keys(text)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        print("✅ SUBMITTED!")
    except:
        print("❌ Form needs HTML customization")
    
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

if __name__ == "__main__":
    main()
