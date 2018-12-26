# -*- coding: utf-8 -*-
import requests
import re

html = requests.get('http://www.wuyanxia.net/read/77374/8826758.html')
html_str = html.content.decode('GBK')
#print(html_str)
block=re.findall('<!--主内容-->(.*?)</div>',html_str,re.S)[0]
#print(block)
chaptename = re.findall('<span id="htmltimu">(.*?)</span>', html_str, re.S)[0]
chaptename = chaptename.replace(' ', '')
content = re.findall('</table>(.*)', block, re.S)[0]
#print(content)
content = content.replace('&nbsp;', ' ')
content = content.replace('<br />', '')
print(content)


