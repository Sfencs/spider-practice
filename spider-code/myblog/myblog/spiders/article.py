# -*- coding: utf-8 -*-
import scrapy
from scrapy.conf import settings
from myblog.items import MyblogItem
from scrapy_redis.spiders import RedisSpider
from lxml import etree
from html import unescape
class ArticleSpider(RedisSpider):

    redis_key = 'myblogSpider:start_urls'
    name = 'article'
    allowed_domains = ['hcyue.cn']
    start_urls = ['https://www.hcyue.cn/archives/']
    host = 'https://hcyue.cn'
    #HEADERS = settings['HEADERS']

    def parse(self, response):
        title_tag_list = response.xpath('//a[@class="post-title-link"]')
        for title_tag in title_tag_list:
            article_title = title_tag.xpath('span/text()').extract_first()
            article_url = self.host+title_tag.xpath('@href').extract_first()
            item = MyblogItem()
            item['title'] = article_title
            item['url'] = article_url
            yield scrapy.Request(article_url,headers=self.settings['HEADERS'],dont_filter=True,callback=self.parse_detail,meta={'item':item})
        pass

    def parse_detail(self,response):

        item = response.meta['item']
        post_time = response.xpath('//time[@itemprop="dateCreated"]/text()').extract_first()
        category = response.xpath('//span[@itemprop="about"]/a/span/text()').extract_first()
        post_body = response.xpath('//div[@class="post-body"]')
        body_html = unescape(etree.tostring(post_body[0]._root).decode())
        item['post_time'] = post_time
        item['category'] = category
        item['detail'] = body_html
        yield item
        pass