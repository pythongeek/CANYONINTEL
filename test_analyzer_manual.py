import os
import asyncio
from google import genai
from dotenv import load_dotenv

load_dotenv()

async def test_analyzer():
    api_key = os.getenv("GEMINI_API_KEY")
    print(f"API Key present: {bool(api_key)}")
    if not api_key:
        print("Error: No API Key")
        return

    try:
        client = genai.Client(api_key=api_key)
        print("Client initialized")
        
        prompt = "Hello, can you generate a simple JSON object? {'test': 'ok'}"
        
        print("Sending request...")
        # Testing the sync call as used in analyzer.py
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        
        print(f"Response type: {type(response)}")
        print(f"Response text: {response.text}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_analyzer())
