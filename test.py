import requests
from bs4 import BeautifulSoup

page = requests.get("https://quotes.toscrape.com/")

if page.status_code == 200:
    print("Page is available")
    parsedPage = BeautifulSoup(page.content, 'lxml')
    topTenTags = parsedPage.find('div',{"class":"col-md-4 tags-box"})
    listTopTags = topTenTags.find_all('a')

    # for tag in listTopTags:
    #     print(tag.attrs['href'])

    print(parsedPage.h1.text)

else:
    print("Page is not available")