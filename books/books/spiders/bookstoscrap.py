from unicodedata import category
import scrapy


class BookstoscrapSpider(scrapy.Spider):
    name = 'bookstoscrap'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        div_image = response.xpath('//div[@class="image_container"]')[0]
        div_image_child = div_image.xpath('.//child::node()')
        div_image_sibling = div_image.xpath('.//following-sibling::node()')
        div_image_parents = div_image.xpath('.//ancestor::node()')
        
        result = {
            'div': div_image_parents
        }
        
        yield result