import requests
from bs4 import BeautifulSoup
import json

page = requests.get("https://quotes.toscrape.com/")

if page.status_code == 200:
    print("Page is available")
    parsedPage = BeautifulSoup(page.content, 'lxml')

    divQuotes = parsedPage.find_all('div', class_='quote')

    def extract_data(divQuotes):
        quotes = divQuotes.find('span', class_='text').text
        author = divQuotes.find('small', class_='author').text
        tags = [tag.text for tag in divQuotes.find_all('a', class_='tag')]
        data = {
            'quotes': quotes,
            'author': author,
            'tags': tags
        }
        return data

    listQuotes = []

    for quotes in divQuotes:
        listQuotes.append(extract_data(quotes))

    with open('quotes.json', 'w') as file:
        json.dump(listQuotes, file)

else:
    print("Page is not available")