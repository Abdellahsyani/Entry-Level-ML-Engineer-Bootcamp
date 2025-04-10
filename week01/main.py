import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
res = soup.find(id="ResultsContainer")

job_cards = res.find_all("div", class_="box")

for card in job_cards:
    title = card.find("h1", class_="title is-2")
    company = card.find("h2", class_="company")
    loc = card.find("p", id="location")
    print(title.text)
    print(company.text)
    print(loc.text)
