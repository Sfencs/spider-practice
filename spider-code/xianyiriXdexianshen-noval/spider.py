# -*- coding: utf-8 -*-
import requests
import redis
import pymongo
import lxml.html


client_mongo = pymongo.MongoClient(host='localhost', port=27017)
client_redis = redis.StrictRedis()


def get_url_to_redis():
    html = requests.get("http://dongyeguiwu.zuopinj.com/5532/")
    html_str = html.content.decode()
    selector = lxml.html.fromstring(html_str)

    url_list = selector.xpath('//div[@class="book_list"]/ul/li/a/@href')
    for url in url_list:
        client_redis.lpush("url_queue", url)


if __name__ == "__main__":
    get_url_to_redis()
    db = client_mongo["spider"]
    collection = db["xianyiriX"]
    while client_redis.llen("url_queue") > 0:
        url = client_redis.rpop("url_queue")
        html_str = requests.get(url).content.decode()
        selector = lxml.html.fromstring(html_str)
        chapter = selector.xpath('//div[@class="h1title"]/h1/text()')[0]
        # 好像直接取p会自动根据里边其他标签分割成部分放入列表
        content = selector.xpath('//div[@id="htmlContent"]/p/text()')
        # content.replace('<br>','')
        dict = {"chapter": chapter, "content": '\n'.join(content)}
        collection.insert_one(dict)
        print("添加:" + chapter)
