# -*- coding: utf-8 -*-
import lxml.html
import requests


if __name__ == '__main__':
    html_ = requests.get(
        'https://tieba.baidu.com/f?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8')
    html_str = html_.content.decode()
    # print(html_str)

    selector = lxml.html.fromstring(html_str)
    info = selector.xpath(
        '//div[@class="threadlist_title pull_left j_th_tit "]/a[@rel="noreferrer"]/text()')
    for i in info:
        print(i)