import os
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Install Chrome dependencies FIRST
print("🔧 Installing Chrome dependencies...")
subprocess.run(["apt-get", "update"], capture_output=True)
subprocess.run(["apt-get", "install", "-y", "wget", "gnupg"], capture_output=True)
subprocess.run(["wget", "-q", "-O", "-chrome.deb", "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"], capture_output=True)
subprocess.run(["dpkg", "-i", "-chrome.deb"], capture_output=True)
subprocess.run(["apt-get", "-f", "install"], capture_output=True)

# FIXED Chrome options for Railway
chrome_options = Options()
chrome_options.binary_location = "/usr/bin/google-chrome"
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-background-timer-throttling")
chrome_options.add_argument("--disable-backgrounding-occluded-windows")
chrome_options.add_argument("--disable-renderer-backgrounding")
chrome_options.add_argument("--window-size=1920,1080")

print("🚀 Starting Telegram Monitor...")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://web.telegram.org")

print("🔐 LOGIN: Scan QR code with Telegram app...")
print("📱 Navigate to your target group...")
input("Ready? Press ENTER...")

print("✅ 24/7 MONITORING LIVE!")
last_messages = []

while True:
    try:
        messages = driver.find_elements(By.CSS_SELECTOR, "[data-message-id]")
        recent = messages[-5:]
        
        for msg in recent:
            msg_text = msg.text.lower()
            
            if any(word in msg_text for word in ["entry", "buy", "sell", "signal"]):
                buttons = msg.find_elements(By.TAG_NAME, "button")
                for btn in buttons:
                    btn_text = btn.text.lower()
                    if any(x in btn_text for x in ["click", "join", "tap"]):
                        print(f"🖱️ CLICKED: {btn.text}")
                        btn.click()
                        time.sleep(3)
                        
                        # Copy result
                        result = messages[-1].text
                        print(f"📋 COPIED: {result}")
                        
                        # Website (customize later)
                        print(f"🌐 READY TO SUBMIT: {result[:50]}...")
                        break
        
        time.sleep(5)
    except Exception as e:
        print(f"Loop error: {e}")
        time.sleep(5)
