import requests

payload = { 'api_key': 'a1f77bf4cacd457f155d803eb1c4142a', 'url': 'https://codecanyon.net/category/php-scripts?sort=sales', 'output_format': 'markdown' }
r = requests.get('https://api.scraperapi.com/', params=payload)
print(r.text)
