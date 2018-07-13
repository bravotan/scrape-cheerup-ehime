# -*- coding: utf-8 -*-
import scrapy
import re
import html2text
from ..items import CheerupEhimeItem


class UwajimaSpider(scrapy.Spider):
    name = 'uwajima'    
    allowed_domains = ['www.city.uwajima.ehime.jp']
    start_urls = ['https://www.city.uwajima.ehime.jp/soshiki/list3-1.html']

    def parse(self, response):
        for n, link in enumerate(response.css('#news_wrap').css('a::attr(href)').extract(), start=1):
            yield scrapy.Request(url=response.urljoin(link), callback=self.parse_pages,
                                 meta={'item': {'seq': n}})

    def parse_pages(self, response):
        title=response.css('h1::text').extract_first()
        y, m, d = [int(n) for n in response.css('#content_date::text').re('\d+')]
        mdbody = html2text.html2text(response.css('div.detail_free').extract_first())
        item = CheerupEhimeItem(title=title, year=y, month=m, date=d,
                               autonomy=self.name,
                               autonomy_ja='宇和島市', url=response.url,
                               body=mdbody)
        item.update(response.meta['item'])
        yield item
