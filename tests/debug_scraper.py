from curl_cffi import requests
from bs4 import BeautifulSoup
import os
import time

# User's ScraperAPI Key
API_KEY = "a1f77bf4cacd457f155d803eb1c4142a"
TARGET_URL = "https://codecanyon.net/search?date=this-year&sort=rating"

def debug_scrape_render_false():
    print(f"Fetching {TARGET_URL} with ScraperAPI...")
    # Matches app/services/scraper.py logic
    proxy_url = f"http://api.scraperapi.com?api_key={API_KEY}&url={TARGET_URL}&country_code=us"
    
    try:
        t0 = time.time()
        response = requests.get(proxy_url, timeout=30) # Longer timeout for debug
        elapsed = time.time() - t0
        print(f"Status Code: {response.status_code} (took {elapsed:.2f}s)")
        
        if response.status_code != 200:
            print(f"Response Body: {response.text[:500]}...")
            return

        with open("debug_response.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("Saved HTML to debug_response.html")
        
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Selectors from app/services/scraper.py
        selectors = [
            'a.shared-item_cards-item_name_component__itemNameLink', 
            'a.shared-item_cards-list-image_card_component__itemLinkOverlay',
            '.item-list h3 a', 
            'a[href*="/item/"]'
        ]
        
        found_any = False
        print("\n--- Testing Selectors ---")
        for selector in selectors:
            links = soup.select(selector)
            print(f"Selector '{selector}': Found {len(links)} links")
            if len(links) > 0:
                found_any = True
                print(f"  First: {links[0].get('href')}")
        
        if not found_any:
            print("\n❌ FAILED: No selectors matched any items.")
        else:
            print("\n✅ SUCCESS: Found items.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    debug_scrape_render_false()
