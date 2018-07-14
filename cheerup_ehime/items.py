# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CheerupEhimeItem(scrapy.Item):
    title = scrapy.Field()
    year = scrapy.Field()
    month = scrapy.Field()
    seq = scrapy.Field()
    date = scrapy.Field()
    city = scrapy.Field()
    city_ja = scrapy.Field()
    url = scrapy.Field()
    body = scrapy.Field()
