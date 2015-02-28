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
class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["watchguard.com"]
    start_urls = (
        'http://www.watchguard.com/',
    )
    def parse(self, response):
        result_list = response.xpath('//*[contains(@src, "watchguard")]//@src | //*[contains(@href, "watchguard")]//@href').extract()
#        self.log("result_list: %s" % result_list)
        for link in result_list:
            global item_count
            item_count += 1
            if re.match(r'^http', link) == None:
                link = response.url + link
                self.log("construct new url %s with releative path.." % link)
            self.log("Getting Item[%s]: URL: %s" % (item_count, link))
            yield scrapy.http.Request(link, callback=self.follow_link_lvl_1)
        self.log("Continue next page")
        result = response.xpath('//li/a/@href').extract()
        for page in result:
            if re.match(r'^http', page) == None:
                page = response.url + page
            global page_count
            page_count += 1
            self.log("Getting page[%s]: URL: %s" % (page_count, page))
            yield scrapy.http.Request(page, callback=self.parse)
    def follow_link_lvl_1(self, response):
        self.log("sending request to %s ...." % response.url)
