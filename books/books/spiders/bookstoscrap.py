import scrapy


class BookstoscrapSpider(scrapy.Spider):
    name = 'bookstoscrap'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        result = {
            'productsPrice': response.xpath('//p[@class="price_color"]/text()').getall(),
        }
        
        yield result