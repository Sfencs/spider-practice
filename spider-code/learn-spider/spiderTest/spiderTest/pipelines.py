# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings

class SpidertestPipeline(object):

    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        db_name = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host,port=port)
        db = client[db_name]
        self.post=db[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
        spider_test=dict(item)
        self.post.insert(spider_test)
        return item
