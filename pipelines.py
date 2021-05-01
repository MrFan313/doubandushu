# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os,requests
class DoubandushuPipeline(object):
    def process_item(self, item, spider):
        k = item["kname"][0]
        p = item["pic"][0]
        res = requests.get(p)
        path = p.split('/')[-1]
        if not os.path.exists(path = "picture"):
            os.mkdir("picture")
        else:
            with open(os.path.join('picture',item["kname"][0]+".jpg"),mode='wb')as file:
                file.write(res.content)
        print("当前图片下载完成!")
        return item
