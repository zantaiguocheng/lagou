# -*- coding: utf-8 -*-
import scrapy


class LagoupachongSpider(scrapy.Spider):
    name = 'lagoupachong'
    allowed_domains = ['www.lagou.com/zhaopin/shujufenxishi/']
    start_urls = ['https://www.lagou.com/zhaopin/shujufenxishi/']

    def parse(self, response):
        print(response.body)
