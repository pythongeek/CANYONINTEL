try:
    from curl_cffi import requests
    CURL_CFFI_AVAILABLE = True
except ImportError:
    import requests
    CURL_CFFI_AVAILABLE = False

from bs4 import BeautifulSoup
import re
import time
import random
import json
from datetime import datetime
from typing import Dict, Any, List, Optional
from fake_useragent import UserAgent
from app.config import settings

class CodeCanyonScraper:
    """Advanced Scraper with Robust Cloudflare Defense."""
    
    # Randomizable TLS Fingerprints
    BROWSERS = ["chrome110", "chrome107", "chrome104", "edge99", "safari15_5"]

    def __init__(self, delay: float = 2.0):
        self.delay = delay
        self.ua = UserAgent()
        
        # 1. Randomize TLS Fingerprint (if available)
        if CURL_CFFI_AVAILABLE:
            self.impersonate_browser = random.choice(self.BROWSERS)
            self.session = requests.Session(impersonate=self.impersonate_browser)
        else:
            self.session = requests.Session()
        
        self.warmed_up = False

    def _get_headers(self) -> Dict[str, str]:
        # 4. Enhanced Header Rotation
        return {
            'User-Agent': self.ua.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': random.choice(['en-US,en;q=0.9', 'en-GB,en;q=0.8', 'en-CA,en;q=0.8']),
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': 'max-age=0',
            'Referer': 'https://www.google.com/',
        }

    def _warmup_cookies(self):
        """3. Cookie Warmup: Visit homepage to establish session."""
        if self.warmed_up:
            return

        try:
            # Short timeout, just to get cookies
            self.session.get("https://codecanyon.net", headers=self._get_headers(), timeout=5)
            # Short sleep to mimic human processing
            time.sleep(random.uniform(1.0, 2.5)) 
            self.warmed_up = True
        except Exception:
            # Don't fail the whole job if warmup fails, just proceed
            pass

    def _get_proxy_url(self, target_url: str) -> str:
        if settings.SCRAPER_API_KEY:
            # Vercel Optimization: standard proxy mode, US geo to ensure English/USD
            # Cache Buster: Force fresh content from ScraperAPI
            api_key = settings.SCRAPER_API_KEY.strip()
            ts = int(time.time())
            # Premium=true for higher success rate on Vercel
            return f"http://api.scraperapi.com?api_key={api_key}&url={target_url}&country_code=us&t={ts}&premium=true"
        return target_url

    def _is_blocked(self, response) -> bool:
        """5. Monitor for Detection Patterns"""
        text_lower = response.text.lower() if response.text else ""
        indicators = [
            response.status_code == 403,
            response.status_code == 429,
            'captcha' in text_lower,
            'cloudflare' in text_lower,
            'ray id' in text_lower and 'error' in text_lower
        ]
        return any(indicators)

    def _parse_product(self, soup: BeautifulSoup, url: str) -> Dict[str, Any]:
        """Extracts data from the product page using JSON-LD and CSS fallback."""
        data = {
            "url": url,
            "title": "Unknown Product",
            "price": 0.0,
            "currency": "USD",
            "rating": 0.0,
            "sales_count": 0,
            "author": "Unknown",
            "category": "Unknown",
            "image_url": "",
            "last_updated": datetime.now().isoformat(),
            "description": "",
            "technologies": []
        }

        
        # Strategy 1: JSON-LD (Most Reliable for Non-JS)
        json_data = self._extract_from_jsonld(soup)
        if json_data:
            data.update(json_data)

        # Strategy 2: CSS Selectors (Fallback/Supplement)
        if data["title"] == "Unknown Product":
            title = soup.select_one('h1')
            if title: data["title"] = title.get_text(strip=True)

        if data["price"] == 0.0:
            data["price"] = self.extract_price(soup)
            
        if data["sales_count"] == 0:
            data["sales_count"] = self.extract_sales(soup)
            
        if data["author"] == "Unknown":
            auth = soup.select_one('.item-header__author a, .media__body h2 a')
            if auth: data["author"] = auth.get_text(strip=True)

        if not data["image_url"]:
            img = soup.select_one('.item-preview img, .item-thumbnail__image img')
            if img: data["image_url"] = img.get('src') or img.get('data-src')

        # Cleanup/Formatting
        if data["technologies"]:
            data["technologies"] = list(set(data["technologies"])) # dedupe

        return data

    def _extract_from_jsonld(self, soup: BeautifulSoup) -> Dict[str, Any]:
        """Parses Schema.org JSON-LD to extract core metadata."""
        extracted = {}
        debug = []
        scripts = soup.find_all('script', type='application/ld+json')
        debug.append(f"Found {len(scripts)} scripts")
        
        for i, script in enumerate(scripts):
            try:
                content = script.string
                if not content: 
                    debug.append(f"Script {i}: empty")
                    continue
                schema = json.loads(content)
                
                # We expect a "Product" or "SoftwareApplication" type
                s_type = schema.get('@type')
                debug.append(f"Script {i}: Type={s_type}")
                
                if s_type == 'Product':
                    if 'name' in schema: extracted['title'] = schema['name']
                    if 'image' in schema: extracted['image_url'] = schema['image']
                    if 'description' in schema: extracted['description'] = schema['description'][:500] + "..."
                    
                    # Price
                    if 'offers' in schema:
                        offers = schema['offers']
                        debug.append(f"Offers type: {type(offers)}")
                        if isinstance(offers, dict):
                            extracted['price'] = float(offers.get('price', 0))
                            extracted['currency'] = offers.get('priceCurrency', 'USD')
                            debug.append(f"Extracted price: {extracted['price']}")
                    
                    # Brand/Author
                    if 'brand' in schema and isinstance(schema['brand'], dict):
                        extracted['author'] = schema['brand'].get('name')
                    
                    # Rating
                    if 'aggregateRating' in schema:
                        extracted['rating'] = float(schema['aggregateRating'].get('ratingValue', 0))

                elif s_type == 'SoftwareApplication':
                    if 'name' in schema and 'title' not in extracted: extracted['title'] = schema['name']
                    if 'author' in schema and isinstance(schema['author'], dict):
                        extracted['author'] = schema['author'].get('name')
                    if 'aggregateRating' in schema:
                        extracted['rating'] = float(schema['aggregateRating'].get('ratingValue', 0))
                        
            except Exception as e:
                debug.append(f"Script {i} Error: {str(e)}")
                continue
        
        extracted['_debug'] = "; ".join(debug)
        return extracted

    def scrape(self, url: str) -> Dict[str, Any]:
        """Main scraping method."""
        
        # 3. Cookie Warmup (only if not using ScraperAPI)
        if not settings.SCRAPER_API_KEY:
            self._warmup_cookies()
            # 7. Exponential Backoff (Only needed for direct connection)
            backoff_delay = self.delay + random.uniform(0.5, 1.5)
            time.sleep(backoff_delay)
        
        try:
            url = url.strip()
            
            # Discovery Phase
            if self.is_search_url(url):
                discovered_url = self.discover_first_product(url)
                url = discovered_url
                # No sleep needed here if using ScraperAPI

            fetch_url = self._get_proxy_url(url)
            
            # 6. Vercel-Specific Optimization: 9s timeout
            # Use standard requests for ScraperAPI to avoid curl_cffi conflicts on Vercel
            import requests
            response = requests.get(
                fetch_url, 
                headers=self._get_headers() if not settings.SCRAPER_API_KEY else None, 
                timeout=9
            )
            
            if self._is_blocked(response):
                 soup = BeautifulSoup(response.text, 'lxml')
                 title = soup.title.string.strip() if soup.title else "No Title"
                 raise Exception(f"Access Denied ({response.status_code}). Block detected. Title: {title}")
            
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'lxml')
            
            return self._parse_product(soup, url)
            
        except Exception as e:
            msg = str(e)
            debug_info = ""
            try:
                if 'response' in locals() and response:
                    debug_info = f" HTML: {response.text[:1000]}"
            except: pass
            
            if "Timeout" in msg:
                msg = "Request Timed Out (Vercel limit). Try again or use a faster proxy."
            elif "403" in msg or "block" in msg.lower():
                msg = f"Cloudflare Block detected.{debug_info}"
            raise Exception(f"Scraper Error: {msg}")

    # ... (rest of the file)

    def is_search_url(self, url: str) -> bool:
        return any(k in url.lower() for k in ["/search", "/category/", "/all", "date=", "sort="])

    def discover_first_product(self, search_url: str) -> Optional[str]:
        try:
            # 6. Vercel-Specific Optimization: 9s timeout
            response = self.session.get(
                self._get_proxy_url(search_url), 
                headers=self._get_headers() if not settings.SCRAPER_API_KEY else None, 
                timeout=9
            )
            
            if self._is_blocked(response):
                raise Exception(f"Search Page Blocked ({response.status_code})")
            
            soup = BeautifulSoup(response.text, 'lxml')
            
            selectors = [
                'a.shared-item_cards-item_name_component__itemNameLink', 
                'a.shared-item_cards-list-image_card_component__itemLinkOverlay',
                '.item-list h3 a', 
                'a[href*="/item/"]'
            ]
            
            for selector in selectors:
                links = soup.select(selector)
                for link in links:
                    href = link.get('href', '')
                    if '/item/' in href:
                         if '?' in href: href = href.split('?')[0]
                         return f"https://codecanyon.net{href}" if href.startswith('/') else href
            debug_html = soup.prettify()[:2000] # Capture 2000 chars
            raise ValueError(f"Analysis failed: No product links found. HTML Dump: {debug_html}")
        except Exception as e:
             # Propagate specific error
            raise Exception(f"Discovery phase failed: {str(e)}")

    # Extraction Helpers (kept identical to previous version)
    def extract_id(self, url: str) -> Optional[str]:
        match = re.search(r'/item/[^/]+/(\d+)', url)
        return match.group(1) if match else None
        
    def extract_slug(self, url: str) -> str:
        match = re.search(r'/item/([^/]+)/', url)
        return match.group(1) if match else "unknown"

    def extract_title(self, soup: BeautifulSoup) -> str:
        selectors = ['h1.t-heading--xl', 'h1', '.item-header__title', '.shared-item_cards-item_name_component__itemNameLink']
        for s in selectors:
            elem = soup.select_one(s)
            if elem: return elem.get_text(strip=True)
        return "Unknown Product"

    def extract_category(self, soup: BeautifulSoup) -> str:
        breadcrumb = soup.select('.t-link--one-color')
        return breadcrumb[1].get_text(strip=True) if len(breadcrumb) >= 2 else "Software"

    def extract_subcategory(self, soup: BeautifulSoup) -> Optional[str]:
        breadcrumb = soup.select('.t-link--one-color')
        return breadcrumb[2].get_text(strip=True) if len(breadcrumb) >= 3 else None

    def extract_price(self, soup: BeautifulSoup) -> float:
        elem = soup.select_one('.js-item-purchase__price')
        if elem:
            match = re.search(r'\$(\d+(?:\.\d{2})?)', elem.get_text())
            return float(match.group(1)) if match else 0.0
        return 0.0

    def extract_sales(self, soup: BeautifulSoup) -> int:
        elem = soup.select_one('.item-header__sales-count')
        if elem:
            match = re.search(r'(\d+)', elem.get_text().replace(',', ''))
            return int(match.group(1)) if match else 0
        return 0

    def extract_rating(self, soup: BeautifulSoup) -> float:
        elem = soup.select_one('.user-rating__rating')
        if elem:
            match = re.search(r'(\d+(?:\.\d+)?)', elem.get_text())
            return float(match.group(1)) if match else 0.0
        return 0.0

    def extract_review_count(self, soup: BeautifulSoup) -> int:
        elem = soup.select_one('.user-rating__count')
        if elem:
            match = re.search(r'(\d+)', elem.get_text().replace(',', ''))
            return int(match.group(1)) if match else 0
        return 0

    def extract_author(self, soup: BeautifulSoup) -> Optional[str]:
        elem = soup.select_one('.item-header__author a')
        return elem.get_text(strip=True) if elem else None

    def extract_author_id(self, soup: BeautifulSoup) -> Optional[str]:
        elem = soup.select_one('.item-header__author a')
        return elem.get('href').split('/')[-1] if elem and elem.get('href') else None

    def extract_technologies(self, soup: BeautifulSoup) -> List[str]:
        tags = []
        for tag in soup.select('.meta-attributes__attr-name'):
            if any(k in tag.get_text().lower() for k in ['compatible with', 'software version']):
                val = tag.find_next_sibling('.meta-attributes__attr-value')
                if val: tags.extend([t.strip() for t in val.get_text().split(',')])
        return list(set(tags))

    def extract_features(self, soup: BeautifulSoup) -> List[str]:
        features = []
        desc = soup.select_one('.user-html')
        if desc:
            for li in desc.select('li'):
                text = li.get_text(strip=True)
                if 5 < len(text) < 100: features.append(text)
        return features[:15]

    def extract_description(self, soup: BeautifulSoup) -> Optional[str]:
        elem = soup.select_one('.user-html')
        return str(elem) if elem else None

    def extract_screenshots(self, soup: BeautifulSoup) -> List[str]:
        images = []
        main = soup.select_one('.item-preview img')
        if main and main.get('src'): images.append(main.get('src'))
        return images
