# -*- coding: utf-8 -*-
import scrapy


class Baidu2Spider(scrapy.Spider):
    name = 'baidu2'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        print(response.body.decode())
        title=response.xpath('//title/text()').extract()
        print(title)