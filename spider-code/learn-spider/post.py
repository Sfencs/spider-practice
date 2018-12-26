# -*- coding: utf-8 -*-
import requests
import re
'''
使用post方式提交获取页面
使用简单表达式提取内容
'''
data = {
    'name': 'kingname',
    'password': '1234567',
}

html = requests.post(
    'http://exercise.kingname.info/exercise_requests_post',
    data=data)
print(html.content.decode())
html = requests.post(
    'http://exercise.kingname.info/exercise_requests_post',
    json=data)
print(html.content.decode())

title = re.findall(
    'title>(.*?)</',
    html.content.decode(),
    re.S)  # re.s表示“.”可以匹配“\n”
print(title[0])
content = re.findall('p>(.*?)</p', html.content.decode(), re.S)
print('\n'.join(content))
