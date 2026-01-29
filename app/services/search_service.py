import os
import requests
import logging

logger = logging.getLogger(__name__)

class GoogleSearchService:
    def __init__(self):
        self.api_key = os.getenv('GOOGLE_SEARCH_API_KEY')
        self.engine_id = os.getenv('GOOGLE_SEARCH_ENGINE_ID')
    
    def search(self, query: str, num_results: int = 10):
        if not self.api_key or not self.engine_id:
            logger.warning("Google Search API Key or Engine ID not set.")
            return []
            
        url = 'https://www.googleapis.com/customsearch/v1'
        params = {
            'key': self.api_key,
            'cx': self.engine_id,
            'q': query,
            'num': num_results
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get('items', [])
        except Exception as e:
            logger.error(f"Google Search failed: {e}")
            return []
