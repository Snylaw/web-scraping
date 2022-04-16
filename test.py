import requests
from bs4 import BeautifulSoup

page = requests.get("https://quotes.toscrape.com/")

if page.status_code == 200:
    print("Page is available")
    parsedPage = BeautifulSoup(page.content, 'lxml')
    
    citations = parsedPage.find_all('span', class_='text')
    listCitations = [citation.text for citation in citations]

    print(listCitations)

else:
    print("Page is not available")