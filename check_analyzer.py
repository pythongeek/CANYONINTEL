import asyncio
import os
from dotenv import load_dotenv

# Mock data to simulate scraping result
mock_product_data = {
    "title": "Ultimate eCommerce Solution",
    "category": "WordPress",
    "price": 59.00,
    "sales": 1500,
    "rating": 4.8,
    "description": "A complete solution for your online store with advanced features and responsive design."
}

async def test_analyzer():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    print(f"Checking API Key... {'Found' if api_key else 'Missing'}")
    
    try:
        from worker.analyzer import MarketAnalyzer
        print("Initializing MarketAnalyzer...")
        analyzer = MarketAnalyzer()
        
        print("Running analyze_product...")
        result = await analyzer.analyze_product(mock_product_data)
        
        print("\n--- Analysis Result ---")
        print(f"Profitability Score: {result.get('profitability_score', 'N/A')}")
        print(f"Verdict: {result.get('verdict', 'N/A')}")
        print(f"SWOT Keys: {list(result.get('swot', {}).keys())}")
        print("-----------------------")
        
    except Exception as e:
        print(f"Error during analysis: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_analyzer())
