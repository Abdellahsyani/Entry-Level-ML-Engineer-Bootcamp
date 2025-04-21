import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://data.1337ai.org/"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
rows = soup.find_all('tr')
data = []
headers = [th.text for th in rows[0].find_all('th')]

for tag in rows[1:]:
    values = [td.text.strip() for td in tag.find_all('td')]
    if len(headers) == len(values):
        data.append(dict(zip(headers, values)))
panda = pd.DataFrame(data)
panda.to_csv('data.csv', index=False)
