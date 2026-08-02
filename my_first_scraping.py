import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

products_data = []

print("\n--- SCRAPING DATA AND GENERATING SPREADSHEET ---")

for book in books:
    title = book.h3.a["title"]
    
    
    price_text = book.find("p", class_="price_color").text.replace("£", "").replace("Â", "").strip()
   
    products_data.append({
        "Book Title": title,
        "Price (GBP)": price_text
    })

df = pd.DataFrame(products_data)
df.to_excel("extracted_books.xlsx", index=False)

print("Done! The file 'extracted_books.xlsx' was created successfully!")
print("-----------------------------------------\n")