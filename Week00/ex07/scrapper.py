import requests
from bs4 import BeautifulSoup


URL = "https://data.1337ai.org/"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
tr = soup.find_all('tr')

list1 = []

for tag in tr:
    li = []
    r = tag.find_all('th')
    li.append(r)
    if (li):
        list1.append(li)
print(list1)
