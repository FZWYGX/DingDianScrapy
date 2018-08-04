# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChapterItem(scrapy.Item):

    # 小说章节url
    url = scrapy.Field()
    # 小说风格
    style = scrapy.Field()
    # 小说名字
    name = scrapy.Field()
    # 小说作者
    author = scrapy.Field()
    # 小说章节汇总
    chapters = scrapy.Field()
    # 小说章节汇总和url汇总, 组成字典
    chapters_urls = scrapy.Field()


class ContentItem(scrapy.Item):

    # 每小说具体一章的url
    url = scrapy.Field()
    # 小说的名字
    name = scrapy.Field()
    # 小说这一章的名字
    chapter = scrapy.Field()
    # 小说这一章的内容
    content = scrapy.Field()