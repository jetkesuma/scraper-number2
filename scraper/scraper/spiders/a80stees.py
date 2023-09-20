import scrapy


class A80steesSpider(scrapy.Spider):
    name = "80stees"
    allowed_domains = ["www.80stees.com"]
    start_urls = ["https://www.80stees.com/a/search?q=christmas"]

    def parse(self, response):
        yield {'title': response.css('title::text').get()}

