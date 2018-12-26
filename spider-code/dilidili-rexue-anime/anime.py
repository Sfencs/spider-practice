# -*- coding: utf-8 -*-
import requests
import lxml.html
import csv


def get_item_list(html_str):
    selector = lxml.html.fromstring(html_str)
    item_list = selector.xpath('//div[@class="anime_list"]/dl')
    return item_list


def get_item_content_dict(item):
    dict = {}
    dict['名称'] = item.xpath('dd/h3/a/text()')[0]
    d_lable = item.xpath('dd/div[@class="d_label"]/a/text()')
    dict['地区'] = d_lable[0]
    dict['年代'] = d_lable[1]
    dict['标签'] = ''
    for index, i in enumerate(d_lable, 0):
        if index > 1:
            dict['标签'] = dict['标签'] + i + ' '

    return dict


if __name__ == '__main__':
    html_str = requests.get('http://www.dilidili.wang/rexue/').content.decode()
    item_list = get_item_list(html_str)
    item_dict_list = []
    for item in item_list:
        item_dict_list.append(get_item_content_dict(item))
    with open('热血动漫.csv', 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['名称', '地区', '年代', '标签'])
        writer.writeheader()
        writer.writerows(item_dict_list)
