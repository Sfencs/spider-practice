# -*- coding: utf-8 -*-
import requests

'''
get方式获取自己博客园的页面源代码
'''

html = requests.get('https://www.cnblogs.com/sfencs-hcy/')
html_bytes = html.content
html_str = html_bytes.decode()
print(html_str)
