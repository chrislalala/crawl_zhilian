# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals  
import json  
import codecs  




 
class TutorialInfoPipeline(object):
    def open_spider(self, spider):
        self.f = open('TutorialInfo.txt', 'w')
 


    def process_item(self, item, spider):
        try:
            line = item['info'] + '\n'
            self.f.write(line)
        except:
            pass
        return item

    def close_spider(self, spider):
        self.f.close()
