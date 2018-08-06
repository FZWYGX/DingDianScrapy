# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from traceback import format_exc
from ..items import ChapterItem, ContentItem
from scrapy_redis.spiders import RedisCrawlSpider


class A23usSpider(RedisCrawlSpider):
    name = '23us'
    allowed_domains = ['www.23us.so']
    # start_urls = ['https://www.23us.so/']
    redis_key = '23us:start_urls'

    rules = (
        # 匹配小说章节页面, 示例网址: https://www.23us.so/files/article/html/2/2739/index.html
        Rule(LinkExtractor(allow=r'https://www\.23us\.so/files/article/html/\d{0,5}/\d{0,10}/index\.html'), callback="parse_index"),
        # 匹配小说介绍页面
        Rule(LinkExtractor(allow=r'https://www\.23us\.so/xiaoshuo/\d+\.html'), callback="parse_item"),
        # 下面三个是匹配小说不同分类
        Rule(LinkExtractor(allow=r'/list.*?'), follow=True),
        Rule(LinkExtractor(allow=r'/full.*?'), follow=True),
        Rule(LinkExtractor(allow=r'/top.*?'), follow=True),
        # 匹配小说排行榜
        Rule(LinkExtractor(allow=r'https://www.23us.so/.*?'), follow=True),

    )

    def parse_item(self, response):
        print(response.url)
        index_url = response.xpath("//p[@class='btnlinks']/a/@href").extract_first()
        print(index_url)
        yield scrapy.Request(url=index_url,
                             callback=self.parse_index,
                             errback=self.error_back,
                             priority=10)

    def parse_index(self, response):
        """
        解析小说章节页面
        """
        print("我进入了parse_index")
        url = response.url
        # 小说风格
        style = response.xpath("//div[@class='bdsub']/dl/dt/a//text()").extract()
        style = style[1]

        # 小说名字
        name = response.xpath("//div[@class='bdsub']/dl/dd[1]/h1/text()").extract_first().replace("最新章节", "")

        # 小说作者
        author = response.xpath("//div[@class='bdsub']/dl/dd[2]/h3/text()").extract_first().replace("作者：", "")

        # 小说章节
        chapters = response.xpath("//table[@id='at']//text()").extract()
        urls = response.xpath("//table[@id='at']//a/@href").extract()

        # 小说章节和章节对应的url组成字典
        chapters_urls = {chapters[i]: urls[i] for i in range(len(chapters))}

        # 实例化item
        item = ChapterItem(url=url, style=style, name=name,
                           author=author, chapters=chapters,
                           chapters_urls=chapters_urls)
        yield item

        for content in urls:
            yield scrapy.Request(url=content,
                                 callback=self.parse_content,
                                 errback=self.error_back,
                                 priority=20)

    def parse_content(self, response):
        """
        解析小说每一章具体的内容
        """
        url = response.url
        print(url)

        # 小说名字
        name = response.xpath("//div[@class='bdsub']/dl/dt/a//text()").extract()
        name = name[-1]

        # 章节名字
        chapter = response.xpath("//h1/text()").extract_first().strip()

        # 小说这一章的内容
        content = response.xpath("//dd[@id='contents']//text()").extract()
        content = "\n".join(i.strip() for i in content if len(i.strip()) > 0)

        # 实例化item
        item = ContentItem(url=url, name=name,
                           chapter=chapter, content=content)
        yield item

    def error_back(self, e):
        """
        报错函数
        """
        self.logger.error(format_exc())
