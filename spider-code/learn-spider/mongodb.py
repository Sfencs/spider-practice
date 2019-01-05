# -*- coding: utf-8 -*-
import pymongo
from bson.objectid import ObjectId
#client=pymongo.MongoClient('mongodb://用户名:密码@服务器IP或域名:端口号')
# client=pymongo.MongoClient('mongodb://localhost:27017')
client=pymongo.MongoClient(host='localhost',port=27017)
db1=client['test1']
db2=client.test2
collection1=db1['test1_collection']
collection2=db2.test2_collection
# data=[{'name':'sfencs','age':20,'hobby':'coding'},{'name':'tom','age':30,'hobby':'playing'}]
# # data={'name':'sfencs','age':20,'hobby':'coding'}
# result=collection1.insert_many(data)
# print(result)# <pymongo.results.InsertManyResult object at 0x000002B3B4B71D08>
# print(result.inserted_ids)# [ObjectId('5c23a4a8080b33197c17cb0e'), ObjectId('5c23a4a8080b33197c17cb0f')]
# people=collection1.find_one({'name':'sfencs'})
# people['age']=15
# result=collection1.delete_many({'age':18})
# print(result.deleted_count)
# result=collection1.distinct('name')
# print(result)

def add(list1=None):
    if list1==None:
        list1=[1,2,3]
    list1.append(4)
    return list1


