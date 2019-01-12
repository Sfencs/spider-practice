# -*- coding: utf-8 -*-
import requests
import redis
import lxml.html
import os
client_redis = redis.StrictRedis()


def get_pictures_to_redius():
    html = requests.get("http://news.4399.com/gonglue/lscs/kptj/")
    html_str = html.content.decode('gbk')
    selector = lxml.html.fromstring(html_str)

    url_list = selector.xpath('//ul[@class="cf"]/li/a/img/@lz_src')
    picture_name_list = selector.xpath('//ul[@class="cf"]/li/a/div/text()')
    print(len(url_list), len(picture_name_list))
    for url in url_list:
        print(url)
        client_redis.lpush("url_queue", url)
    for name in picture_name_list:
        print(name)
        client_redis.lpush("picture_name", name)
    # picture_byte = requests.get(url_list[0]).content
    # file_path = os.path.join('炉石传说图片', picture_name_list[0] + '.jpg')
    # print(file_path)
    # with open(file_path, 'wb') as f:
    #     f.write(picture_byte)


def write_picture_to_file():
    while client_redis.llen("url_queue") > 0:
        name = client_redis.rpop('picture_name').decode()
        url = client_redis.rpop('url_queue')
        picture_byte = requests.get(url).content
        file_path = os.path.join('炉石传说图片', name + '.jpg')
        with open(file_path, 'wb') as f:
            f.write(picture_byte)
        print('存入' + name)


get_pictures_to_redius()
write_picture_to_file()
