from typing import List

import scrapy
from parsel import Selector


class TsSpider(scrapy.Spider):
    name = "ts"
    allowed_domains = ["www.80stees.com"]
    start_urls = ["https://www.80stees.com/collections/80s-movies"]

    def parse(self, response):
        detail_products: List[Selector] = response.css ('.hero-body is-flex-column is-justify-center .has-text-weight-bold '
                                        'is-size-6-mobile is-size-5-tablet heading line-height-1-mobile '
                                        'has-no-text-transform a')
        for detail in detail_products:
            href = detail.
            yield response.follow(href, callback=self.parse_detail)


    def parse_detail(self, response):
        yield {'title': response.css('title::text').get()}
