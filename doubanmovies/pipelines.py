# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import csv
class DoubanmoviesPipeline(object):

    #def __init__(self):
     #   self.file=codecs.open('douban.csv',mode='wb')
      #  self.file.write(codecs.BOM_UTF8)

    def process_item(self, item, spider):
        return item

