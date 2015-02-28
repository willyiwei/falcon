# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.shell import inspect_response
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
import time
global item_count
global page_count
item_count = 0
page_count = 0
base = "http://www.baidu.com"
url = "http://www.baidu.com/s?wd="
param = ""
class ExampleSpider(scrapy.Spider):
    name = "baidu"
#    start_urls = (
        #'http://search.jd.com/Search?keyword=north%20face&enc=utf-8&suggest=0',
#        'http://search.jd.com/Search?keyword=columbia&enc=utf-8&suggest=0',
#    )
    def __init__(self, keyword=None, *args, **kwargs):
        super(ExampleSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['%s%s%s' % (url, keyword, param)]
    def parse(self, response):
        result_list = response.xpath('//div/h3/a/@href').extract()
#        self.log("result_list: %s" % result_list)
        for link in result_list:
            global item_count
            item_count += 1
#            if re.match(r'www\.baidu\.com', link):
 #                continue 
#                link = link.lstrip()
           #     self.log("construct new url %s with releative path.." % link)
#            link = 'http://' + link
            self.log("Getting Item[%s]: URL: %s" % (item_count, link))
            yield scrapy.http.Request(link, callback=self.follow_link_lvl_1)
        self.log("Continue next page")
        for page in response.css('.n'):
            # print page
            next_page = page.xpath("@href").extract()[0]
            next_page = "%s%s" % (base, next_page)
            self.log("Continue next page with URL: %s" % next_page)
            global page_count
            page_count += 1
#            time.sleep( 5 )
            # self.log("sleep 5 seconds to avoid get caught")
            yield scrapy.http.Request(next_page, callback=self.parse)
    def follow_link_lvl_1(self, response):
        self.log("sending request to %s ...." % response.url)
