import asyncio
import os
from playwright.async_api import async_playwright
import playwright_stealth
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)

# Try to find the correct stealth function
if hasattr(playwright_stealth, 'stealth_async'):
    stealth_async = playwright_stealth.stealth_async
elif hasattr(playwright_stealth, 'stealth'):
    stealth_async = playwright_stealth.stealth
else:
    logger.error("Could not find stealth function in playwright_stealth module")
    stealth_async = None

class PlaywrightScraper:
    def __init__(self, headless: bool = True):
        self.headless = headless

    async def scrape_with_stealth(self, url: str) -> dict:
        """Alias for scrape() to match Phase 3 terminology."""
        return await self.scrape(url)

    def _get_scraper_api_url(self, target_url: str) -> str:
        api_key = os.getenv('SCRAPER_API_KEY')
        if not api_key: return target_url
        return f"http://api.scraperapi.com?api_key={api_key}&url={target_url}&render=true&premium=true"

    async def scrape(self, url: str) -> dict:
        logger.info(f"Launching browser to scrape: {url}")
        async with async_playwright() as p:
            # Launch without proxy settings, using API wrapper instead
            browser = await p.chromium.launch(
                headless=self.headless,
                args=["--disable-blink-features=AutomationControlled", "--no-sandbox", "--ignore-certificate-errors"]
            )
            
            max_retries = 3
            for attempt in range(max_retries):
                context = None
                try:
                    context = await browser.new_context(
                        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                        viewport={"width": 1920, "height": 1080},
                        device_scale_factor=1,
                        ignore_https_errors=True
                    )
                    
                    page = await context.new_page()
                    if stealth_async and callable(stealth_async):
                        await stealth_async(page)
                    
                    logger.info(f"Navigating to {url} (Attempt {attempt + 1}/{max_retries})")
                    target_url = self._get_scraper_api_url(url)
                    logger.info(f"Target URL: {target_url}")
                    response = await page.goto(target_url, wait_until="domcontentloaded", timeout=120000) # Increased timeout for proxy
                    
                    if not response:
                        logger.error("No response received")
                        continue

                    status_code = response.status
                    logger.info(f"Response status: {status_code}")

                    if status_code == 404:
                        content = await page.content()
                        title = await page.title()
                        logger.error(f"404 Detected. Title: {title}")
                        logger.error(f"404 Content Start: {content[:500]}")
                        raise ValueError("Item not found (404)")
                    
                    if status_code == 403:
                        logger.warning("403 Forbidden detected. Retrying...")
                        await asyncio.sleep(5)
                        if context: await context.close()
                        continue

                    # Check for Soft Block via Title/Content
                    title = await page.title()
                    if "Access Denied" in title or "Just a moment" in title:
                        logger.warning("Soft Block detected (Title check). Retrying...")
                        await asyncio.sleep(5)
                        if context: await context.close()
                        continue

                    # Success path
                    html = await page.content()
                    
                    # Discovery Mode Detection
                    if "search" in url or "popular_item" in url or "category" in url:
                        logger.info("Discovery Mode Detected!")
                        urls = await self._extract_discovery_urls(page)
                        await context.close()
                        return urls

                    # Phase 5: Extract Comments
                    comments = await self._extract_comments(page)
                    
                    data = self._parse_with_bs4(html, url)
                    data['comments'] = comments
                    data['type'] = 'product'
                    
                    await context.close()
                    return data

                except ValueError as ve:
                    # Propagate specific errors like 404
                    if context: await context.close()
                    await browser.close()
                    raise ve
                    
                except Exception as e:
                    logger.error(f"Scrape attempt {attempt + 1} failed: {e}")
                    if context: await context.close()
                    if attempt == max_retries - 1:
                        await browser.close()
                        raise e
                    await asyncio.sleep(2)
            
            await browser.close()
            raise Exception("Max retries exceeded")

    def _parse_with_bs4(self, html: str, url: str) -> dict:
        soup = BeautifulSoup(html, 'lxml')
        
        data = {
           "url": url,
           "title": "Unknown Product",
           "price": 0.0,
           "author_name": "Unknown",
           "author_id": "Unknown",
           "category": "Software",
           "subcategory": None,
           "rating": 0.0,
           "review_count": 0,
           "total_sales": 0,
           "description": "",
           "features": [],
           "technologies": [],
           "screenshots": [],
           "slug": "unknown",
           "codecanyon_id": "unknown"
        }
        
        # ID and Slug from URL
        import re
        id_match = re.search(r'/item/[^/]+/(\d+)', url)
        if id_match: data["codecanyon_id"] = id_match.group(1)
        
        slug_match = re.search(r'/item/([^/]+)/', url)
        if slug_match: data["slug"] = slug_match.group(1)

        # Title
        t = soup.select_one('h1')
        if t: data["title"] = t.get_text(strip=True)
        
        # Price
        p = soup.select_one('.js-item-purchase__price')
        if p:
            match = re.search(r'\$(\d+(?:\.\d{2})?)', p.get_text())
            if match: data["price"] = float(match.group(1))

        # Author
        a = soup.select_one('.item-header__author a')
        if a:
            data["author_name"] = a.get_text(strip=True)
            data["author_id"] = a.get('href', '').split('/')[-1]

        # Category
        breadcrumb = soup.select('.t-link--one-color')
        if len(breadcrumb) >= 2: data["category"] = breadcrumb[1].get_text(strip=True)
        if len(breadcrumb) >= 3: data["subcategory"] = breadcrumb[2].get_text(strip=True)

        # Sales
        s = soup.select_one('.item-header__sales-count')
        if s:
            match = re.search(r'(\d+)', s.get_text().replace(',', ''))
            if match: data["total_sales"] = int(match.group(1))

        # Rating
        r_val = soup.select_one('.user-rating__rating')
        if r_val:
            match = re.search(r'(\d+(?:\.\d+)?)', r_val.get_text())
            if match: data["rating"] = float(match.group(1))
            
        r_count = soup.select_one('.user-rating__count')
        if r_count:
            match = re.search(r'(\d+)', r_count.get_text().replace(',', ''))
            if match: data["review_count"] = int(match.group(1))

        # Description
        desc_elem = soup.select_one('.user-html')
        if desc_elem:
            data["description"] = str(desc_elem)
            # Features
            for li in desc_elem.select('li'):
                txt = li.get_text(strip=True)
                if 5 < len(txt) < 100: data["features"].append(txt)
            data["features"] = data["features"][:15]

        # Tech
        for tag in soup.select('.meta-attributes__attr-name'):
            if any(k in tag.get_text().lower() for k in ['compatible with', 'software version']):
                val = tag.find_next_sibling('.meta-attributes__attr-value')
                if val: data["technologies"].extend([t.strip() for t in val.get_text().split(',')])
        data["technologies"] = list(set(data["technologies"]))

        # Screenshots
        main_img = soup.select_one('.item-preview img')
        if main_img and main_img.get('src'): data["screenshots"].append(main_img.get('src'))

        return data

    async def _extract_comments(self, page) -> list:
        """Extracts user comments, clicking the Comments tab if necessary."""
        logger.info("Extracting comments...")
        comments = []
        try:
            # Check if Comments tab is present and click it
            # Different themes might have different selectors, but 'Comments' text is common
            import re
            comments_tab = page.get_by_role("tab", name=re.compile("Comments", re.IGNORECASE))
            if await comments_tab.count() > 0:
                logger.info("Clicking Comments tab...")
                await comments_tab.click()
                await asyncio.sleep(2) # Wait for content to load
            else:
                # Try clicking by text if role tab fails
                try:
                    await page.click('text="Comments"', timeout=5000)
                    await asyncio.sleep(2)
                except:
                    logger.info("Comments tab already active or not found as clickable.")

            comment_elements = await page.query_selector_all('.comment__content, .comments-list .comment-text, .user-html')
            # Filter specifically for likely comment containers if .user-html is too broad
            # Usually comments are in certain wrappers
            
            for element in comment_elements[:20]: # Get top 20 comments
                text = await element.inner_text()
                if text and len(text.strip()) > 10:
                    comments.append(text.strip())
            
            logger.info(f"Extracted {len(comments)} comments.")
        except Exception as e:
            logger.warning(f"Failed to extract comments: {e}")
        
        return comments

    async def _extract_discovery_urls(self, page) -> list:
        """Extracts all product URLs from a search or category page."""
        logger.info("Extracting product URLs for discovery...")
        urls = set()
        try:
            # Common selectors for product links in search results
            # They usually contain '/item/' and are within a search results container
            selectors = [
                '.shared-item_cards-item_name_component__itemNameLink',
                '.shared-item_cards-list-image_card_component__itemLinkOverlay',
                'h3 a[href*="/item/"]',
                'a[href*="/item/"][class*="item_name"]',
                'a[href*="/item/"]'
            ]
            
            for selector in selectors:
                elements = await page.query_selector_all(selector)
                for element in elements:
                    href = await element.get_attribute('href')
                    if href:
                        if not href.startswith('http'):
                            href = f"https://codecanyon.net{href}"
                        
                        # Clean URL (remove tracking params)
                        if '?' in href:
                            href = href.split('?')[0]
                        
                        if '/item/' in href:
                            urls.add(href)
            
            logger.info(f"Discovery Mode: Found {len(urls)} products.")
        except Exception as e:
            logger.warning(f"Failed during discovery URL extraction: {e}")
        
        return list(urls)
