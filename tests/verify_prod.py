import urllib.request
import urllib.parse
import json

url = "https://canyon-intel.vercel.app/api/scrape"
import random
r = random.randint(1, 10000)
target = f"https://codecanyon.net/search?date=this-year&sort=rating&random={r}"
data = urllib.parse.urlencode({"url": target}).encode()
req = urllib.request.Request(url, data=data, method="POST")

print(f"POST {url}")
import re
import time

try:
    # 1. Start Job
    with urllib.request.urlopen(req) as r:
        initial_html = r.read().decode('utf-8')
        print(f"Initial Status: {r.status}")
        
        # Extract Job ID
        match = re.search(r'hx-get="/api/scrape/status/([a-f0-9\-]+)"', initial_html)
        if not match:
             print("Could not find Job ID in response")
             print(initial_html[:1000])
             exit(1)
             
        job_id = match.group(1)
        print(f"Job ID: {job_id}")
        
    # 2. Poll Status
    status_url = f"https://canyon-intel.vercel.app/api/scrape/status/{job_id}"
    
    for i in range(15): # Poll for 30s max
        print(f"Polling {i+1}/15...")
        time.sleep(2)
        with urllib.request.urlopen(status_url) as r:
            html = r.read().decode('utf-8')
            if "Phase: Pending" in html or "Fetching" in html or "Extracting" in html:
                continue
            elif "Scraping failed" in html:
                print("FAILED:")
                print(html)
                break
            else:
                print("SUCCESS/COMPLETE:")
                print(html[:5000])
                break

except Exception as e:
    print(f"Error: {e}")
