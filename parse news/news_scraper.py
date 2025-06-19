import requests
from bs4 import BeautifulSoup
import csv
from pathlib import Path
from datetime import datetime

def fetch_bbc_ukraine_news_csv(output_file="data/news.csv", max_articles=20):
    url = "https://www.bbc.com/news/world-60525350"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("❌ Failed to fetch page:", response.status_code)
        return

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = []
    for tag in soup.find_all(["h3", "h2"]):
        text = tag.get_text(strip=True)
        if "Ukraine" in text and len(text.split()) > 3:
            headlines.append({
                "title": text,
                "source": "BBC",
                "date": datetime.today().strftime("%Y-%m-%d")
            })
        if len(headlines) >= max_articles:
            break

    Path("data").mkdir(exist_ok=True)
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["title", "source", "date"])
        writer.writeheader()
        writer.writerows(headlines)

    print(f"✅ Saved {len(headlines)} rows to {output_file}")

if __name__ == "__main__":
    fetch_bbc_ukraine_news_csv()
