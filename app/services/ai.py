from google import genai
import logging
import json
from typing import Dict, Any, List
from app.config import settings

logger = logging.getLogger(__name__)

class AIRecommendationService:
    """
    Service for generating market insights and development roadmaps using Gemini.
    """
    def __init__(self):
        self.api_key = settings.GEMINI_API_KEY
        if not self.api_key:
            logger.warning("GEMINI_API_KEY not found in settings.")
            self.client = None
        else:
            # Explicitly set v1beta for better model compatibility
            self.client = genai.Client(
                api_key=self.api_key,
                http_options={'api_version': 'v1beta'}
            )

    async def analyze_market_gaps(self, product_data: Dict[str, Any], comments: List[str]) -> Dict[str, Any]:
        """
        Identifies feature gaps and competitive advantages.
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
        
        last_error = None
        for model_name in ["gemini-1.5-flash", "gemini-1.5-flash-latest"]:
            try:
                # Using async interface for the SDK
                response = await self.client.aio.models.generate_content(
                    model=model_name,
                    contents=prompt
                )
                
                text_content = response.text
                return self._parse_json(text_content)
            except Exception as e:
                logger.warning(f"AI Gap Analysis failed for {model_name}: {e}")
                last_error = e
                continue
        
        logger.error(f"AI Gap Analysis failed for all models. Last error: {last_error}")
        raise last_error

    def _parse_json(self, text: str) -> Dict[str, Any]:
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0].strip()
        elif "```" in text:
            text = text.split("```")[1].split("```")[0].strip()
        return json.loads(text.strip())

    async def generate_step_content(self, product_data: Dict[str, Any], step: int) -> str:
        """
        Generates detailed content for a specific step in the Project Planner.
        """
        if not self.client:
            return f"Mock content for step {step}"

        step_prompts = {
            1: "Vision & Market Positioning",
            2: "Core MVP Features & USP",
            3: "Technical Architecture & Tech Stack",
            4: "Monetization & Pricing Strategy",
            5: "Go-to-Market & Launch Plan",
            6: "Scaling & Future Roadmap"
        }

        prompt = f"""
        Provide a detailed, professional recommendation for step {step}: {step_prompts.get(step)}
        For the product: {product_data.get('title')}
        
        Keep it concise, actionable, and focused on current 2026 market trends.
        Format as clean Markdown.
        """
        
        last_error = None
        # Expanded model list to find anything that works with the provided key
            "gemini-1.5-flash", 
            "gemini-1.5-flash-latest", 
            "gemini-1.5-pro", 
            "gemini-pro"
        ]
        
        for model_name in models_to_try:
            try:
                response = await self.client.aio.models.generate_content(
                    model=model_name,
                    contents=prompt
                )
                return response.text
            except Exception as e:
                logger.warning(f"AI Step Generation failed for {model_name}: {e}")
                last_error = e
                continue
                
        logger.error(f"AI Step Generation failed for all models. Last error: {last_error}")
        return f"Error generating insights for step {step} (Detail: {str(last_error)[:100]})."
