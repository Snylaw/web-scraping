import requests

page = requests.get("https://quotes.toscrape.com/")
# print(page)
# print(page.content)
# print(page.status_code)

if page.status_code == 200:
    print("Page is available")