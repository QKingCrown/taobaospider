# -*- coding: utf-8 -*-
import scrapy
from first.items import FirstItem


class OnespiderSpider(scrapy.Spider):
    name = 'onespider'
    allowed_domains = ['www.taobao.com']
    start_urls = ['http://www.taobao.com/']

    def parse(self, response):
        List_1 = []
        item = FirstItem()
        item["name"] = "qzy"
        item["money"] = "12345"
        List_1.append(item)

        return List_1
