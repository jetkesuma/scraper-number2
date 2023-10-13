import scrapy


class TsscrapeSpider(scrapy.Spider):
    name = "tsscrape"
    custom_settings = {
        'FEEDS': {'data.csv': {'format': 'csv',}}
    }

    def start_requests(self):
        url = 'https://www.80stees.com/collections/80s-movies'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        product = response.css('div.grid-item')
