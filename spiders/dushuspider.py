# -*- coding: utf-8 -*-
import scrapy
from doubandushu.items import DoubandushuItem
import os


class DushuspiderSpider(scrapy.Spider):
    name = 'dushuspider'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/top250']

    def parse(self, response):
        # 定位标签
        dushu_item = response.xpath('//tr[@class = "item"]')
        # 遍历数据
        for item in dushu_item:
            # 创建采集对象
            dushu = DoubandushuItem()
            print(dushu)
            dushu['kname'] = item.xpath(
                'td[@valign="top"]/div[@class="pl2"]/a/@title').extract()
            dushu['pic'] = item.xpath('td/a/img/@src').extract()
            yield dushu

        # 深度采集
        next_path = response.xpath(
            '//div[@id="content"]/div/div[1]/div/ div / span[3] / a/@href').extract()[0]
        # print(next_path1)
        if next_path:
            choice = input("是否继续翻页:y/n?\n")
            if choice.lower() == 'y':
                yield scrapy.Request(next_path, callback=self.parse)
            else:
                os.path.exists(0)
        pass
