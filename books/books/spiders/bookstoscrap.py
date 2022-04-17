import scrapy


class BookstoscrapSpider(scrapy.Spider):
    name = 'bookstoscrap'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        result = {
            'title': response.xpath('//head/title')
        }
        
        yield result