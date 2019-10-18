# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CookrecipeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()#菜名
    image = scrapy.Field()#效果图
    materials = scrapy.Field()#用料
    steps = scrapy.Field()#步骤
    pass
