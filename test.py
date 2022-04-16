import requests
from bs4 import BeautifulSoup

page = requests.get("https://quotes.toscrape.com/")

if page.status_code == 200:
    print("Page is available")
    parsedPage = BeautifulSoup(page.content, 'lxml')
    links = parsedPage.find_all('a')
    for link in links:
        print(link.get('href'))
else:
    print("Page is not available")