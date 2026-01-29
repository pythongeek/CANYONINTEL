from google import genai
import os
import json
import logging
from typing import Dict, Any

from app.config import settings

logger = logging.getLogger(__name__)

class MarketAnalyzer:
    def __init__(self):
        api_key = settings.GEMINI_API_KEY
        self.client = genai.Client(api_key=api_key)

    async def analyze_product(self, product_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generates SWOT analysis, Profitability Score, and initial market assessment.
        """
        if not self.client:
            raise ValueError("GEMINI_API_KEY not configured.")

        prompt = f"""
        Act as a Senior Market Analyst & Product Manager. Perform a deep competitive analysis for this CodeCanyon product:
        
        Title: {product_data.get('title')}
        Category: {product_data.get('category')}
        Price: ${product_data.get('price')}
        Sales: {product_data.get('total_sales', 0)}
        Rating: {product_data.get('rating', 0)}
        Features: {', '.join(product_data.get('features', []))}
        Description: {product_data.get('description', '')[:2000]}
        
        TASK:
        1. Conduct a SWOT analysis.
        2. Calculate a Profitability Score (0-100) based on sales velocity and price.
        3. Assess Market Saturation (0-100).
        4. Provide a score breakdown and trend assessment.

        Output strictly valid JSON with this structure:
        {{
            "swot": {{
                "strengths": ["list"],
                "weaknesses": ["list"],
                "opportunities": ["list"],
                "threats": ["list"]
            }},
            "profitability_score": 0-100,
            "market_saturation": 0-100,
            "score_breakdown": {{
                "demand": 0-100,
                "competition": 0-100,
                "pricing": 0-100
            }},
            "trend_analysis": {{
                "momentum": "growing/stable/declining",
                "verdict": "One sentence summary"
            }}
        }}
        """
        
        try:
            response = self.client.models.generate_content(
                model="gemini-2.0-flash-exp", # Using 2.0 for better reasoning if available
                contents=prompt
            )
            
            text_content = response.text
            if "```json" in text_content:
                text_content = text_content.split("```json")[1].split("```")[0].strip()
            elif "```" in text_content:
                text_content = text_content.split("```")[1].split("```")[0].strip()
            
            return json.loads(text_content.strip())
        except Exception as e:
            logger.error(f"Analysis failed: {e}")
            raise

    async def generate_blueprint(self, product_data: Dict[str, Any], comments: list) -> Dict[str, Any]:
        """
        Generates a 4-week Development Blueprint, identifying 3 major feature gaps.
        """
        if not self.client:
            raise ValueError("GEMINI_API_KEY not configured.")

        prompt = f"""
        Act as a Senior Product Manager. Create a "Gap Analysis" and execution roadmap to disrupt this product.
        
        Target Product: {product_data.get('title')}
        Existing Features: {', '.join(product_data.get('features', []))}
        User Pain Points (from comments):
        {chr(10).join(comments[:15])}

        TASK:
        1. Identify 3 major Feature Gaps that competitors are missing.
        2. Create a tactical 4-week Development Roadmap.
        3. Recommend a modern, high-velocity Tech Stack for 2026.
        
        Output strictly valid JSON with this structure:
        {{
            "feature_gaps": ["gap 1", "gap 2", "gap 3"],
            "roadmap": [
                {{"week": 1, "goal": "Foundation", "milestones": ["...", "..."]}},
                {{"week": 2, "goal": "Core USP", "milestones": ["...", "..."]}},
                {{"week": 3, "goal": "Scaling", "milestones": ["...", "..."]}},
                {{"week": 4, "goal": "Launch", "milestones": ["...", "..."]}}
            ],
            "tech_stack": {{
                "frontend": "e.g. Next.js 15, Tailwind v4",
                "backend": "e.g. FastAPI, Supabase",
                "ai": "e.g. GenAI SDK, LangChain"
            }},
            "competitive_edge": "Why this specific plan wins in one sentence."
        }}
        """
        
        try:
            response = self.client.models.generate_content(
                model="gemini-2.0-flash-exp",
                contents=prompt
            )
            
            text_content = response.text
            if "```json" in text_content:
                text_content = text_content.split("```json")[1].split("```")[0].strip()
            elif "```" in text_content:
                text_content = text_content.split("```")[1].split("```")[0].strip()
            
            return json.loads(text_content.strip())
        except Exception as e:
            logger.error(f"Blueprint generation failed: {e}")
            raise
