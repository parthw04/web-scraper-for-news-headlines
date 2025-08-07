# ================================== Task 3: Web Scraper ============================

import requests
from bs4 import BeautifulSoup

url = "https://www.indiatoday.in"

headers = {
     "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers)

soup = BeautifulSoup(response.text, 'html.parser')

headlines = []

for tag in soup.find_all(['h1', 'h2', 'title']):
     text = tag.get_text(strip=True)
     if text:
          headlines.append(text)


with open("headlines.txt", "w", encoding='utf-8') as file:
     for line in headlines:
          file.write(line + '\n')

print("Headlines saved to headlines.txt")