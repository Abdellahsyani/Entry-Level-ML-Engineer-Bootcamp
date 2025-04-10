import requests
from bs4 import BeautifulSoup

URL = "https://www.octoparse.com/template/amazon-product-scraper-by-keywords"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# cards = soup.find_all("div", class_="table-scroll-box")
cards = soup.find_all("div", class_="t-max-height")

for card in cards:
    print(card.text)
