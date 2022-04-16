import requests
from bs4 import BeautifulSoup

page = requests.get("https://quotes.toscrape.com/")

if page.status_code == 200:
    print("Page is available")
    parsedPage = BeautifulSoup(page.content, 'lxml')
    topTenTags = parsedPage.find('div',{"class":"col-md-4 tags-box"})
    listTopTags = topTenTags.find_all('a')
    print(listTopTags)
else:
    print("Page is not available")