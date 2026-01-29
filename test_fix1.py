import asyncio
import os
import logging
from dotenv import load_dotenv
from worker.analyzer import MarketAnalyzer

# Load env vars
load_dotenv()

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("TestFix1")

async def test_analyzer():
    print("--- 1. Checking Environment ---")
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("FAILED: GEMINI_API_KEY is not set in .env")
        print("Please set the key and run again.")
        return
    print(f"SUCCESS: GEMINI_API_KEY found: {api_key[:5]}...")

    print("\n--- 2. Testing analyze_product() ---")
    mock_product = {
        "title": "CodeCanyon Scraper 2026",
        "category": "Scripts",
        "price": 49.00,
        "total_sales": 1500,
        "rating": 4.8,
        "features": ["Python", "Scrapy", "React Dashboard"],
        "description": "The ultimate scraping tool for CodeCanyon market analysis."
    }

    analyzer = MarketAnalyzer()
    
    try:
        analysis = await analyzer.analyze_product(mock_product)
        print("Analysis Result Received")
        
        # validation
        if "swot" not in analysis:
            print("FAILED: Response missing 'swot' key")
        elif "Mock" in str(analysis):
            print("FAILED: Response contains mock data (string 'Mock' found)")
        else:
            print("SUCCESS: analyze_product returned valid, non-mock data")
            print(f"Profitability Score: {analysis.get('profitability_score')}")

    except Exception as e:
        print(f"FAILED: analyze_product raised exception: {e}")
        return

    print("\n--- 3. Testing generate_blueprint() ---")
    comments = [
        "Great script but needs better documentation.",
        "Missing proxy support, please add.",
        "Can you add AI analysis features?"
    ]
    
    try:
        blueprint = await analyzer.generate_blueprint(mock_product, comments)
        print("Blueprint Result Received")
        
        if "roadmap" not in blueprint:
             print("FAILED: Response missing 'roadmap'")
        elif "Mock" in str(blueprint):
             print("FAILED: Response contains mock data")
        else:
             print("SUCCESS: generate_blueprint returned valid roadmap")
             print(f"First week goal: {blueprint['roadmap'][0].get('goal')}")

    except Exception as e:
        print(f"FAILED: generate_blueprint raised exception: {e}")

if __name__ == "__main__":
    asyncio.run(test_analyzer())
