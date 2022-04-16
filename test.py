import requests
from bs4 import BeautifulSoup

page = requests.get("https://quotes.toscrape.com/")

if page.status_code == 200:
    print("Page is available")
    parsedPage = BeautifulSoup(page.content, 'lxml')
    # parsedPage = BeautifulSoup(page.content, 'html.parser')
    # parsedPage = BeautifulSoup(page.content, 'html5lib')
    print(parsedPage.title)