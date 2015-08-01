# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaomihrItem(scrapy.Item):
    work = scrapy.Field()
    worktype = scrapy.Field()
    location = scrapy.Field()
    # detail_link = scrapy.Field()
    requirement = scrapy.Field()
    duty = scrapy.Field()
    hr_way = scrapy.Field()
