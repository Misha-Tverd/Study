import csv
from googlesearch import search
import requests
from bs4 import BeautifulSoup

# Дані для пошуку
name = "Вербіцький Олександр"
city = "Хмельницький"
keywords = ["будівництво", "суд", "незаконне", "порушення"]
query = f'"{name}" {city} {" ".join(keywords)}'

# Файл для збереження результатів
output_file = "enhanced_results.csv"

# Функція для збору інформації зі сторінки
def get_page_description(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        title = soup.title.string if soup.title else "Без заголовка"
        meta_desc = soup.find("meta", attrs={"name": "description"})
        description = meta_desc["content"] if meta_desc else "Опис відсутній"
        
        return title, description
    except Exception as e:
        return "Помилка доступу", str(e)

# Пошук і збереження результатів
def parse_information(query):
    results = []
    for url in search(query, num_results=20):  # Шукаємо більше результатів
        title, description = get_page_description(url)
        results.append({"URL": url, "Title": title, "Description": description})
    
    # Зберігаємо результати в CSV
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["URL", "Title", "Description"])
        writer.writeheader()
        writer.writerows(results)
    print(f"Результати збережені у {output_file}")

# Викликаємо функцію
parse_information(query)
# ще одна робота яка не знадобилася