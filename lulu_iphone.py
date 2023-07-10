import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.luluhypermarket.com/en-qa/department-store-mobiles-smart-phones/c/HY00214730?sort=discount-desc&q=%3Anewest-desc%3Abrand%3AAPPLE%3Afeature-Resolution%3A2556%25E2%2580%2591by%25E2%2580%25911179-pixel%2Bresolution%2Bat%2B460%25C2%25A0ppi%3Afeature-Resolution%3A2796%25E2%2580%2591by%25E2%2580%25911290-pixel%2Bresolution%2Bat%2B460%25C2%25A0ppi%3Afeature-Resolution%3A2532%25E2%2580%2591by%25E2%2580%25911170-pixel%2Bresolution%2Bat%2B460%25C2%25A0ppi%3Afeature-Resolution%3A2778-by-1284-pixel%2Bresolution%2Bat%2B458%2Bppi"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

product_descs = soup.find_all("div", class_="product-desc")

rows = []
for product_desc in product_descs:
    name = product_desc.find("h3").text.strip()
    price = product_desc.find("p", class_="product-price has-icon").span.text.strip()

    # Extracting model, color, and storage from the name
    model = name.split(", ")[0]
    storage = int(name.split(", ")[-2].replace(" GB Storage", ""))
    color = name.split(", ")[-1]
    price = float(price.replace("QAR", "").replace(",", ""))

    rows.append([model, color, storage, price])

# Writing the data to a CSV file
with open("lulu_iphone.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Model", "Color", "Storage", "Price(QAR)"])  # Writing header
    writer.writerows(rows)