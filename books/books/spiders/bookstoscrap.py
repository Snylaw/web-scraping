import scrapy


class BookstoscrapSpider(scrapy.Spider):
    name = 'bookstoscrap'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        books = response.xpath("//h3[contains(.//text(),'the')]")
        text = books.xpath('.//text()').getall()
        
        result = {
            'text_book': text
        }
        
        yield result