import logging
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

class PlaywrightScraper:
    def __init__(self, headless: bool = True):
        self.headless = headless

    async def scrape(self, url: str) -> dict:
        logger.info(f"Launching browser to scrape: {url}")
        
        async with async_playwright() as p:
            # 1. Launch Browser with random tweaks
            browser = await p.chromium.launch(
                headless=self.headless,
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--no-sandbox"
                ]
            )
            
            # 2. Context with Stealth
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                viewport={"width": 1920, "height": 1080},
                device_scale_factor=1,
            )
            
            page = await context.new_page()
            await stealth_async(page)
            
            # 3. Navigate with massive timeout (Render has no 10s limit)
            try:
                logger.info(f"Navigating to {url}")
                await page.goto(url, wait_until="domcontentloaded", timeout=60000)
                
                # 4. Handle "Soft Block" / Cloudflare
                # Check for "Access Denied" or Challenge
                title = await page.title()
                content = await page.content()
                
                if "Access Denied" in title or "Just a moment" in title:
                    logger.warning("Soft Block detected. Attempting bypass...")
                    # Naive wait - in real world, might need mouse moves or CAPTCHA solving service
                    await page.wait_for_timeout(5000)
                    
                # 5. Extract Content
                # We can perform clicks here if needed (e.g. "View Demo")
                
                # Dump HTML for BS4 parsing
                html = await page.content()
                
                # Use existing extraction logic (mimic scraping.py or import if possible)
                # For Phase 3 MVP, let's just extract title/price/author directly with locators 
                # or parse the HTML to ensure consistent result format.
                
                data = self._parse_with_bs4(html, url)
                return data

            except Exception as e:
                logger.error(f"Scrape failed: {e}")
                raise
            finally:
                await browser.close()

    def _parse_with_bs4(self, html: str, url: str) -> dict:
        soup = BeautifulSoup(html, 'lxml')
        # ... Reused logic from app/services/scraper.py ...
        # For simplicity, implementing core fields
        
        data = {
           "url": url,
           "title": "Unknown",
           "price": 0.0,
           "author": "Unknown",
           "rating": 0.0,
           "sales": 0,
           "description": ""
        }
        
        # Title
        t = soup.select_one('h1')
        if t: data["title"] = t.get_text(strip=True)
        
        # Price
        p = soup.select_one('.js-item-purchase__price')
        import re
        if p:
            match = re.search(r'\$(\d+(?:\.\d{2})?)', p.get_text())
            if match: data["price"] = float(match.group(1))

        # Author
        a = soup.select_one('.item-header__author a')
        if a: data["author"] = a.get_text(strip=True)
        
        # TODO: Full fields later
        return data
