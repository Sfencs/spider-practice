# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider

class ScrapyRedisTestSpider(RedisSpider):
    name = 'scrapy_redis_test'
    allowed_domains = ['url.com']
    start_urls = ['http://url.com/']
    redis_key = 'ScrapyRedisTestSpider:start_urls'
    def parse(self, response):
        pass
