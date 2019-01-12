# -*- coding: utf-8 -*-
import requests

headers = {

    'Cookie': '_zap=79129e11-2234-4966-8944-adb60b9c14c6; _xsrf=XlcxvsBo5TJmQDTO4A1xe7smfeN5UfDh; d_c0="AGAo89B-aQ6PTpsOhTwhqyyn5UMUZnI7r58=|1540377843"; __utma=155987696.314537570.1540907037.1540907037.1540907037.1; __utmz=155987696.1540907037.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); capsion_ticket="2|1:0|10:1546854171|14:capsion_ticket|44:OTM3YzExMzZjYmYyNDFmNjkzMzA5YmM2MjI3NjU5NmQ=|c086c42543ef848a8ef40d784d2c8ba6781eb6f0a0fa94d539ffdff434f9ab2b"; z_c0="2|1:0|10:1546854208|4:z_c0|92:Mi4xSnBJdEF3QUFBQUFBWUNqejBINXBEaVlBQUFCZ0FsVk5RRzBnWFFDZjljMVVOd2RqY1YwM0I1a3c0VnZKZC1HMmlR|f0df44f91a65e1e4e2993945dc67fce794f61a7e90102232b38fda690eeba41b"; tst=r; q_c1=7630f07079a0448e96e7158153c19ed5|1546854209000|1546854209000; __gads=ID=12b7dd609550ae38:T=1546854211:S=ALNI_MbYqA3v-xw_Fvwi8FcWwM7v1YU4Gw; tgw_l7_route=66cb16bc7f45da64562a077714739c11; Hm_lvt_39dcd5bd05965dcfa70b1d2457c6dcae=1546854148,1547216943; Hm_lpvt_39dcd5bd05965dcfa70b1d2457c6dcae=1547216943',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
session = requests.Session()
source = session.get(
    'https://zhihu.com',
    headers=headers,
    verify=False).content.decode()
print(source)
