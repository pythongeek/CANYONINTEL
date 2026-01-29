import asyncio
import logging
from playwright.async_api import async_playwright
import playwright_stealth
from bs4 import BeautifulSoup
import re

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Find stealth function
if hasattr(playwright_stealth, 'stealth_async'):
    stealth_async = playwright_stealth.stealth_async
elif hasattr(playwright_stealth, 'stealth'):
    stealth_async = playwright_stealth.stealth
else:
    stealth_async = None

async def test_live():
    url = "https://codecanyon.net/item/chatbot-ai/50001234" # Example URL from prompt
    logger.info(f"Starting live scrape test on: {url}")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled", "--no-sandbox"]
        )
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080},
        )
        page = await context.new_page()
        
        if stealth_async:
            await stealth_async(page)
        
        logger.info(f"Navigating to {url}...")
        response = await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        
        if not response:
            print("FAILED: No response received")
            await browser.close()
            return

        status_code = response.status
        title = await page.title()
        
        print(f"\n--- SCRAPER VALIDATION ---")
        print(f"Status Code: {status_code}")
        print(f"Page Title: {title}")
        
        if status_code == 403 or "Access Denied" in title or "Just a moment" in title:
            print("RESULT: BLOCKED (403 or Cloudflare)")
            await browser.close()
            return

        # Phase 5: Extract Comments
        from worker.scraper import PlaywrightScraper
        scraper = PlaywrightScraper()
        comments = await scraper._extract_comments(page)
        print(f"Extracted {len(comments)} comments.")
        if comments:
            print(f"Sample Comment: {comments[0][:50]}...")

        html = await page.content()
        soup = BeautifulSoup(html, 'lxml')
        
        # Extraction
        extracted_title = "N/A"
        t_elem = soup.select_one('h1')
        if t_elem: extracted_title = t_elem.get_text(strip=True)
        
        # ... existing extraction logic simplified for test ...
        data = {"title": extracted_title, "features": ["Feature 1", "Feature 2"]}
        
        # Phase 5: Blueprint Generation
        print("Generating AI Blueprint...")
        from worker.analyzer import MarketAnalyzer
        analyzer = MarketAnalyzer()
        blueprint = await analyzer.generate_blueprint(data, comments)
        
        if "roadmap" in blueprint:
            print("AI Blueprint Generated Successfully!")
            print(f"Competitive Edge: {blueprint.get('competitive_edge')}")
        else:
            print(f"AI Blueprint Generation Failed: {blueprint.get('error') or blueprint.get('blueprint')}")

        print(f"\n--- PHASE 5 VALIDATION ---")
        
        price = "N/A"
        p_elem = soup.select_one('.js-item-purchase__price')
        if p_elem: price = p_elem.get_text(strip=True)
        
        sales = "N/A"
        s_elem = soup.select_one('.item-header__sales-count')
        if s_elem: sales = s_elem.get_text(strip=True)
        
        print(f"Extracted Title: {extracted_title}")
        print(f"Extracted Price: {price}")
        print(f"Extracted Sales: {sales}")
        
        # Review Check
        reviews_class = soup.select_one('.item-test-reviews')
        reviews_tab = soup.select_one('a[href*="reviews"]') # Common pattern for reviews tab
        
        if reviews_class:
            print("Reviews Check: Found .item-test-reviews class")
        elif reviews_tab:
            print("Reviews Check: Found reviews tab link")
        else:
            print("Reviews Check: Neither .item-test-reviews nor reviews tab found")
            
        if extracted_title == "Unknown Product" or not extracted_title or extracted_title == "N/A":
            print("RESULT: FAILED (Empty Title)")
        else:
            print("RESULT: SUCCESS")
            
        print(f"---------------------------\n")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_live())
