# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LorryproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    engine = scrapy.Field()
    gear_box = scrapy.Field()
    carr_length = scrapy.Field()
    tf_drive = scrapy.Field()
    carr_st = scrapy.Field()
    emi = scrapy.Field()


class Lorrypro_detail(scrapy.Item):
    name = scrapy.Field()
    pic = scrapy.Field()
