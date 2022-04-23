from unicodedata import category
import scrapy


class BookstoscrapSpider(scrapy.Spider):
    name = 'bookstoscrap'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        category = response.xpath('//div[@class="side_categories"]/ul/li/ul/li')
        text = category.xpath('normalize-space(.//a/text())').getall()
        
        result = {
            'category': text
        }
        
        yield result