import scrapy


class LazarovSpider(scrapy.Spider):
    name = 'lazarov'
    allowed_domains = ['lazarovphoto.com']
    start_urls = ['http://lazarovphoto.com/']

    def parse(self, response):
        pass
