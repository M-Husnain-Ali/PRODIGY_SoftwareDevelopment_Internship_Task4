import requests
from bs4 import BeautifulSoup
import pandas

books = []
for i in range(1, 5):
    url = f"https://books.toscrape.com/catalogue/page-1.html"
    r = requests.get(url)
    r = r.content
    soup = BeautifulSoup(r, "html.parser")
    ol = soup.find("ol")
    article = ol.find_all("article", class_="product_pod")

    for art in article:
        img = art.find("img")
        title = img.attrs["alt"]
        star = art.find("p")["class"][1]
        price = art.find("p", class_="price_color").text
        books.append([title, star, price])

file = pandas.DataFrame(books, columns=["Title", "Price", "Star_Rating"])
file.to_csv("Books.csv")
