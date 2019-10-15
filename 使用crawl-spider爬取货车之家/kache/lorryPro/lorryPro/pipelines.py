# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

import pymysql
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class ImgproPipeline(ImagesPipeline):
    #对图片数据进行操作
    def get_media_requests(self, item, info):
        if item.__class__.__name__ == 'Lorrypro_detail':
            print(item['pic'],'进入的')
            yield scrapy.Request(item['pic'])

    def file_path(self, request, response=None, info=None):
        file_name = request.url.split('/')[-1]
        return file_name

    def item_completed(self, results, item, info):
        if item.__class__.__name__ == 'Lorrypro_detail':
            print(item['pic'],'出去的')
        return item


class LorryproPipeline(object):
    db = None
    cursor = None

    def open_spider(self, spider):
        print('开始爬虫')
        self.db = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='123', db='spider', charset='utf8')

    def process_item(self, item, spider):
        if item.__class__.__name__ == 'LorryproItem':
            name = item['name']
            price = item['price']
            engine = item['engine']
            gear_box = item['gear_box']
            carr_length = item['carr_length']
            tf_drive = item['tf_drive']
            carr_st = item['carr_st']
            emiss_standard = item['emi']
            # print(name, price, engine, gear_box, carr_length, tf_drive, carr_st, emiss_standard)
            sql = 'insert into app01_trunk(name,price,engine,gear_box,carr_length,tf_drive,carr_st,emiss_standard) values("%s","%s","%s","%s","%s","%s","%s","%s")' % (name, price, engine, gear_box, carr_length, tf_drive, carr_st, emiss_standard)
        else:
            c_name = item['name']
            pic = item['pic']
            sql = 'insert into app01_pic(name,pic_name) values("%s","%s")' % (c_name, pic.split('/')[-1])

        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()


        return item


    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()
        print('爬虫完毕')