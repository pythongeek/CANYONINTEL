import google.generativeai as genai
import os
import json
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class MarketAnalyzer:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            logger.warning("GEMINI_API_KEY not found. Analysis will be mocked.")
            self.model = None
        else:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-1.5-pro')

    async def analyze_product(self, product_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generates SWOT analysis and Profitability Score.
        """
        if not self.model:
            return self._mock_analysis()

        prompt = f"""
        Act as a Senior Market Analyst. Analyze this CodeCanyon product:
        
        Title: {product_data.get('title')}
        Price: ${product_data.get('price')}
        Sales: {product_data.get('sales')}
        Rating: {product_data.get('rating')}
        Description: {product_data.get('description')[:2000]}...

        Output strictly valid JSON with this structure:
        {{
            "swot": {{
                "strengths": ["list"],
                "weaknesses": ["list"],
                "opportunities": ["list"],
                "threats": ["list"]
            }},
            "profitability_score": 0-100 (integer),
            "market_saturation": 0-100 (integer),
            "verdict": "One sentence summary"
        }}
        """
        
        try:
            response = self.model.generate_content(prompt)
            # Parse JSON from response
            text = response.text.replace("```json", "").replace("```", "").strip()
            return json.loads(text)
        except Exception as e:
            logger.error(f"Analysis failed: {e}")
            return self._mock_analysis()

    def _mock_analysis(self):
        return {
            "swot": {
                "strengths": ["High potential", "Good design"],
                "weaknesses": ["Analysis Mocked (No API Key)"],
                "opportunities": ["Expand features"],
                "threats": ["Competitors"]
            },
            "profitability_score": 75,
            "market_saturation": 40,
            "verdict": "Promising product (Mock Analysis)"
        }
