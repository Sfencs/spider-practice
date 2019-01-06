# -*- coding: utf-8 -*-
import requests
import re
import json

class LeSpider():

    comment_url='http://api.my.le.com/vcm/api/list?jsonp=jQuery19108339382637251942_1546789205636&type=video&rows=20&page=1&sort=&cid=1&source=1&xid={vid}&pid={pid}&ctype=cmt%2Cimg%2Cvote&listType=1&_=1546789205644'

    header={'Accept': '*/*',
'Accept-Encoding' :'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Cookie': 'tj_lc=5c9178fc09b66618f1f31aa3f22b78f7; tj_uuid=-_15467811859630159379; tj_env=1; ssoCookieSynced=1; language=zh-cn; sso_curr_country=CN; ark_uuid=ck-33d68842-e259-4298-b39d-5dcf1de8f5c6; bd_xid=5c9178fc09b66618f1f31aa3f22b78f7; tj_v2c=-31522468_1; daily_popup=1',
'Host': 'api.my.le.com',
'Referer': 'http://www.le.com/ptv/vplay/31522468.html?ref=jrjd_pc',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}


    def __init__(self,url):
        self.necessary_info={}
        self.url=url
        self.get_id()
        self.get_comment()

    def get_source(self,url,header):
        return requests.get(url,header).content.decode()

    def get_id(self):
        html_htr=self.get_source(self.url,self.header)
        vid=re.search('vid: (\d+)',html_htr).group(1)
        pid = re.search('pid: (\d+)', html_htr).group(1)
        self.necessary_info['vid']=vid
        self.necessary_info['pid'] = pid

    def get_comment(self):
        url=self.comment_url.format(vid=self.necessary_info['vid'],pid=self.necessary_info['pid'])
        source=self.get_source(url,self.header)
        source_json=source[source.find('{"'):-1]
        comment_dict=json.loads(source_json)
        comments=comment_dict["data"]
        for comment in comments:
            print('姓名：'+comment['user']['username']+"  评论："+comment['content'])

if __name__=="__main__":
    spider=LeSpider('http://www.le.com/ptv/vplay/31522468.html?ref=jrjd_pc')