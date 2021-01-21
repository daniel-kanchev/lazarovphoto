import scrapy
from datetime import datetime
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from lazarovphoto.items import Article


class LazarovSpider(scrapy.Spider):
    name = 'lazarov'
    allowed_domains = ['lazarovphoto.com']
    start_urls = ['https://lazarovphoto.com/blog']

    def parse(self, response):
        articles = response.xpath("//div[@scriptolia_item_id]")
        for article in articles:
            item = ItemLoader(Article(), response)
            item.default_output_processor = TakeFirst()

            title = article.xpath('.//h2/a/text()').get()
            link = article.xpath('.//h2/a/@href').get()
            date = article.xpath('.//div[@original_date]/text()').get()
            date = format_date(date)
            content = article.xpath(".//div[@class='scriptolia-blog-posting-message']/text()").get()

            item.add_value('title', title)
            item.add_value('date', date)
            item.add_value('link', response.urljoin(link))
            item.add_value('content', content)

            yield item.load_item()


def format_date(date):
    date_dict = {
        "януари": "January",
        "февруари": "February",
        "март": "March",
        "април": "April",
        "май": "May",
        "юни": "June",
        "юли": "July",
        "август": "August",
        "септември": "September",
        "октомври": "October",
        "ноември": "November",
        "декември": "December",
    }

    date = date.split(" ")
    date[1] = date[1][:-1]
    for key in date_dict.keys():
        if date[1] == key:
            date[1] = date_dict[key]
    date = " ".join(date)

    date_time_obj = datetime.strptime(date, '%d %B %Y %H:%M')
    date = date_time_obj.strftime("%Y/%m/%d %H:%M")
    return date
