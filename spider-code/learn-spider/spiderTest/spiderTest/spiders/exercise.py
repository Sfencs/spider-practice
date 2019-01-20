# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from spiderTest.items import PersonInfoItem
class ExerciseSpider(scrapy.Spider):
    name = 'exercise'
    allowed_domains = ['exercise.kingname.info']
    start_urls = ['http://exercise.kingname.info/exercise_xpath_3.html']

    def parse(self, response):
        person_list=response.xpath('//div[@class="person_table"]/table/tbody/tr')
        for person in person_list:
            item = PersonInfoItem()
            person_info = person.xpath('td/text()').extract()
            item['name'] = person_info[0]
            item['age'] = person_info[1]
            item['salary'] = person_info[2]
            item['phone'] = person_info[3]
            yield item
        pass
