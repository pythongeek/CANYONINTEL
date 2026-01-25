from curl_cffi import requests
from bs4 import BeautifulSoup
import os
import time

# User's ScraperAPI Key
API_KEY = "a1f77bf4cacd457f155d803eb1c4142a"
# Using a known popular item to test standard selectors
TARGET_URL = "https://codecanyon.net/item/optech-it-service-and-business-consulting-laravel-script/57011612"

def debug_item_scrape():
    print(f"Fetching Item {TARGET_URL}...")
    proxy_url = f"http://api.scraperapi.com?api_key={API_KEY}&url={TARGET_URL}&country_code=us"
    
    try:
        t0 = time.time()
        response = requests.get(proxy_url, timeout=30)
        print(f"Status: {response.status_code} (took {time.time()-t0:.2f}s)")
        
        if response.status_code != 200:
            print(f"Error Body: {response.text[:500]}")
            return

        with open("debug_item.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("Saved to debug_item.html")
        
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Test specific failed selectors
        print("\n--- Testing Specific Selectors ---")
        
        # 1. Price
        price_sel = '.js-item-purchase__price'
        price_elem = soup.select_one(price_sel)
        print(f"Price ('{price_sel}'): {price_elem.get_text(strip=True) if price_elem else 'NOT FOUND'}")
        
        # Test JSON-LD Extraction
        print("\n--- Testing JSON-LD Extraction ---")
        import json
        scripts = soup.find_all('script', type='application/ld+json')
        print(f"Found {len(scripts)} JSON-LD scripts")
        
        for i, script in enumerate(scripts):
            try:
                content = script.string
                if not content: continue
                schema = json.loads(content)
                s_type = schema.get('@type')
                print(f"Script {i} Type: {s_type}")
                
                if s_type == 'Product':
                    print(f"  Name: {schema.get('name')}")
                    print(f"  Brand: {schema.get('brand')}")
                    if 'offers' in schema:
                         print(f"  Price: {schema['offers'].get('price')}")
                         
            except Exception as e:
                print(f"  Error parsing script {i}: {e}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    debug_item_scrape()
