import requests
from bs4 import BeautifulSoup
import json
import pandas as pd


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

def getQuotes(pageUrl):
    page = requests.get(pageUrl)
    parsedPage = BeautifulSoup(page.content, 'lxml')
    quotes = parsedPage.find_all('div', class_='quote')

    if(len(quotes) > 0):
        listQuotes = [extract_data(quote) for quote in quotes]
        return listQuotes
    else:
        return None

data = getQuotes('http://quotes.toscrape.com/')
for i in range(2,100):
    pageUrl = f'http://quotes.toscrape.com/page/{i}/'
    currentPageQuotes = getQuotes(pageUrl)

    if(currentPageQuotes is not None):
        data.extend(currentPageQuotes)
    else:
        break

dataPd = pd.DataFrame.from_dict(data)
dataPd.to_csv('quotes_full.csv')