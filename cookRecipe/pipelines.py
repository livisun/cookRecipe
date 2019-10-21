# -*- coding: utf-8 -*-
from pymongo import MongoClient
from scrapy.conf import settings

class CookrecipePipeline(object):
    def __init__(self):
        self.client = MongoClient(host=settings['HOST'], port=settings['PORT'])
        # 数据库登录需要帐号密码的话
        # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])
        self.db = self.client[settings['DB']]  # 获得数据库的句柄
        self.coll = self.db[settings['TABLE']]  # 获得collection的句柄

    def process_item(self, item, spider):
        postItem = dict(item)  # 把item转化成字典形式
        self.coll.insert(postItem)  # 向数据库插入一条记录
        return item  # 会在控制台输出原item数据，可以选择不写
