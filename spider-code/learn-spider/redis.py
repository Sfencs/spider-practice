# -*- coding: utf-8 -*-
import requests
import redis
import pymongo
import lxml.html
client=redis.StrictRedis()
html=requests.get("https://www.cnblogs.com/sfencs-hcy/p/9769505.html")
