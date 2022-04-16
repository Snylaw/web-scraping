import requests
from bs4 import BeautifulSoup

page = requests.get("https://quotes.toscrape.com/")

if page.status_code == 200:
    print("Page is available")
    parsedPage = BeautifulSoup(page.content, 'lxml')
    
    print(parsedPage.select('a[href^="/tag/inspirational/page/1/"]'))

else:
    print("Page is not available")