import logging
from typing import Dict, Any
from datetime import datetime

logger = logging.getLogger(__name__)

class ProfitabilityAnalyzer:
    """
    Deterministic scoring engine for CodeCanyon products.
    Calculates a Profitability Score (0-100) based on multiple market factors.
    """

    def calculate_score(self, product_data: Dict[str, Any]) -> float:
        """
        Calculates the weighted score based on:
        - Sales Volume (30%)
        - Price Point (20%) - High enough to be profitable, low enough to be accessible
        - Ratings (20%)
        - Sales Velocity (15%) - (Sales / Days since launch) - approximation
        - Market Fit/Recency (15%)
        """
        try:
            sales = float(product_data.get('total_sales', 0))
            price = float(product_data.get('price', 0))
            rating = float(product_data.get('rating', 0))
            # Placeholder for launch date logic if available, else use a default
            # For now, let's use what we have in the models/scraper output
            
            # 1. Sales Score (30%) - Logarithmic scaling for sales
            # 0 sales = 0, 100 sales = 50, 1000 sales = 80, 10k+ sales = 100
            import math
            sales_score = min(100, (math.log10(sales + 1) / 4) * 100) if sales > 0 else 0
            
            # 2. Price Score (20%) - Target price range $29 - $99 for high volume
            # < $10 = penalty, > $200 = penalty for mass market
            if 29 <= price <= 99:
                price_score = 100
            elif price < 29:
                price_score = (price / 29) * 100
            else:
                price_score = max(0, 100 - ((price - 99) / 2)) # Drops off after $200

            # 3. Rating Score (20%) - Linear 0-5 mapping
            rating_score = (rating / 5) * 100
            
            # 4. Market Fit / Velocity (30%) - Combination of reviews and sales
            # Items with high sales AND high ratings are proven
            velocity_score = min(100, (sales_score + rating_score) / 2)

            # Final Weighted Score
            final_score = (
                (sales_score * 0.30) +
                (price_score * 0.20) +
                (rating_score * 0.20) +
                (velocity_score * 0.30)
            )
            
            logger.info(f"Calculated Score for {product_data.get('title', 'Product')}: {final_score}")
            return round(final_score, 2)

        except Exception as e:
            logger.error(f"Error calculating profitability score: {e}")
            return 0.0

    def get_market_verdict(self, score: float) -> str:
        if score >= 80:
            return "High Potential: Strong market validation and pricing power."
        elif score >= 60:
            return "Solid Opportunity: Good sales but may face high competition."
        elif score >= 40:
            return "Moderate: Requires unique value proposition to succeed."
        else:
            return "Saturated/Low Demand: Not recommended for direct entry."
