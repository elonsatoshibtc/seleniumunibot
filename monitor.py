import os
from playwright.sync_api import sync_playwright
import time
import subprocess

# Install browsers first
os.system("playwright install --with-deps chromium")

def run_monitor():
    with sync_playwright() as p:
        # Headless=True for containers, args for stealth
        browser = p.chromium.launch(
            headless=True,
            args=['--no-sandbox', '--disable-setuid-sandbox']
        )
        page = browser.new_page()
        page.goto("https://uniswap.org")
        
        print("🟢 Monitoring Uniswap...")
        while True:
            try:
                # Check pools/activity
                pools = page.query_selector_all(".pool-card, [data-testid='pool-card']")
                if pools:
                    print(f"🔥 Found {len(pools)} pools")
                else:
                    print("🔄 Scanning...")
                time.sleep(30)
            except Exception as e:
                print(f"⚠️ Error: {e}")
                time.sleep(30)
        
        browser.close()

if __name__ == "__main__":
    run_monitor()
