# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

class CheerupEhimePipeline(object):

    def open_spider(self, spider):
        self.template = open(spider.settings.get('TEMPLATE')).read()
    
    def process_item(self, item, spider):
        open(os.path.join(spider.settings.get('POSTDIR'), '{year:04}{month:02}{date:02}-{autonomy}-{month:02}{date:02}{seq:02}.md'.format(**item)), 'w').write(self.template.format(**item))
        return item
