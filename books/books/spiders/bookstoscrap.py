import scrapy


class BookstoscrapSpider(scrapy.Spider):
    name = 'bookstoscrap'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        bookBlock = response.xpath('//li[@class="col-xs-6 col-sm-4 col-md-3 col-lg-3"]')[0]
        title = bookBlock.xpath('.//h3/a/text()').get()
        price = bookBlock.xpath('.//p[@class="price_color"]/text()').get()

        result = {
            'title': title,
            'price': price
        }
        
        yield result