# -*- coding: utf-8 -*-
import re  
import scrapy
from scrapy import Request
from tutorial.items import TutorialItem

class Tut_Spider(scrapy.Spider):

    name = "tut_spider"
    start_urls = ["http://company.zhaopin.com/"]

    def parse(self,response):
        i = 0
        for company in response.xpath('//a[contains(@href, "http://company.zhaopin.com")]/text()').extract():
            if i < 9 :
                print (company)
                mainpage_url = "http://sou.zhaopin.com/jobs/searchresult.ashx?bj=160000&in=210500%3B160400%3B160000%3B160600&jl=北京%2B广州%2B深圳%2B海口&kw="+ company +"&p=1&kt=2&isadv=0"
                yield scrapy.Request(mainpage_url,dont_filter=True,callback=self.parse_mainpage)
            i = i+1





    def parse_mainpage(self, response):

        for href in response.xpath('//a[contains(@href, "http://jobs.zhaopin.com/0")]/@href').extract():
            try:
                yield scrapy.Request(href,dont_filter=True,callback = self.parse_info)
            except:
                continue

        next_url = response.xpath("//li[@class = 'pagesDown-pos']/a/@href").extract()[0]
        if next_url:
            yield scrapy.Request(next_url,dont_filter=True,callback=self.parse_mainpage)




    def parse_info(self, response):
        item = TutorialItem()
        zhaopininfo = response.xpath('//p/text()').re(r'[1-9].*')

        for tlt in zhaopininfo:
            item['info'] = re.sub(r'[0-9.；、，。]','',tlt)
            yield item
            

        




        











        
