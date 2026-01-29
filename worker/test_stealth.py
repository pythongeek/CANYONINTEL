import asyncio
import logging
from playwright.async_api import async_playwright
import playwright_stealth
import os

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

async def test_stealth():
    logger.info("Starting stealth test...")
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
            logger.info("Stealth applied.")
        else:
            logger.warning("Stealth function not found, proceeding without it.")

        url = "https://bot.sannysoft.com"
        logger.info(f"Visiting {url}...")
        await page.goto(url, wait_until="networkidle")
        
        screenshot_path = "worker/stealth_results.png"
        await page.screenshot(path=screenshot_path, full_page=True)
        logger.info(f"Screenshot saved to {screenshot_path}")
        
        await browser.close()
        logger.info("Stealth test complete.")

if __name__ == "__main__":
    asyncio.run(test_stealth())
