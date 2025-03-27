import requests
from bs4 import BeautifulSoup


URL = "https://www.octoparse.com/template/craigslist-scraper"

r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

print(soup.prettify())
