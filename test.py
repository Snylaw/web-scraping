import requests
from bs4 import BeautifulSoup

page = requests.get("https://quotes.toscrape.com/")

if page.status_code == 200:
    print("Page is available")
    parsedPage = BeautifulSoup(page.content, 'lxml')
    
    firstQuote = parsedPage.find('div', class_='quote')

    sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></a>", 'lxml')
    print(sibling_soup.b.next_sibling)
    print(sibling_soup.c.previous_sibling)

else:
    print("Page is not available")