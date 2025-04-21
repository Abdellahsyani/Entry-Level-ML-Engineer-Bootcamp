import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://data.1337ai.org/"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
tr = soup.find_all('tr')

list1 = []

for tag in tr:
    li = []
    th = tag.find_all('th')
    td = tag.find_all('td')
    li.append([tag.text for tag in th])
    li.append([tag.text for tag in td])
    if (li):
        list1.append(li)

panda = pd.DataFrame(list1)
panda.to_csv('data.csv', index=False)
