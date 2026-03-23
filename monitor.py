import os
from playwright.sync_api import sync_playwright
import time

def run_monitor():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://uniswap.org")
        
        print("🟢 Monitoring Uniswap...")
        while True:
            try:
                # Check for new pools or activity
                pools = page.query_selector_all(".pool-card")
                if pools:
                    print(f"🔥 Found {len(pools)} active pools")
                time.sleep(30)
            except:
                print("🔄 Still monitoring...")
                time.sleep(30)
        
        browser.close()

if __name__ == "__main__":
    run_monitor()
