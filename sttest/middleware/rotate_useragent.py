#!/usr/bin/python
#-*-coding:utf-8-*-
 
import random
from scrapy import log
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
 
class RotateUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent=''):
        self.user_agent = user_agent
 
    def process_request(self, request, spider):
        # Random choose a user-agent
        ua = random.choice(self.user_agent_list)
        if ua:
            log.msg(format="%(request)s UserAgent: %(ua)s.",
                level=log.DEBUG, spider = spider, request=request, ua=ua)
            request.headers.setdefault('User-Agent', ua)
 
    #the default user_agent_list composes chrome,I E,firefox,Mozilla,opera,netscape
    #for more user agent strings,you can find it inhttp://www.useragentstring.com/pages/useragentstring.php
    user_agent_list = [\
        "Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)",\
        "Mozilla/5.0 (compatible; ABrowse 0.4; Syllable)",\
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)",\
        "Mozilla/4.0 (compatible; Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729); Windows NT 5.1; Trident/4.0)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB6; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; America Online Browser 1.1; rev1.5; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; America Online Browser 1.1; rev1.5; Windows NT 5.1; .NET CLR 1.0.3705; .NET CLR 1.1.4322; Media Center PC 4.0; InfoPath.1; .NET CLR 2.0.50727; Media Center PC 3.0; InfoPath.2)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; Windows NT 5.1; SV1; HbTools 4.7.0)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.0.3705; .NET CLR 1.1.4322; Media Center PC 3.1)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; Windows NT 5.1; SV1; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; Windows NT 5.1; FunWebProducts; (R1 1.5); HbTools 4.7.7)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; Windows NT 5.1)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; Windows 98)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1; SV1; .NET CLR 1.1.4322; InfoPath.1)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.5001; Windows NT 5.1; Trident/4.0)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.5000; Windows NT 5.1; Trident/4.0; .NET4.0C; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.27; Windows NT 5.1; Trident/4.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322; Media Center PC 4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; InfoPath.2)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.168; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.130; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30618)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.12; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.124; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.122; Windows NT 5.1; Trident/4.0; FunWebProducts)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.110; Windows NT 5.1; Trident/4.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.6; AOLBuild 4340.128; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.5; AOLBuild 4337.29; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.21022; .NET CLR 3.5.30729; .NET CLR 3.0.30618)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.89; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.0.04506)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.81; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30618) (Compatible; ; ; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.80; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.43; Windows NT 6.0; WOW64; GTB5; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30618)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.43; Windows NT 5.1; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.40; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30618)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.40; Windows NT 5.1; Trident/4.0; GTB6; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.36; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.30618; .NET CLR 3.5.30729)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.36; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30618)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.1; AOLBuild 4334.5011; Windows NT 6.1; WOW64; Trident/4.0; GTB7.2; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.1; AOLBuild 4334.5009; Windows NT 5.1; GTB5; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.1; AOLBuild 4334.5006; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.1; AOLBuild 4334.5006; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 1.0.3705; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.1; AOLBuild 4334.5000; Windows NT 5.1; Media Center PC 3.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322; InfoPath.1)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.1; AOLBuild 4334.34; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.1; AOLBuild 4334.34; Windows NT 5.1; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.1; AOLBuild 4334.27; Windows NT 6.0; WOW64; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.0.04506; Media Center PC 5.0); UnAuth-State",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.1; AOLBuild 4334.27; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; InfoPath.1); UnAuth-State",\
        "Mozilla/4.0 (compatible; MSIE 6.0; AOL 9.1; AOLBuild 4334.5006; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.0; AOLBuild 4327.5201; Windows NT 6.0; WOW64; Trident/4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.30729; .NET CLR 3.5.30729)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30618)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506; Seekmo 10.0.406.0)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.0; Windows NT 6.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.0; Windows NT 6.0; FunWebProducts; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506; Seekmo 10.0.341.0)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.0; Windows NT 5.1; Trident/4.0; GTB6; FunWebProducts; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.0; Windows NT 5.1; InfoPath.1)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.0; Windows NT 5.1; GTB5; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.0; Windows NT 5.1; GTB5; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.0; Windows NT 5.1; FunWebProducts; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) )",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 8.0; Windows NT 5.1; .NET CLR 2.0.50727)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 8.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 8.0; Windows NT 5.1; .NET CLR 1.0.3705)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; AOL 8.0; Windows NT 5.1; YComp 5.0.0.0; .NET CLR 1.0.3705)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; AOL 8.0; Windows NT 5.1; SV1; (R1 1.3); .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; AOL 8.0; Windows NT 5.1; Q312461)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; AOL 8.0; Windows NT 5.1; FunWebProducts; SV1)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; AOL 8.0; Windows NT 5.1; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; AOL 8.0; Windows NT 5.1; (R1 1.3))",\
        "Mozilla/4.0 (compatible; MSIE 6.0; AOL 8.0; Windows NT 5.0)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 7.0; Windows NT 5.1; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 7.0; Windows NT 5.1)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; AOL 7.0; Windows NT 5.1; YComp 5.0.2.4)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; AOL 7.0; Windows NT 5.1; SV1; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; AOL 7.0; Windows NT 5.1; SV1)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; AOL 7.0; Windows NT 5.1; Q312461)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; AOL 7.0; Windows NT 5.1; Hotbar 4.1.7.0)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; AOL 7.0; Windows NT 5.1)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; AOL 7.0; Windows 98; Win 9x 4.90; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; AOL 7.0; Windows 98; Win 9x 4.90)",\
        "Mozilla/4.0 (compatible; MSIE 5.5; AOL 6.0; Windows 98; Win 9x 4.90)",\
        "Mozilla/4.0 (compatible; MSIE 5.5; AOL 6.0; Windows 95)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; AOL 5.0; Windows NT 5.1)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; AOL 5.0; Windows 98)",\
        "Mozilla/4.0 (compatible; MSIE 5.5; AOL 5.0; Windows 98; YComp 5.0.0.0)",\
        "Mozilla/4.0 (compatible; MSIE 5.5; AOL 5.0; Windows 98)",\
        "Mozilla/4.0 (compatible; MSIE 5.0; AOL 5.0; Windows 98; DigExt)",\
        "Mozilla/4.0 (compatible; MSIE 5.0; AOL 5.0; Windows 95)",\
        "Mozilla/4.0 (compatible; MSIE 5.5; AOL 4.0; Windows 98)",\
        "Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 98; DigExt)",\
        "Mozilla/4.0 (compatible; MSIE 4.01; AOL 4.0; Windows 98)",\
        "Mozilla/4.0 (compatible; MSIE 4.01; AOL 4.0; Mac_68K)",\
        "Mozilla/5.0 (X11; U; Linux; de-DE) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",\
        "Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",\
        "Mozilla/5.0 (X11; U; Linux; ru-RU) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: 802 025a17d)",\
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )",\
        "Mozilla/5.0 (X11; U; Linux; pt-PT) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.4",\
        "Mozilla/5.0 (X11; U; Linux; it-IT) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.4 (Change: 413 12f13f8)",\
        "Mozilla/5.0 (X11; U; Linux; hu-HU) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.4 (Change: 388 835b3b6)",\
        "Mozilla/5.0 (X11; U; Linux; fr-FR) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.4",\
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.4",\
        "Mozilla/5.0 (X11; U; Linux; en-GB) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.4",\
        "Mozilla/5.0 (X11; U; Linux; cs-CZ) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.4 (Change: 333 41e3bc6)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; de-DE) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.4 (Change: )",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.4 (Change: )",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",\
        "Mozilla/5.0 (X11; U; Linux; nb-NO) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.2 (Change: 0 )",\
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.2 (Change: 189 35c14e0)",\
        "Mozilla/5.0 (X11; U; Linux; de-DE) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.2 (Change: 0 )",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; nl-NL) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-CH) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.2",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.34 (KHTML, like Gecko) Arora/0.11.0 Safari/534.34",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.34 (KHTML, like Gecko) Arora/0.10.2 Safari/534.34",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-MY) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.10.0",\
        "Mozilla/5.0 (Windows; U; ; hu-HU) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.10.0",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Avant Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506; .NET CLR 3.5.21022; InfoPath.2)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB6.4; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; chromeframe; Avant Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; InfoPath.1; .NET CLR 3.0.4506.",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Avant Browser; Avant Browser; .NET CLR 2.0.50727)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; Avant Browser)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; Avant Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; GTB6.3; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Avant Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; Avant Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506; .NET CLR 3.5.21022; InfoPath.2)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Avant Browser; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Avant Browser; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30618; InfoPath.2; OfficeLiveConnector.1.3; OfficeLivePatch.0.0)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Avant Browser; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",\
        "Mozilla/5.0 (Windows; U; WinNT; en; rv:1.0.2) Gecko/20030311 Beonex/0.8.2-stable",\
        "Mozilla/5.0 (X11; U; Linux i686; nl; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2 (Debian-1.99+2.0b2+dfsg-1)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1b2) Gecko/20060826 BonEcho/2.0b2",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.8.1b1) Gecko/20060601 BonEcho/2.0b1 (Ubuntu-edgy)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X Mach-O; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.9) Gecko/20071103 BonEcho/2.0.0.9",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.8pre) Gecko/20071012 BonEcho/2.0.0.8pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.7) Gecko/20070918 BonEcho/2.0.0.7",\
        "Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.8.1.7) Gecko/20070917 BonEcho/2.0.0.7",\
        "Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.8.1.6) Gecko/20070731 BonEcho/2.0.0.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.5pre) Gecko/20070622 BonEcho/2.0.0.5pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.1.4pre) Gecko/20070510 BonEcho/2.0.0.4pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.4pre) Gecko/20070410 BonEcho/2.0.0.4pre",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.4) Gecko/20070531 BonEcho/2.0.0.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-GB; rv:1.8.1.3pre) Gecko/20070302 BonEcho/2.0.0.3pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.1.3pre) Gecko/20070301 BonEcho/2.0.0.3pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.9a3) Gecko/20070409 BonEcho/2.0.0.3",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1.3) Gecko/20070322 BonEcho/2.0.0.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070213 BonEcho/2.0.0.2pre",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.2) Gecko/20070302 BonEcho/2.0.0.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2) Gecko/20070227 BonEcho/2.0.0.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.1pre) Gecko/20061203 BonEcho/2.0.0.1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.1pre) Gecko/20061122 BonEcho/2.0.0.1pre",\
        "Mozilla/5.0 (BeOS; U; Haiku BePC; en-US; rv:1.8.1.17) Gecko/20080831 BonEcho/2.0.0.17",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.14) Gecko/20080417 BonEcho/2.0.0.14",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.13) Gecko/20080401 BonEcho/2.0.0.13",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.12) Gecko/20080208 BonEcho/2.0.0.12",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.8.1.11) Gecko/20080208 BonEcho/2.0.0.11",\
        "Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.8.1.10) Gecko/20071128 BonEcho/2.0.0.10",\
        "Mozilla/5.0 (X11; U; Linux mips; en-US; rv:1.8.1.1) Gecko/20070628 BonEcho/2.0.0.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20070222 BonEcho/2.0.0.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20070217 BonEcho/2.0.0.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20070115 BonEcho/2.0.0.1",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.1) Gecko/20070131 BonEcho/2.0.0.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.1) Gecko/20061230 BonEcho/2.0.0.1",\
        "Mozilla/5.0 (X11; U; Win95; en-US; rv:1.8.1) Gecko/20061125 BonEcho/2.0",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061031 BonEcho/2.0",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061003 BonEcho/2.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1) Gecko/20061210 BonEcho/2.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1) Gecko/20061121 BonEcho/2.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1) Gecko/20061112 BonEcho/2.0",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1) Gecko/20061026 BonEcho/2.0",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1) Gecko/20061024 BonEcho/2.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en; rv:1.9a1) Gecko/20061128 BonEcho/0.7b1",\
        "Firefox based browser for Mac OS X. The XUL-based user interface used by most Mozilla based applications has been replaced with a native Cocoa interface",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; XH; rv:8.578.498) fr, Gecko/20121021 Camino/8.443+ (Firefox compatible)",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.8; it; rv:1.93.26.2658) Gecko/20141026 Camino/2.176.223 (MultiLang) (like Firefox/3.64.2268)0",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en; rv:1.9.2.14pre) Gecko/20101212 Camino/2.1a1pre (like Firefox/3.6.14pre)",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; de; rv:1.9.2.28) Gecko/20120308 Camino/2.1.2 (MultiLang) (like Firefox/3.6.28)",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; fr; rv:1.9.2.28) Gecko/20120308 Camino/2.1.2 (MultiLang) (like Firefox/3.6.28)",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en; rv:1.9.0.8pre) Gecko/2009022800 Camino/2.0b3pre",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; it; rv:1.9.0.19) Gecko/2010111021 Camino/2.0.6 (MultiLang) (like Firefox/3.0.19)",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.4; en; rv:1.9.0.19) Gecko/2010051911 Camino/2.0.3 (like Firefox/3.0.19)",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en; rv:1.9.0.18) Gecko/2010021619 Camino/2.0.2 (like Firefox/3.0.18)",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; de; rv:1.8.1.5pre) Gecko/20070605 Camino/1.6a1pre",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en; rv:1.8.1.4pre) Gecko/20070521 Camino/1.6a1pre",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; fr; rv:1.8.1.21) Gecko/20090327 Camino/1.6.7 (MultiLang) (like Firefox/2.0.0.21pre)",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en; rv:1.8.1.24) Gecko/20100305 Camino/1.6.11 (like Firefox/2.0.0.24)",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X Mach-O; en; rv:1.8.1.12) Gecko/20080206 Camino/1.5.5",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en; rv:1.8.1.6) Gecko/20070809 Camino/1.5.1",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en; rv:1.8.1.6) Gecko/20070809 Camino/1.5.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en; rv:1.8.1.4) Gecko/20070509 Camino/1.5",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en; rv:1.8.1.4) Gecko/20070607 Camino/1.5",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en; rv:1.9a4pre) Gecko/20070404 Camino/1.2+",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en; rv:1.8.1.2pre) Gecko/20070227 Camino/1.1b",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en; rv:1.8.1.2pre) Gecko/20070108 Camino/1.1a2",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1) Gecko/20061018 Camino/1.1a1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.0.1) Gecko/20060119 Camino/1.0b2+",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8) Gecko/20051228 Camino/1.0b1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8b4) Gecko/20050914 Camino/1.0a1",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.0.10) Gecko/20070228 Camino/1.0.4",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.0.7) Gecko/20060911 Camino/1.0.3 (MultiLang)",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.0.7) Gecko/20060911 Camino/1.0.3",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.0.4) Gecko/20060613 Camino/1.0.2",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.0.3) Gecko/20060427 Camino/1.0.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1b1) Gecko/20060721 Camino/1.0+",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1) Gecko/20061013 Camino/1.0+ (Firefox compatible)",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1a3) Gecko/20060601 Camino/1.0+",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.0.1) Gecko/20060214 Camino/1.0",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.0.1) Gecko/20060214 Camino/1.0",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.7) Gecko/20040517 Camino/0.8b",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.7.2) Gecko/20040825 Camino/0.8.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.0.1) Gecko/20030306 Camino/0.7",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/418.8 (KHTML, like Gecko, Safari) Cheshire/1.0.UNOFFICIAL",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko, Safari/419.3) Cheshire/1.0.ALPHA",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/418.9 (KHTML, like Gecko, Safari/111) Cheshire/1.0.ALPHA",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/418.9 (KHTML, like Gecko) Safari/419.3 Cheshire/1.0.ALPHA",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko, Safari/419.3) Cheshire/1.0.ALPHA",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; pl-PL; rv:1.0.1) Gecko/20021111 Chimera/0.6",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US; rv:1.0.1) Gecko/20021111 Chimera/0.6",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.0.1) Gecko/20030111 Chimera/0.6",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.0.1) Gecko/20021220 Chimera/0.6",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",\
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",\
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",\
        "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36",\
        "Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36",\
        "Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.6 Safari/537.11",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.26 Safari/537.11",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.17 Safari/537.11",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_0) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",\
        "Mozilla/5.0 (X11; FreeBSD amd64) AppleWebKit/536.5 (KHTML like Gecko) Chrome/19.0.1084.56 Safari/1EA69",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.22 (KHTML, like Gecko) Chrome/19.0.1047.0 Safari/535.22",\
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/19.0.1041.0 Safari/535.21",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",\
        "Mozilla/5.0 (X11; CrOS i686 1660.57.0) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.46 Safari/535.19",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.19 (KHTML, like Gecko) Ubuntu/11.10 Chromium/18.0.1025.142 Chrome/18.0.1025.142 Safari/535.19",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11",\
        "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.04 Chromium/17.0.963.65 Chrome/17.0.963.65 Safari/535.11",\
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/17.0.963.65 Chrome/17.0.963.65 Safari/535.11",\
        "Mozilla/5.0 (X11; FreeBSD amd64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_4) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11",\
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",\
        "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/17.0.940.0 Safari/535.8",\
        "Mozilla/5.0 (X11; CrOS i686 1193.158.0) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7",\
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.8",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2",\
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.872.0 Safari/535.2",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.864.0 Safari/535.2",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.861.0 Safari/535.2",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.860.0 Safari/535.2",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.834.0 Safari/535.1",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.824.0 Safari/535.1",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.815.0 Safari/535.1",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.814.0 Safari/535.1",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.813.0 Safari/535.1",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.813.0 Safari/535.1",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.812.0 Safari/535.1",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.810.0 Safari/535.1",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.809.0 Safari/535.1",\
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/10.04 Chromium/14.0.808.0 Chrome/14.0.808.0 Safari/535.1",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.803.0 Safari/535.1",\
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.803.0 Safari/535.1",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.803.0 Safari/535.1",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.801.0 Safari/535.1",\
        "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.794.0 Safari/535.1",\
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.792.0 Safari/535.1",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.792.0 Safari/535.1",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.790.0 Safari/535.1",\
        "Mozilla/5.0 (X11; CrOS i686 13.587.48) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.43 Safari/535.1",\
        "Mozilla/5.0 ArchLinux (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1",\
        "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1",\
        "Mozilla/5.0 (Windows NT 5.2; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1",\
        "Mozilla/5.0 (X11; Linux amd64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",\
        "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.220 Safari/535.1",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.215 Safari/535.1",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.215 Safari/535.1",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1",\
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1",\
        "Mozilla/5.0 (X11; CrOS i686 0.13.587) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.14 Safari/535.1",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.107 Safari/535.1",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.36 (KHTML, like Gecko) Chrome/13.0.766.0 Safari/534.36",\
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.35 (KHTML, like Gecko) Ubuntu/10.10 Chromium/13.0.764.0 Chrome/13.0.764.0 Safari/534.35",\
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.33 (KHTML, like Gecko) Ubuntu/9.10 Chromium/13.0.752.0 Chrome/13.0.752.0 Safari/534.33",\
        "Mozilla/5.0 (Windows NT 6.1; en-US) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.750.0 Safari/534.30",\
        "Mozilla/5.0 (X11; CrOS i686 12.0.742.91) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.93 Safari/534.30",\
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.91 Chromium/12.0.742.91 Safari/534.30",\
        "Mozilla/5.0 ArchLinux (X11; U; Linux x86_64; en-US) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.60 Safari/534.30",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.113 Safari/534.30",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30",\
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30",\
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/10.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30",\
        "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_6) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30",\
        "Mozilla/5.0 (X11; CrOS i686 12.433.216) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.105 Safari/534.30",\
        "Mozilla/5.0 ArchLinux (X11; U; Linux x86_64; en-US) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100",\
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100 Safari/534.30",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100 Safari/534.30",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.724.100 Safari/534.30",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.25 (KHTML, like Gecko) Chrome/12.0.704.0 Safari/534.25",\
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.702.0 Chrome/12.0.702.0 Safari/534.24",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/12.0.702.0 Safari/534.24",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.699.0 Safari/534.24",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_6) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.698.0 Safari/534.24",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.71 Safari/534.24",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.68 Safari/534.24",\
        "Mozilla/5.0 Slackware/13.37 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/11.0.696.50",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.34 Safari/534.24",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.3 Safari/534.24",\
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.3 Safari/534.24",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.12 Safari/534.24",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.04 Chromium/11.0.696.0 Chrome/11.0.696.0 Safari/534.24",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.694.0 Safari/534.24",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.21 (KHTML, like Gecko) Chrome/11.0.682.0 Safari/534.21",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_0; en-US) AppleWebKit/534.21 (KHTML, like Gecko) Chrome/11.0.678.0 Safari/534.21",\
        "Mozilla/5.0 (Windows NT) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.669.0 Safari/534.20",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.18 (KHTML, like Gecko) Chrome/11.0.661.0 Safari/534.18",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.17 (KHTML, like Gecko) Chrome/11.0.655.0 Safari/534.17",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.17 (KHTML, like Gecko) Chrome/11.0.654.0 Safari/534.17",\
        "Mozilla/4.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/11.0.1245.0 Safari/537.36",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/534.17 (KHTML, like Gecko) Chrome/10.0.649.0 Safari/534.17",\
        "Mozilla/5.0 (X11; U; Linux armv7l; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16",\
        "Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.134 Safari/534.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.134 Safari/534.16",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.648.133 Chrome/10.0.648.133 Safari/534.16",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.648.133 Chrome/10.0.648.133 Safari/534.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.127 Safari/534.16",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.127 Safari/534.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru-RU; AppleWebKit/534.16; KHTML; like Gecko; Chrome/10.0.648.11;Safari/534.16)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.11 Safari/534.16",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.648.0 Chrome/10.0.648.0 Safari/534.16",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.642.0 Chrome/10.0.642.0 Safari/534.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.638.0 Safari/534.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.634.0 Safari/534.16",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.04 Chromium/10.0.612.3 Chrome/10.0.612.3 Safari/534.15",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.611.0 Chrome/10.0.611.0 Safari/534.15",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML,like Gecko) Chrome/9.1.0.0 Safari/540.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.600.0 Safari/534.14",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-CA) AppleWebKit/534.13 (KHTML like Gecko) Chrome/9.0.597.98 Safari/534.13",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.44 Safari/534.13",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.15 Safari/534.13",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.107 Safari/534.13 v1416758524.9051",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.107 Safari/534.13 v1416670950.695",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.107 Safari/534.13 v1333515017.9196",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.0 Safari/534.13",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.0 Safari/534.13",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.0 Safari/534.13",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Ubuntu/10.04 Chromium/9.0.595.0 Chrome/9.0.595.0 Safari/534.13",\
        "Mozilla/5.0 (X11; U; Windows NT 6; en-US) AppleWebKit/534.12 (KHTML, like Gecko) Chrome/9.0.587.0 Safari/534.12",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.12 (KHTML, like Gecko) Chrome/9.0.579.0 Safari/534.12",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/8.1.0.0 Safari/540.0",\
        "Mozilla/5.0 (X11; U; CrOS i686 0.9.130; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.344 Safari/534.10",\
        "Mozilla/5.0 (X11; U; CrOS i686 0.9.128; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.341 Safari/534.10",\
        "Mozilla/5.0 (X11; U; CrOS i686 0.9.128; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.339",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.224 Safari/534.10",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.224 Safari/534.10",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.200 Safari/534.10",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.548.0 Safari/534.10",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.15) Gecko/20101027 Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.9 (KHTML, like Gecko) Chrome/7.0.531.0 Safari/534.9",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.24 Safari/534.7",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.6 (KHTML, like Gecko) Chrome/7.0.500.0 Safari/534.6",\
        "Mozilla/5.0 (ipad Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.6 (KHTML, like Gecko) Chrome/7.0.498.0 Safari/534.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.4 (KHTML, like Gecko) Chrome/6.0.481.0 Safari/534.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.53 Safari/534.3",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.470.0 Safari/534.3",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.462.0 Safari/534.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.461.0 Safari/534.3",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.461.0 Safari/534.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.460.0 Safari/534.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.459.0 Safari/534.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.458.1 Safari/534.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.458.1 Safari/534.3",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.458.0 Safari/534.3",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.457.0 Safari/534.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.2 (KHTML, like Gecko) Chrome/6.0.454.0 Safari/534.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.2 (KHTML, like Gecko) Chrome/6.0.453.1 Safari/534.2",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/534.2 (KHTML, like Gecko) Chrome/6.0.453.1 Safari/534.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.1 SUSE/6.0.428.0 (KHTML, like Gecko) Chrome/6.0.428.0 Safari/534.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.428.0 Safari/534.1",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.427.0 Safari/534.1",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.417.0 Safari/534.1",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.414.0 Safari/534.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.8 (KHTML, like Gecko) Chrome/6.0.397.0 Safari/533.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.999 Safari/533.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.99 Safari/533.4",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_0; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.99 Safari/533.4",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.86 Safari/533.4",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_0; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.86 Safari/533.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.127 Safari/533.4",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; fr-FR) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.126 Safari/533.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.370.0 Safari/533.4",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.366.2 Safari/533.4",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.366.0 Safari/533.4",\
        "Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.358.0 Safari/533.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.357.0 Safari/533.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.355.0 Safari/533.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.354.0 Safari/533.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.353.0 Safari/533.3",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.343.0 Safari/533.2",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.7 Safari/533.2",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.3 Safari/533.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.2 Safari/533.2",\
        "Mozilla/5.0 (X11; U; Linux i586; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.1 Safari/533.2",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Chrome/5.0.335.0 Safari/533.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.308.0 Safari/532.9",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.307.1 Safari/532.9",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.302.2 Safari/532.8",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; it-IT) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.25 Safari/532.5",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_8; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.241.0 Safari/532.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.3 (KHTML, like Gecko) Chrome/4.0.227.0 Safari/532.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.3 (KHTML, like Gecko) Chrome/4.0.223.5 Safari/532.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.3 Safari/532.2",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.2 Safari/532.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.2 Safari/532.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.1 Safari/532.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.1 Safari/532.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.8 Safari/532.2",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.6 Safari/532.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.6 Safari/532.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.5 Safari/532.2",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.5 Safari/532.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.4 Safari/532.2",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.4 Safari/532.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.3 Safari/532.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.2 Safari/532.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.12 Safari/532.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.12 Safari/532.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.0 Safari/532.2",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.221.8 Safari/532.2",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.221.8 Safari/532.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.221.6 Safari/532.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.221.6 Safari/532.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.221.0 Safari/532.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.5 Safari/532.1",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.3 Safari/532.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.3 Safari/532.1",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.1 Safari/532.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.1 Safari/532.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.1 Safari/532.1",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.0 Safari/532.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.0 Safari/532.1",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_0; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.212.1 Safari/532.1",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.212.0 Safari/532.0",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.212.0 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.212.0 Safari/532.0",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.212.0 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.7 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.4 Safari/532.0",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.2 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.2 Safari/532.0",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.2 Safari/532.0",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.0 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.0 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.210.0 Safari/532.0",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.209.0 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.209.0 Safari/532.0",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.208.0 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.208.0 Safari/532.0",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.208.0 Safari/532.0",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.1 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.1 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.1 Safari/532.0",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.0 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.0 Safari/532.0",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.205.0 Safari/532.0",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.204.0 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.204.0 Safari/532.0",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.4 Safari/532.0",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.0 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.0 Safari/532.0",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.0 Safari/532.0",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.2 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-DE) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.2 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198.1 Safari/532.0",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198.0 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198.0 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198 Safari/532.0",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.11 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.11 Safari/532.0",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.0 Safari/532.0",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196.2 Safari/532.0",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196.0 Safari/532.0",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.4 Safari/532.0",\
        "Mozilla/4.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.33 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.3 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.24 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.21 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.21 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.20 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.17 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.10 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.10 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.1 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.1 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.4 (KHTML, like Gecko) Chrome/3.0.194.0 Safari/531.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/531.3 (KHTML, like Gecko) Chrome/3.0.193.2 Safari/531.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/531.3 (KHTML, like Gecko) Chrome/3.0.193.0 Safari/531.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.2 (KHTML, like Gecko) Chrome/3.0.191.3 Safari/531.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.0 (KHTML, like Gecko) Chrome/3.0.191.0 Safari/531.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.0 (KHTML, like Gecko) Chrome/2.0.182.0 Safari/531.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.8 (KHTML, like Gecko) Chrome/2.0.178.0 Safari/530.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.8 (KHTML, like Gecko) Chrome/2.0.177.0 Safari/530.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.7 (KHTML, like Gecko) Chrome/2.0.176.0 Safari/530.7",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US) AppleWebKit/530.7 (KHTML, like Gecko) Chrome/2.0.175.0 Safari/530.7",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.175.0 Safari/530.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.173.1 Safari/530.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.173.0 Safari/530.5",\
        "Mozilla/6.0 (Windows; U; Windows NT 6.0; en-US) Gecko/2009032609 Chrome/2.0.172.6 Safari/530.7",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.6 Safari/530.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.43 Safari/530.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.43 Safari/530.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.40 Safari/530.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.39 Safari/530.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.23 Safari/530.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.2 Safari/530.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; eu) AppleWebKit/530.4 (KHTML, like Gecko) Chrome/2.0.172.0 Safari/530.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.0 Safari/530.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.1 (KHTML, like Gecko) Chrome/2.0.170.0 Safari/530.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.1 (KHTML, like Gecko) Chrome/2.0.168.0 Safari/530.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.0 (KHTML, like Gecko) Chrome/2.0.162.0 Safari/530.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/528.10 (KHTML, like Gecko) Chrome/2.0.157.2 Safari/528.10",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_0; en-US) AppleWebKit/528.10 (KHTML, like Gecko) Chrome/2.0.157.2 Safari/528.10",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.9 (KHTML, like Gecko) Chrome/2.0.157.0 Safari/528.9",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.10 (KHTML, like Gecko) Chrome/2.0.157.0 Safari/528.10",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/528.8 (KHTML, like Gecko) Chrome/2.0.156.1 Safari/528.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.8 (KHTML, like Gecko) Chrome/2.0.156.0 Version/3.2.1 Safari/528.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/528.8 (KHTML, like Gecko) Chrome/1.0.156.0 Safari/528.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.59 Safari/525.19",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.55 Safari/525.19",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.50 Safari/525.19",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.46 Safari/525.19",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.43 Safari/525.19",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.43 Safari/525.19",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.39 Safari/525.19",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.4.154.18 Safari/525.19",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.3.155.0 Safari/525.19",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.3.154.6 Safari/525.19",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.153.0 Safari/525.19",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.152.0 Safari/525.19",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.151.0 Safari/525.19",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.151.0 Safari/525.19",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.6 Safari/525.13",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.30 Safari/525.13",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13",\
        "Mozilla/5.0 (Linux; U; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13",\
        "Mozilla/5.0 (Macintosh; U; Mac OS X 10_5_7; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/ Safari/530.5",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/ Safari/530.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30 ChromePlus/1.6.3.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.98 Safari/534.13 ChromePlus/1.6.0.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.224 Safari/534.10 ChromePlus/1.5.2.0alpha1",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.224 Safari/534.10 ChromePlus/1.5.2.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.0alpha3 ChromePlus/1.5.1.0alpha3 ChromePlus/1.5.1.0alpha3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7 ChromePlus/1.5.0.0alpha1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7 ChromePlus/1.5.0.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7 ChromePlus/1.4.3.0alpha3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Chrome/5.0.336.0 Safari/533.1 ChromePlus/1.3.8.1",\
        "Mozilla/5.0 (Macintosh; U; PPC; en-US; mimic; rv:9.3.0) Gecko/20120117 Firefox/3.6.25 Classilla/CFM",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100409 Firefox/3.6.3 CometBird/3.6.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.5) Gecko/2009011615 Firefox/3.0.5 CometBird/3.0.5",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.30 (KHTML, like Gecko) Comodo_Dragon/12.1.0.0 Chrome/12.0.742.91 Safari/534.30",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Comodo_Dragon/4.1.1.11 Chrome/4.1.249.1042 Safari/532.5",\
        "Conkeror is a keyboard-oriented, customizable, extensible web browser based on Mozilla XULRunner, written mainly in JavaScript, and inspired by software such as Emacs and vi. Conkeror features a sophisticated keyboard system, allowing users to run commands and interact with content ",\
        "Mozilla/5.0 (Windows NT 6.1; rv:16.0) Gecko/20121010 conkeror/1.0pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.16) Gecko/20101209 Conkeror/0.9.2 (Debian-0.9.2+git100804-1)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.14) Gecko/20101020 Conkeror/0.9.2 (Debian-0.9.2+git100804-1)",\
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; Crazy Browser 3.1.0)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; InfoPath.2; Crazy Browser 3.0.5)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Crazy Browser 3.0.0 Beta2)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; Crazy Browser 3.0.0 Beta2)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; Crazy Browser 2.0.1)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; Crazy Browser 2.0.1)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Crazy Browser 2.0.1)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; HbTools 4.7.0; Crazy Browser 2.0.1)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; (R1 1.3; Crazy Browser 2.0.1); .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Q312461; SV1; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727; Crazy Browser 2.0.1)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Crazy Browser 2.0.1)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322; Crazy Browser 2.0.1)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; Crazy Browser 2.0.0)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322; Crazy Browser 2.0.0)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; YComp 5.0.0.0; Crazy Browser 1.0.5)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Crazy Browser 1.0.5; .NET CLR 1.1.4322; InfoPath.1)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Crazy Browser 1.0.5; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Crazy Browser 1.0.5)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; MyIE2; Crazy Browser 1.0.5; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FunWebProducts-MyWay; SV1; Crazy Browser 1.0.5)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Crazy Browser 1.0.5; .NET CLR 2.0.40607; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Crazy Browser 1.0.5; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Crazy Browser 1.0.5; (R1 1.3))",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; Crazy Browser 1.0.5)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/4.0; Deepnet Explorer 1.5.3; Smart 2x2; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Deepnet Explorer 1.5.3; Smart 2x2; .NET CLR 1.1.4322; InfoPath.1; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Deepnet Explorer 1.5.3; Smart 2x2)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; FunWebProducts; Deepnet Explorer 1.5.2; SpamBlockerUtility 4.7.1)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Deepnet Explorer 1.5.2; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Deepnet Explorer 1.5.0; .NET CLR 2.0.50727)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ (KHTML, like Gecko) Element Browser 5.0",\
        "Mozilla/5.0 (X11; U; Linux x86_64; it-it) AppleWebKit/534.26+ (KHTML, like Gecko) Ubuntu/11.04 Epiphany/2.30.6",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Epiphany/2.30.6 Safari/534.7",\
        "Mozilla/5.0 (X11; U; Linux x86; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Epiphany/2.30.6 Safari/534.7",\
        "Mozilla/5.0 (X11; U; Linux i686; it-it) AppleWebKit/531.2+ (KHTML, like Gecko) Safari/531.2+ Epiphany/2.30.2",\
        "Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Safari/531.2+ Epiphany/2.30.0",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fr-fr) AppleWebKit/531.2+ (KHTML, like Gecko) Safari/531.2+ Epiphany/2.29.91",\
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-cn) AppleWebKit/531.2+ (KHTML, like Gecko) Safari/531.2+ Epiphany/2.28.0 SUSE/2.28.0-2.4",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en; rv:1.9.0.8) Gecko/20080528 Epiphany/2.22 Firefox/3.0",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en; rv:1.9.0.7) Gecko/20080528 Epiphany/2.22",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en; rv:1.9.0.14) Gecko/20080528 Epiphany/2.22 (Debian/2.26.3-2)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en; rv:1.9) Gecko/20080528 Epiphany/2.22 Firefox/3.0",\
        "Mozilla/5.0 (X11; U; Linux i686; en_GB; rv:1.9.0.1) Gecko/20080528 Epiphany/2.22 Firefox/3.0",\
        "Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.8) Gecko/20080528 Epiphany/2.22 Firefox/3.0",\
        "Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.7) Gecko/20080528 Epiphany/2.22",\
        "Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.4) Gecko/20080528 Epiphany/2.22 Firefox/3.0",\
        "Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.14) Gecko/20080528 Epiphany/2.22 (Debian/2.26.3-2)",\
        "Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9) Gecko/20080528 (Gentoo) Epiphany/2.22 Firefox/3.0",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en; rv:1.8.1.13) Gecko/20080326 (Debian-1.8.1.13-1) Epiphany/2.20",\
        "Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9b3) Gecko Epiphany/2.20",\
        "Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.17) Gecko/20080927 Epiphany/2.20 Firefox/2.0.0.17 (Dropline GNOME)",\
        "Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.12) Gecko/20080208 (Debian-1.8.1.12-5) Epiphany/2.20",\
        "Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.10) Gecko/20071213 Epiphany/2.20 Firefox/2.0.0.10",\
        "Mozilla/5.0 (X11; U; FreeBSD i386; en; rv:1.8.1.12) Gecko/20080213 Epiphany/2.20 Firefox/2.0.0.12",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en; rv:1.8.1.4) Gecko/20061201 Epiphany/2.18 Firefox/2.0.0.4 (Ubuntu-feisty)",\
        "Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.5) Gecko/20070712 (Debian-1.8.1.5-1) Epiphany/2.18",\
        "Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.3) Gecko/20070322 Epiphany/2.18",\
        "Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.14) Gecko/20080416 Fedora/2.18.3-9.fc7 Epiphany/2.18 Firefox/2.0.0.14",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en; rv:1.8.1.4) Gecko/20070628 Epiphany/2.16 Firefox/2.0.0.4",\
        "Mozilla/5.0 (X11; U; Linux sparc64; en-US; rv:1.8.0.14eol) Gecko/20070505 (Debian-1.8.0.15~pre080323b-0etch2) Epiphany/2.14",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.11) Gecko/20071201 (Debian-1.8.1.11-1) Epiphany/2.14",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060928 (Debian-1.8.0.7-1) Epiphany/2.14",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.5) Gecko/20060731 Ubuntu/dapper-security Epiphany/2.14 Firefox/1.5.0.5",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.3) Gecko/20060523 Ubuntu/dapper Epiphany/2.14 Firefox/1.5.0.3",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.13pre) Gecko/20070505 (Debian-1.8.0.14~pre071019b-0lenny1) Epiphany/2.14",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.0.7) Gecko/20060928 (Debian-1.8.0.7-1) Epiphany/2.14",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20060208 Epiphany/1.8.3",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010 Epiphany/1.8.2 (Ubuntu) (Ubuntu package 1.0.7)",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.7.5) Gecko/20050105 Epiphany/1.4.8",\
        "Mozilla/5.0 (X11; U; Linux i686; rv:1.7.8) Gecko/20050831 Epiphany/1.4.8 (Debian)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.8) Gecko/20050831 Epiphany/1.4.8 (Debian)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.3) Gecko/20041007 Epiphany/1.4.7",\
        "Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)",\
        "Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.6) Gecko/20040413 Epiphany/1.2.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040114 Epiphany/1.0.7",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.4) Gecko/20030908 Epiphany/0.9.2",\
        "Mozilla/5.0 (X11; U; Linux i686; pl-pl) AppleWebKit/525.1+ (KHTML, like Gecko, Safari/525.1+) epiphany-browser",\
        "Mozilla/4.0 (compatible; MSIE 5.23; Macintosh; PPC) Escape 5.1.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; x64; fr; rv:1.9.2.13) Gecko/20101203 Firebird/3.6.13",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.6a) Gecko/20031002 Firebird/0.7",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.5) Gecko/20031007 Firebird/0.7",\
        "Mozilla/5.0 (Windows; U; Win95; en-US; rv:1.5) Gecko/20031007 Firebird/0.7",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.5a) Gecko/20030729 Mozilla Firebird/0.6.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.5a) Gecko/20030728 Mozilla Firebird/0.6.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.5a) Gecko/20030728 Mozilla Firebird/0.6.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.5a) Gecko/20030728 Mozilla Firebird/0.6.1",\
        "Mozilla/5.0 (Windows; U; Win98; de-DE; rv:1.5a) Gecko/20030728 Mozilla Firebird/0.6.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.4b) Gecko/20030630 Mozilla Firebird/0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.4b) Gecko/20030516 Mozilla Firebird/0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.4a) Gecko/20030425 Mozilla Firebird/0.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:x.xx) Gecko/20030504 Mozilla Firebird/0.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.5a) Gecko/20030630 Mozilla Firebird/0.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.4b) Gecko/20030516 Mozilla Firebird/0.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.4b) Gecko/20030516 Mozilla Firebird/0.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.4b) Gecko/20030514 Mozilla Firebird/0.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:1.4b) Gecko/20030516 Mozilla Firebird/0.6",\
        "Mozilla/5.0 (Windows; U; Win98; de-DE; rv:1.4b) Gecko/20030516 Mozilla Firebird/0.6",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0",\
        "Mozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0",\
        "Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3",\
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0",\
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0",\
        "Mozilla/5.0 (Windows NT 6.2; rv:22.0) Gecko/20130405 Firefox/22.0",\
        "Mozilla/5.0 (Windows NT 6.1; rv:22.0) Gecko/20130405 Firefox/22.0",\
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1",\
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20130331 Firefox/21.0",\
        "Mozilla/5.0 (X11; Linux i686; rv:21.0) Gecko/20100101 Firefox/21.0",\
        "Mozilla/5.0 (Windows NT 6.2; rv:21.0) Gecko/20130326 Firefox/21.0",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130331 Firefox/21.0",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0",\
        "Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20130328 Firefox/21.0",\
        "Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20130401 Firefox/21.0",\
        "Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20100101 Firefox/21.0",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0",\
        "Mozilla/5.0 (Windows x86; rv:19.0) Gecko/20100101 Firefox/19.0",\
        "Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/18.0.1",\
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0.6",\
        "Mozilla/6.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1",\
        "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1",\
        "Mozilla/5.0 (Windows NT 6.1; rv:15.0) Gecko/20120716 Firefox/15.0a2",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1",\
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1",\
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:14.0) Gecko/20120405 Firefox/14.0a1",\
        "Mozilla/5.0 (Windows NT 5.1; rv:14.0) Gecko/20120405 Firefox/14.0a1",\
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:14.0) Gecko/20100101 Firefox/14.0.1",\
        "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/14.0.1",\
        "Mozilla/5.0 (Windows NT 6.0; rv:14.0) Gecko/20100101 Firefox/14.0.1",\
        "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",\
        "Mozilla/5.0 (Windows NT 5.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:11.0) Gecko Firefox/11.0",\
        "Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0",\
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 11_7_9; de-LI; rv:1.9b4) Gecko/2012010317 Firefox/10.0a4",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0a2) Gecko/20111101 Firefox/9.0a2",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0",\
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/7.0",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110612 Firefox/6.0a2",\
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20110814 Firefox/6.0",\
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.28) Gecko/20120306 Firefox/5.0.1",\
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",\
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",\
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",\
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",\
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",\
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",\
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",\
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",\
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",\
        "Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20110324 Firefox/4.2a1pre",\
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.2a1pre) Gecko/20110324 Firefox/4.2a1pre",\
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.2a1pre) Gecko/20110208 Firefox/4.2a1pre",\
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b9pre) Gecko/20101228 Firefox/4.0b9pre",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b8pre) Gecko/20101114 Firefox/4.0b8pre",\
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b8pre) Gecko/20101128 Firefox/4.0b8pre",\
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0b8pre) Gecko/20101127 Firefox/4.0b8pre",\
        "Mozilla/4.0 (compatible; Intel Mac OS X 10.6; rv:2.0b8) Gecko/20100101 Firefox/4.0b8)",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b7) Gecko/20101111 Firefox/4.0b7",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b6pre) Gecko/20100903 Firefox/4.0b6pre",\
        "Mozilla/5.0 (X11; Linux x86_64; rv:2.0b4) Gecko/20100818 Firefox/4.0b4",\
        "Mozilla/5.0 (Windows NT 5.2; rv:2.0b13pre) Gecko/20110304 Firefox/4.0b13pre",\
        "Mozilla/5.0 (X11; Linux i686; rv:2.0b12pre) Gecko/20110204 Firefox/4.0b12pre",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b11pre) Gecko/20110128 Firefox/4.0b11pre",\
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b11pre) Gecko/20110129 Firefox/4.0b11pre",\
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0b11pre) Gecko/20110126 Firefox/4.0b11pre",\
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b10pre) Gecko/20110118 Firefox/4.0b10pre",\
        "Mozilla/5.0 (X11; Linux i686; rv:2.0b10) Gecko/20100101 Firefox/4.0b10",\
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0b10) Gecko/20110126 Firefox/4.0b10",\
        "Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20110506 Firefox/4.0.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:2.0.1) Gecko/20110606 Firefox/4.0.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:2.0) Gecko/20110404 Fedora/16-dev Firefox/4.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows NT 6.1; rv:1.9) Gecko/20100101 Firefox/4.0",\
        "Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/2008092313 Ubuntu/9.25 (jaunty) Firefox/3.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.3) Gecko/20100401 Mozilla/5.0 (X11; U; Linux i686; it-IT; rv:1.9.0.2) Gecko/2008092313 Ubuntu/9.25 (jaunty) Firefox/3.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2b5) Gecko/20091204 Firefox/3.6b5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.9.2b5) Gecko/20091204 Firefox/3.6b5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.9.2b4) Gecko/20091124 Firefox/3.6b4 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2b1) Gecko/20091014 Firefox/3.6b1 GTB5",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2a1pre) Gecko/20090405 Firefox/3.6a1pre",\
        "Mozilla/5.0 (Windows; Windows NT 5.1; es-ES; rv:1.9.2a1pre) Gecko/20090402 Firefox/3.6a1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja; rv:1.9.2a1pre) Gecko/20090402 Firefox/3.6a1pre (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.9) Gecko/20100827 Red Hat/3.6.9-2.el6 Firefox/3.6.9",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:1.9.2.9) Gecko/20100913 Firefox/3.6.9",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-GB; rv:1.9.2.9) Gecko/20100824 Firefox/3.6.9",\
        "Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.2.8) Gecko/20101230 Firefox/3.6.8",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100723 SUSE/3.6.8-0.1.1 Firefox/3.6.8",\
        "Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9.2.8) Gecko/20100723 Ubuntu/10.04 (lucid) Firefox/3.6.8",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.8) Gecko/20100727 Firefox/3.6.8",\
        "Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; pt-BR; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; he; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0C)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.2.3) Gecko/20121221 Firefox/3.6.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.7) Gecko/20100726 CentOS/3.6-3.el5.centos Firefox/3.6.7",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.7 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.6) Gecko/20100628 Ubuntu/10.04 (lucid) Firefox/3.6.6 GTB7.1",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.6) Gecko/20100628 Ubuntu/10.04 (lucid) Firefox/3.6.6 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; pt-PT; rv:1.9.2.6) Gecko/20100625 Firefox/3.6.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.6) Gecko/20100625 Firefox/3.6.6 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; nl; rv:1.9.2.6) Gecko/20100625 Firefox/3.6.6",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; de-AT; rv:1.9.1.8) Gecko/20100625 Firefox/3.6.6",\
        "Mozilla/5.0 (X11; U; Linux i686; fa; rv:1.8.1.4) Gecko/20100527 Firefox/3.6.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-TW; rv:1.9.2.4) Gecko/20100611 Firefox/3.6.4 ( .NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ja; rv:1.9.2.4) Gecko/20100611 Firefox/3.6.4 GTB7.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-CN; rv:1.9.2.4) Gecko/20100513 Firefox/3.6.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; fr; rv:1.9.2.4) Gecko/20100523 Firefox/3.6.4 ( .NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2.4) Gecko/20100527 Firefox/3.6.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2.4) Gecko/20100513 Firefox/3.6.4 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-TW; rv:1.9.2.4) Gecko/20100611 Firefox/3.6.4 GTB7.0 ( .NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.2.4) Gecko/20100503 Firefox/3.6.4 ( .NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ko; rv:1.9.2.4) Gecko/20100523 Firefox/3.6.4",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; he; rv:1.9.1b4pre) Gecko/20100405 Firefox/3.6.3plugin1",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.3) Gecko/20100403 Firefox/3.6.3",\
        "Mozilla/5.0 (X11; U; Linux i686; ko-KR; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 GTB7.1",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; pl; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; hu; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 GTB7.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; es-ES; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 GTB7.0 ( .NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ca; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.9.2.28) Gecko/20120306 AskTbSTC-SRS/3.13.1.18132 Firefox/3.6.28 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja; rv:1.9.2.25) Gecko/20111212 Firefox/3.6.25 ( .NET CLR 3.5.30729; .NET4.0C)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.2.24) Gecko/20111103 Firefox/3.6.24",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; fr; rv:1.9.2.23) Gecko/20110920 Firefox/3.6.23",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; it; rv:1.9.2.22) Gecko/20110902 Firefox/3.6.22",\
        "Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.2.20) Gecko/20110803 Firefox/3.6.20",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.20) Gecko/20110804 Red Hat/3.6-2.el5 Firefox/3.6.20",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; de; rv:1.9.2.20) Gecko/20110803 Firefox/3.6.20",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; hu; rv:1.9.2.20) Gecko/20110803 Firefox/3.6.20 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; cs; rv:1.9.2.20) Gecko/20110803 Firefox/3.6.20",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.2) Gecko/20100316 AskTbSPC2/3.9.1.14019 Firefox/3.6.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2 ( .NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2 ( .NET CLR 3.0.04506.648)",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.7; en-US; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; de; rv:1.9.2.20) Gecko/20110803 Firefox/3.6.19",\
        "Mozilla/5.0 (X11; U; Linux x86_64; ru; rv:1.9.2.18) Gecko/20110628 Ubuntu/10.10 (maverick) Firefox/3.6.18",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.9.2.18) Gecko/20110628 Ubuntu/10.10 (maverick) Firefox/3.6.18",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.2.18) Gecko/20110615 Ubuntu/10.10 (maverick) Firefox/3.6.18",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ar; rv:1.9.2.18) Gecko/20110614 Firefox/3.6.18",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.2.18) Gecko/20110614 Firefox/3.6.18 ( .NET CLR 3.5.30729; .NET4.0E)",\
        "Mozilla/5.0 (X11; Linux i686 on x86_64; rv:5.0) Gecko/20100101 Firefox/3.6.17 Firefox/3.6.17",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.17) Gecko/20110420 Firefox/3.6.17",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR; rv:1.9.2.17) Gecko/20110420 Firefox/3.6.17 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; hu; rv:1.9.2.17) Gecko/20110420 Firefox/3.6.17 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; ja-JP; rv:1.9.2.16) Gecko/20110323 Ubuntu/10.10 (maverick) Firefox/3.6.16",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.9.2.16) Gecko/20110319 Firefox/3.6.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; pl; rv:1.9.2.16) Gecko/20110319 Firefox/3.6.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.9.2.16) Gecko/20110319 Firefox/3.6.16 ( .NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.2.16) Gecko/20110319 AskTbUTR/3.11.3.15590 Firefox/3.6.16",\
        "Mozilla/5.0 (X11; U; Linux i686; nl; rv:1.9.2.15) Gecko/20110303 Ubuntu/8.04 (hardy) Firefox/3.6.15",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.2.15) Gecko/20110330 CentOS/3.6-1.el5.centos Firefox/3.6.15",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15 ( .NET CLR 3.5.30729; .NET4.0C) FirePHP/0.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (X11; U; Linux armv7l; en-US; rv:1.9.2.14) Gecko/20110224 Firefox/3.6.14 MB860/Version.0.43.3.MB860.AmericaMovil.en.MX",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-AU; rv:1.9.2.14) Gecko/20110218 Firefox/3.6.14",\
        "Mozilla/5.0 Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.13) Firefox/3.6.13",\
        "Mozilla/5.0 (X11; U; Linux x86_64; nb-NO; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.04 (lucid) Firefox/3.6.13",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.2.13) Gecko/20110103 Fedora/3.6.13-1.fc14 Firefox/3.6.13",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101223 Gentoo Firefox/3.6.13",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101206 Red Hat/3.6-3.el4 Firefox/3.6.13",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-NZ; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.9.2.13) Gecko/20101206 Red Hat/3.6-2.el5 Firefox/3.6.13",\
        "Mozilla/5.0 (X11; U; Linux MIPS32 1074Kf CPS QuadCore; en-US; rv:1.9.2.13) Gecko/20110103 Fedora/3.6.13-1.fc14 Firefox/3.6.13",\
        "Mozilla/5.0 (X11; U; Linux i686; pt-BR; rv:1.9.2.13) Gecko/20101209 Fedora/3.6.13-1.fc13 Firefox/3.6.13",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.2.13) Gecko/20101209 CentOS/3.6-2.el5.centos Firefox/3.6.13",\
        "Mozilla/5.0 (X11; U; NetBSD i386; en-US; rv:1.9.2.12) Gecko/20101030 Firefox/3.6.12",\
        "Mozilla/5.0 (X11; U; Linux x86_64; es-ES; rv:1.9.2.12) Gecko/20101027 Fedora/3.6.12-1.fc13 Firefox/3.6.12",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.12) Gecko/20101102 Gentoo Firefox/3.6.12",\
        "Mozilla/5.0 (X11; U; Linux ppc; fr; rv:1.9.2.12) Gecko/20101027 Ubuntu/10.10 (maverick) Firefox/3.6.12",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.12) Gecko/20101114 Gentoo Firefox/3.6.12",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.2.12) Gecko/20101027 Fedora/3.6.12-1.fc13 Firefox/3.6.12",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.2.12) Gecko/20101026 Firefox/3.6.12 ( .NET CLR 3.5.30729; .NET4.0E)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2.12) Gecko/20101026 Firefox/3.6.12 (.NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; .NET CLR 3.5.21022)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; ru; rv:1.9.2.11) Gecko/20101028 CentOS/3.6-2.el5.centos Firefox/3.6.11",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; ru; rv:1.9.2.11) Gecko/20101012 Firefox/3.6.11",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.9.2.11) Gecko/20101012 Firefox/3.6.11 ( .NET CLR 3.5.30729)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; pt-BR; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10 GTB7.1",\
        "Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10 GTB7.1",\
        "Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.2.10) Gecko/20100915 Ubuntu/10.04 (lucid) Firefox/3.6.10",\
        "Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.9.2.11) Gecko/20101013 Ubuntu/10.10 (maverick) Firefox/3.6.10",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.2.10) Gecko/20100915 Ubuntu/10.04 (lucid) Firefox/3.6.10",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ro; rv:1.9.2.10) Gecko/20100914 Firefox/3.6.10",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; fr; rv:1.9.2.10) Gecko/20100914 Firefox/3.6.10 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0(Windows; U; Windows NT 7.0; rv:1.9.2) Gecko/20100101 Firefox/3.6",\
        "Mozilla/5.0 (X11; U; x86_64 Linux; en_GB, en_US; rv:1.9.2) Gecko/20100115 Firefox/3.6",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2) Gecko/20100130 Gentoo Firefox/3.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100312 Ubuntu/9.04 (jaunty) Firefox/3.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2) Gecko/20100115 Ubuntu/10.04 (lucid) Firefox/3.6",\
        "Mozilla/5.0 (X11; Linux i686; rv:2.0) Gecko/20100101 Firefox/3.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru-RU; rv:1.9.2) Gecko/20100105 MRA 5.6 (build 03278) Firefox/3.6 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.3a3pre) Gecko/20100306 Firefox3.6 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.17) Gecko/20110420 Firefox/3.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ar; rv:1.9.2) Gecko/20100115 Firefox/3.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1b5pre) Gecko/20090517 Firefox/3.5b4pre (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1b4pre) Gecko/20090401 Firefox/3.5b4pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1b4) Gecko/20090423 Firefox/3.5b4 GTB5 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1b4) Gecko/20090423 Firefox/3.5b4 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1b4) Gecko/20090423 Firefox/3.5b4 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; fr; rv:1.9.1b4) Gecko/20090423 Firefox/3.5b4",\
        "Mozilla/5.0 (X11; U; Linux x86_64; it; rv:1.9.1.9) Gecko/20100402 Ubuntu/9.10 (karmic) Firefox/3.5.9 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.1.9) Gecko/20100317 SUSE/3.5.9-0.1.1 Firefox/3.5.9 GTB7.0",\
        "Mozilla/5.0 (X11; U; Linux x86_64; cs-CZ; rv:1.9.1.9) Gecko/20100317 SUSE/3.5.9-0.1.1 Firefox/3.5.9",\
        "Mozilla/5.0 (X11; U; Linux i686; hu-HU; rv:1.9.1.9) Gecko/20100330 Fedora/3.5.9-1.fc12 Firefox/3.5.9",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100401 Ubuntu/9.10 (karmic) Firefox/3.5.9 GTB7.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.4) Gecko/20091028 Ubuntu/9.10 (karmic) Firefox/3.5.9",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; hu; rv:1.9.1.9) Gecko/20100315 Firefox/3.5.9 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; et; rv:1.9.1.9) Gecko/20100315 Firefox/3.5.9",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; nl; rv:1.9.1.9) Gecko/20100315 Firefox/3.5.9 ( .NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; de; rv:1.9.2.13) Gecko/20101203 Firefox/3.5.9 (de)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; ru; rv:1.9.1.8) Gecko/20100216 Fedora/3.5.8-1.fc12 Firefox/3.5.8",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.8) Gecko/20100318 Gentoo Firefox/3.5.8",\
        "Mozilla/5.0 (X11; U; Linux i686; ja-JP; rv:1.9.1.8) Gecko/20100216 Fedora/3.5.8-1.fc12 Firefox/3.5.8",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.1.8) Gecko/20100214 Ubuntu/9.10 (karmic) Firefox/3.5.8",\
        "Mozilla/5.0 (X11; U; FreeBSD i386; ja-JP; rv:1.9.1.8) Gecko/20100305 Firefox/3.5.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.8) Gecko/20100202 Firefox/3.5.8 (.NET CLR 3.5.30729) FirePHP/0.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja; rv:1.9.1.8) Gecko/20100202 Firefox/3.5.8 GTB7.0 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2) Gecko/20100305 Gentoo Firefox/3.5.7",\
        "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.1.7) Gecko/20091222 SUSE/3.5.7-1.1.1 Firefox/3.5.7",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; de; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7 (.NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fa; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.1.6) Gecko/20091215 Ubuntu/9.10 (karmic) Firefox/3.5.6",\
        "Mozilla/5.0 (X11; U; Linux i686; zh-CN; rv:1.9.1.6) Gecko/20091216 Fedora/3.5.6-1.fc11 Firefox/3.5.6 GTB6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.6) Gecko/20100118 Gentoo Firefox/3.5.6",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.1.6) Gecko/20091215 Ubuntu/9.10 (karmic) Firefox/3.5.6 GTB7.0",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.1.6) Gecko/20091201 SUSE/3.5.6-1.1.1 Firefox/3.5.6",\
        "Mozilla/5.0 (X11; U; Linux i686; ca; rv:1.9.1.6) Gecko/20091215 Ubuntu/9.10 (karmic) Firefox/3.5.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 ( .NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 MRA 5.4 (build 02647) Firefox/3.5.6 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.6) Gecko/20091201 MRA 5.5 (build 02842) Firefox/3.5.6 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB6 (.NET CLR 3.5.30729) FBSMTWB",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.1.5) Gecko/20091109 Ubuntu/9.10 (karmic) Firefox/3.5.5",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091114 Gentoo Firefox/3.5.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; uk; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; ru; rv:1.9.1.5) Gecko/20091102 MRA 5.5 (build 02842) Firefox/3.5.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; zh-CN; rv:1.9.1.5) Gecko/Firefox/3.5.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.5) Gecko/20091102 MRA 5.5 (build 02842) Firefox/3.5.5",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; pl; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 FBSMTWB",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.4) Gecko/20091016 Firefox/3.5.4 (.NET CLR 3.5.30729) FBSMTWB",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU; rv:1.9.1.4) Gecko/20091016 Firefox/3.5.4 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.4) Gecko/20091007 Firefox/3.5.4",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.1.5) Gecko/20091109 Ubuntu/9.10 (karmic) Firefox/3.5.3pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.3) Gecko/20090912 Gentoo Firefox/3.5.3 FirePHP/0.3",\
        "Mozilla/5.0 (X11; U; FreeBSD i386; ru-RU; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; fr; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 ( .NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.5.3;MEGAUPLOAD 1.0 ( .NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; fi; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; bg; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ko; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.2) Gecko/20090803 Slackware Firefox/3.5.2",\
        "Mozilla/5.0 (X11; U; Linux i686; ru-RU; rv:1.9.1.2) Gecko/20090804 Firefox/3.5.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; pl; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2 GTB7.1 ( .NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; de; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; uk; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; es-ES; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.1.16) Gecko/20101130 AskTbMYC/3.9.1.14019 Firefox/3.5.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.16) Gecko/20101130 MRA 5.4 (build 02647) Firefox/3.5.16 ( .NET CLR 3.5.30729; .NET4.0C)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.16) Gecko/20101130 AskTbPLTV5/3.8.0.12304 Firefox/3.5.16 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.1.16) Gecko/20101130 Firefox/3.5.16 GTB7.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.9.1.15) Gecko/20101027 Fedora/3.5.15-1.fc12 Firefox/3.5.15",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.12) Gecko/2009070611 Firefox/3.5.12",\
        "Mozilla/5.0 (X11; U; Linux; en-US; rv:1.9.1.11) Gecko/20100720 Firefox/3.5.11",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR; rv:1.9.1.11) Gecko/20100701 Firefox/3.5.11 ( .NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.10) Gecko/20100504 Firefox/3.5.11 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.1.10) Gecko/20100504 Firefox/3.5.10 GTB7.0 ( .NET CLR 3.5.30729)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.3) Gecko/20100524 Firefox/3.5.1",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090716 Firefox/3.5.1",\
        "Mozilla/5.0 (X11; U; Linux x86; rv:1.9.1.1) Gecko/20090716 Linux Firefox/3.5.1",\
        "Mozilla/5.0 (X11; U; Linux i686; nl-NL; rv:1.9.0.19) Gecko/20090720 Firefox/3.5.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 GTB5",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.1.1) Gecko/20090714 SUSE/3.5.1-1.1 Firefox/3.5.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; tr; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 GTB5 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1) Gecko/20090630 Firefox/3.5 GTB6",\
        "Mozilla/5.0 (X11; U; Linux i686; it-IT; rv:1.9.0.2) Gecko/2008092313 Ubuntu/9.04 (jaunty) Firefox/3.5",\
        "Mozilla/5.0 (X11; U; Linux i686; fr-FR; rv:1.9.1) Gecko/20090624 Ubuntu/9.04 (jaunty) Firefox/3.5",\
        "Mozilla/5.0 (X11; U; Linux i686; en-us; rv:1.9.0.2) Gecko/2008092313 Ubuntu/9.04 (jaunty) Firefox/3.5",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.1) Gecko/20090624 Firefox/3.5",\
        "Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.9.1) Gecko/20090703 Firefox/3.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; pl; rv:1.9.1) Gecko/20090624 Firefox/3.5 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1) Gecko/20090612 Firefox/3.5 (.NET CLR 4.0.20506)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.1) Gecko/20090624 Firefox/3.5 (.NET CLR 4.0.20506)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-TW; rv:1.9.1) Gecko/20090624 Firefox/3.5 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1b3pre) Gecko/20090204 Firefox/3.1b3pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1b3) Gecko/20090312 Firefox/3.1b3",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3 GTB5 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; es-AR; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; de; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9.1b2pre) Gecko/20081026 Firefox/3.1b2pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1 ; x64; en-US; rv:1.9.1b2pre) Gecko/20081026 Firefox/3.1b2pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; de-AT; rv:1.9.1b2) Gecko/20081201 Firefox/3.1b2",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; it; rv:1.9.1b2) Gecko/20081201 Firefox/3.1b2",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; de-AT; rv:1.9.1b2) Gecko/20081201 Firefox/3.1b2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.9.1b2) Gecko/20081201 Firefox/3.1b2",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; fr; rv:1.9.1b1) Gecko/20081007 Firefox/3.1b1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.2) Gecko/2008092313 Ubuntu/8.04 (hardy) Firefox/3.1.6",\
        "Mozilla/4.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.7) Gecko/2008398325 Firefox/3.1.4",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.2) Gecko/2008092313 Ubuntu/8.04 (hardy) Firefox/3.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.6pre) Gecko/2009011606 Firefox/3.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.0.8) Gecko/2009032609 Firefox/3.07",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9pre) Gecko/2008040318 Firefox/3.0pre (Swiftfox)",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.9b5) Gecko/2008032620 Firefox/3.0b5",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9pre) Gecko/2008042312 Firefox/3.0b5",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9b5) Gecko/2008040514 Firefox/3.0b5",\
        "Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9b5) Gecko/2008032600 SUSE/2.9.95-25.1 Firefox/3.0b5",\
        "Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.9b5) Gecko/2008041514 Firefox/3.0b5",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.9b5) Gecko/2008041514 Firefox/3.0b5",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9b5) Gecko/2008041514 Firefox/3.0b5",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; de; rv:1.9b5) Gecko/2008032620 Firefox/3.0b5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; fr; rv:1.9b5) Gecko/2008032620 Firefox/3.0b5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.9b5) Gecko/2008032620 Firefox/3.0b5",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b4pre) Gecko/2008021714 Firefox/3.0b4pre (Swiftfox)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9b4pre) Gecko/2008020708 Firefox/3.0b4pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9b4) Gecko/2008040813 Firefox/3.0b4",\
        "Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9b4) Gecko/2008030800 SUSE/2.9.94-4.2 Firefox/3.0b4",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; pl; rv:1.9b4) Gecko/2008030714 Firefox/3.0b4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9b4) Gecko/2008030714 Firefox/3.0b4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; lt; rv:1.9b4) Gecko/2008030714 Firefox/3.0b4",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9b3pre) Gecko/2008020509 Firefox/3.0b3pre",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b3pre) Gecko/2008020507 Firefox/3.0b3pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9b3) Gecko/2008020514 Firefox/3.0b3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.9b3) Gecko/2008020514 Firefox/3.0b3",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b2) Gecko/2007121016 Firefox/3.0b2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.9b2) Gecko/2007121120 Firefox/3.0b2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9b1) Gecko/2007110703 Firefox/3.0b1",\
        "Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.9a2) Gecko/20080530 Firefox/3.0a2",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.9a1) Gecko/20061204 Firefox/3.0a1",\
        "Mozilla/6.0 (Windows; U; Windows NT 7.0; en-US; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.9 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; es-ES; rv:1.9.0.9) Gecko/2009042114 Ubuntu/9.04 (jaunty) Firefox/3.0.9",\
        "Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.9) Gecko/2009042114 Ubuntu/9.04 (jaunty) Firefox/3.0.9",\
        "Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.7) Gecko/2009030422 Kubuntu/8.10 (intrepid) Firefox/3.0.9",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.9.0.9) Gecko/2009042113 Ubuntu/8.04 (hardy) Firefox/3.0.9",\
        "Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.9.0.9) Gecko/2009042113 Ubuntu/9.04 (jaunty) Firefox/3.0.9",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.9) Gecko/2009042113 Linux Mint/6 (Felicia) Firefox/3.0.9",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.9) Gecko/2009040820 Firefox/3.0.9",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.0.9) Gecko/2009042113 Ubuntu/8.10 (intrepid) Firefox/3.0.9",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.0.9) Gecko/2009041500 SUSE/3.0.9-2.2 Firefox/3.0.9",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.0.4) Firefox/3.0.8)",\
        "Mozilla/6.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8",\
        "Mozilla/5.0 (X11; U; Linux x86_64; nb-NO; rv:1.9.0.8) Gecko/2009032600 SUSE/3.0.8-1.2 Firefox/3.0.8",\
        "Mozilla/5.0 (X11; U; Linux x86_64; it; rv:1.9.0.8) Gecko/2009032712 Ubuntu/8.10 (intrepid) Firefox/3.0.8",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.8) Gecko/2009040312 Gentoo Firefox/3.0.8",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.8) Gecko/2009032908 Gentoo Firefox/3.0.8",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.8) Gecko/2009032712 Ubuntu/8.10 (intrepid) Firefox/3.0.8",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.8) Gecko/2009032712 Firefox/3.0.8",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.8) Gecko/2009032600 SUSE/3.0.8-1.1 Firefox/3.0.8",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) Gecko Firefox/3.0.8",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.9.0.8) Gecko/2009032712 Ubuntu/8.10 (intrepid) Firefox/3.0.8",\
        "Mozilla/5.0 (X11; U; Mac OSX; it; rv:1.9.0.7) Gecko/2009030422 Firefox/3.0.7",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.0.7) Gecko/2009030423 Ubuntu/8.10 (intrepid) Firefox/3.0.7",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.7) Gecko/2009032606 Red Hat/3.0.7-1.el5 Firefox/3.0.7",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.7) Gecko/2009031802 Gentoo Firefox/3.0.7",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.7) Gecko/2009031120 Mandriva Firefox/3.0.7",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.7) Gecko/2009030516 Ubuntu/9.04 (jaunty) Firefox/3.0.7",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.9.0.7) Gecko/2009030503 Fedora/3.0.7-1.fc9 Firefox/3.0.7",\
        "Mozilla/5.0 (X11; U; Linux i686; zh-TW; rv:1.9.0.7) Gecko/2009030422 Ubuntu/8.04 (hardy) Firefox/3.0.7",\
        "Mozilla/5.0 (X11; U; Linux i686; hu-HU; rv:1.9.0.7) Gecko/2009030422 Ubuntu/8.10 (intrepid) Firefox/3.0.7 FirePHP/0.2.4",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.9.0.7) Gecko/2009030422 Ubuntu/8.10 (intrepid) Firefox/3.0.7",\
        "Mozilla/5.0 (X11; U; Linux; fr; rv:1.9.0.6) Gecko/2009011913 Firefox/3.0.6",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.6) Gecko/2009020519 Ubuntu/9.04 (jaunty) Firefox/3.0.6",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.16) Gecko/2009121609 Firefox/3.0.6 (Windows NT 5.1)",\
        "Mozilla/5.0 (X11; U; Linux i686; pl; rv:1.9.0.6) Gecko/2009011912 Firefox/3.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; eu; rv:1.9.0.6) Gecko/2009012700 SUSE/3.0.6-0.1.2 Firefox/3.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.6) Gecko/2009022714 Ubuntu/9.04 (jaunty) Firefox/3.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.6) Gecko/2009020911 Ubuntu/8.04 (hardy) Firefox/3.0.6 FirePHP/0.2.4",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.6) Gecko/2009020518 Ubuntu/9.04 (jaunty) Firefox/3.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.6) Gecko/2009012700 SUSE/3.0.6-0.1 Firefox/3.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.19) Gecko/2010072023 Firefox/3.0.6 (Debian-3.0.6-3)",\
        "Mozilla/5.0 (X11; U; x86_64 Linux; en_US; rv:1.9.0.5) Gecko/2008120121 Firefox/3.0.5",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.5) Gecko/2008122406 Gentoo Firefox/3.0.5",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.5) Gecko/2008122014 CentOS/3.0.5-1.el4.centos Firefox/3.0.5",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.5) Gecko/2008121806 Gentoo Firefox/3.0.5",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.9.0.5) Gecko/2008122010 Firefox/3.0.5",\
        "Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9.0.5) Gecko/2008121622 Ubuntu/8.10 (intrepid) Firefox/3.0.5",\
        "Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.5) Gecko/2008121300 SUSE/3.0.5-0.1 Firefox/3.0.5",\
        "Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.0.5) Gecko/2008121711 Ubuntu/9.04 (jaunty) Firefox/3.0.5",\
        "Mozilla/5.0 (X11; U; Linux i686; fi-FI; rv:1.9.0.5) Gecko/2008121622 Ubuntu/8.10 (intrepid) Firefox/3.0.5",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.5) Gecko/2008121914 Ubuntu/8.04 (hardy) Firefox/3.0.5",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.4pre) Gecko/2008101311 Firefox/3.0.4pre (Swiftfox)",\
        "Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.0.4) Gecko/2008111710 Firefox/3.0.4",\
        "Mozilla/5.0 (X11; U; Linux x86_64; es-AR; rv:1.9.0.4) Gecko/2008110510 Red Hat/3.0.4-1.el5_2 Firefox/3.0.4",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.4) Gecko/2008120512 Gentoo Firefox/3.0.4",\
        "Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.9.0.4) Gecko/2008111317 Ubuntu/8.04 (hardy) Firefox/3.0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; pt-BR; rv:1.9.0.4) Gecko/2008111317 Ubuntu/8.04 (hardy) Firefox/3.0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.4) Gecko/20081031100 SUSE/3.0.4-4.6 Firefox/3.0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; nl; rv:1.9.0.11) Gecko/2009060309 Ubuntu/8.04 (hardy) Firefox/3.0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.9.0.4) Gecko/2008111317 Ubuntu/8.04 (hardy) Firefox/3.0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.7) Gecko/2009032018 Firefox/3.0.4 (Debian-3.0.6-1)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.4) Gecko/2008111318 Ubuntu/8.10 (intrepid) Firefox/3.0.4",\
        "Mozilla/5.0 (X11; U; Linux x86_64; it; rv:1.9.0.3) Gecko/2008092813 Gentoo Firefox/3.0.3",\
        "Mozilla/5.0 (X11; U; Linux x86_64; es-AR; rv:1.9.0.3) Gecko/2008092515 Ubuntu/8.10 (intrepid) Firefox/3.0.3",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092510 Ubuntu/8.04 (hardy) Firefox/3.0.3 (Linux Mint)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.9.0.3) Gecko/2008092510 Ubuntu/8.04 (hardy) Firefox/3.0.3",\
        "Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.3) Gecko/2008090713 Firefox/3.0.3",\
        "Mozilla/5.0 (X11; U; Linux x64_64; es-AR; rv:1.9.0.3) Gecko/2008092515 Ubuntu/8.10 (intrepid) Firefox/3.0.3",\
        "Mozilla/5.0 (X11; U; Linux i686; zh-TW; rv:1.9.0.3) Gecko/2008092510 Ubuntu/8.04 (hardy) Firefox/3.0.3",\
        "Mozilla/5.0 (X11; U; Linux i686; pt-BR; rv:1.9.0.3) Gecko/2008092510 Ubuntu/8.04 (hardy) Firefox/3.0.3",\
        "Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.3) Gecko/2008092510 Ubuntu/8.04 (hardy) Firefox/3.0.3",\
        "Mozilla/5.0 (X11; U; Linux i686; ko-KR; rv:1.9.0.3) Gecko/2008092510 Ubuntu/8.04 (hardy) Firefox/3.0.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.0.2pre) Gecko/2008082305 Firefox/3.0.2pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.0.2) Gecko/2008092213 Ubuntu/8.04 (hardy) Firefox/3.0.2",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.2) Gecko/2008092318 Fedora/3.0.2-1.fc9 Firefox/3.0.2",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.9.0.2) Gecko/2008092213 Ubuntu/8.04 (hardy) Firefox/3.0.2",\
        "Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.0.2) Gecko/2008092313 Ubuntu/8.04 (hardy) Firefox/3.0.2",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.9.0.2) Gecko/2008092313 Ubuntu/8.04 (hardy) Firefox/3.0.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.2) Gecko/2008092809 Gentoo Firefox/3.0.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.2) Gecko/2008092318 Fedora/3.0.2-1.fc9 Firefox/3.0.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.2) Gecko/2008092313 Ubuntu/1.4.0 (hardy) Firefox/3.0.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.2) Gecko/2008091816 Red Hat/3.0.2-3.el5 Firefox/3.0.2",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.0.2) Gecko/2008092313 Ubuntu/8.04 (hardy) Firefox/3.0.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9) Gecko/2008052906 Firefox/3.0.1pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.0.19) Gecko/2010051407 CentOS/3.0.19-1.el5.centos Firefox/3.0.19",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-CN; rv:1.9.0.19) Gecko/2010031422 Firefox/3.0.19 ( .NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; cs; rv:1.9.0.19) Gecko/2010031422 Firefox/3.0.19",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.9.0.19) Gecko/2010031422 Firefox/3.0.19 ( .NET CLR 3.5.30729; .NET4.0C)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.9.0.18) Gecko/2010021501 Ubuntu/9.04 (jaunty) Firefox/3.0.18",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.0.18) Gecko/2010020400 SUSE/3.0.18-0.1.1 Firefox/3.0.18",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; it-IT; rv:1.9a1) Gecko/20100202 Firefox/3.0.18",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.17) Gecko/2010010604 Ubuntu/9.04 (jaunty) Firefox/3.0.17 FirePHP/0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; cs-CZ; rv:1.9.0.16) Gecko/2009121601 Ubuntu/9.04 (jaunty) Firefox/3.0.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; es-ES; rv:1.9.0.16) Gecko/2009120208 Firefox/3.0.16 FBSMTWB",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.16) Gecko/2009120208 Firefox/3.0.16 FBSMTWB",\
        "Mozilla/5.0 (X11; U; Linux x86_64; ru; rv:1.9.0.14) Gecko/2009090217 Ubuntu/9.04 (jaunty) Firefox/3.0.14 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; it; rv:1.9.0.14) Gecko/2009090216 Ubuntu/8.04 (hardy) Firefox/3.0.14",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fi-FI; rv:1.9.0.14) Gecko/2009090217 Firefox/3.0.14",\
        "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.14) Gecko/2009090216 Firefox/3.0.14",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.14) Gecko/2009091010 Firefox/3.0.14 (Debian-3.0.14-1)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.14) Gecko/2009090216 Ubuntu/9.04 (jaunty) Firefox/3.0.14 GTB5",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.0.14) Gecko/2009082505 Red Hat/3.0.14-1.el5_4 Firefox/3.0.14",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.14) Gecko/2009082707 Firefox/3.0.14 ( .NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR; rv:1.9.0.14) Gecko/2009082707 Firefox/3.0.14",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ; rv:1.9.0.14) Gecko/2009082707 Firefox/3.0.14",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.14) Gecko/2009090217 Ubuntu/9.04 (jaunty) Firefox/3.0.13",\
        "Mozilla/5.0 (X11; U; Linux i686; zh-TW; rv:1.9.0.13) Gecko/2009080315 Ubuntu/9.04 (jaunty) Firefox/3.0.13",\
        "Mozilla/5.0 (X11; U; Linux i686; fr-be; rv:1.9.0.8) Gecko/2009073022 Ubuntu/9.04 (jaunty) Firefox/3.0.13",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.13) Gecko/2009080315 Ubuntu/9.04 (jaunty) Firefox/3.0.13",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.0.13) Gecko/2009080315 Ubuntu/9.04 (jaunty) Firefox/3.0.13",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; de; rv:1.9.0.13) Gecko/2009073022 Firefox/3.0.13 (.NET CLR 4.0.20506)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ro; rv:1.9.0.13) Gecko/2009073022 Firefox/3.0.13 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.9.0.13) Gecko/2009073022 Firefox/3.0.13 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.13) Gecko/2009073022 Firefox/3.0.13 (.NET CLR 3.5.30729) FBSMTWB",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.13) Gecko/2009073022 Firefox/3.0.13 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; es-ES; rv:1.9.0.12) Gecko/2009070811 Ubuntu/9.04 (jaunty) Firefox/3.0.12",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.12) Gecko/2009070811 Ubuntu/9.04 (jaunty) Firefox/3.0.12",\
        "Mozilla/5.0 (X11; U; Linux ppc; en-GB; rv:1.9.0.12) Gecko/2009070818 Ubuntu/8.10 (intrepid) Firefox/3.0.12",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.12) Gecko/2009070818 Firefox/3.0.12",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.12) Gecko/2009070610 Firefox/3.0.12",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.0.12) Gecko/2009070811 Ubuntu/9.04 (jaunty) Firefox/3.0.12",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; ru; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 GTB5 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.11) Gecko/2009070612 Gentoo Firefox/3.0.11",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.11) Gecko/2009061118 Fedora/3.0.11-1.fc9 Firefox/3.0.11",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.9.0.11) Gecko/2009060308 Ubuntu/9.04 (jaunty) Firefox/3.0.11",\
        "Mozilla/5.0 (X11; U; Linux i686; nl; rv:1.9.0.11) Gecko/2009060308 Ubuntu/9.04 (jaunty) Firefox/3.0.11",\
        "Mozilla/5.0 (X11; U; Linux i686; it-IT; rv:1.9.0.11) Gecko/2009060308 Linux Mint/7 (Gloria) Firefox/3.0.11",\
        "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.11) Gecko/2009061118 Fedora/3.0.11-1.fc9 Firefox/3.0.11",\
        "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.11) Gecko/2009060309 Linux Mint/5 (Elyssa) Firefox/3.0.11",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060308 Linux Mint/7 (Gloria) Firefox/3.0.11",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.9.0.11) Gecko/2009060308 Ubuntu/9.04 (jaunty) Firefox/3.0.11 GTB5",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.0.11) Gecko/2009062218 Gentoo Firefox/3.0.11",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.9.0.10) Gecko/2009042523 Ubuntu/9.04 (jaunty) Firefox/3.0.10",\
        "Mozilla/5.0 (X11; U; Linux i686; tr-TR; rv:1.9.0.10) Gecko/2009042523 Ubuntu/9.04 (jaunty) Firefox/3.0.10",\
        "Mozilla/5.0 (X11; U; Linux i686; hu-HU; rv:1.9.0.10) Gecko/2009042718 CentOS/3.0.10-1.el5.centos Firefox/3.0.10",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.9.0.10) Gecko/2009042513 Ubuntu/8.04 (hardy) Firefox/3.0.10",\
        "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.10) Gecko/2009042513 Linux Mint/5 (Elyssa) Firefox/3.0.10",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.10) Gecko/2009042812 Gentoo Firefox/3.0.10",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.10) Gecko/2009042523 Ubuntu/8.10 (intrepid) Firefox/3.0.10",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.10) Gecko/2009042523 Linux Mint/6 (Felicia) Firefox/3.0.10",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.9.0.10) Gecko/2009042523 Ubuntu/8.10 (intrepid) Firefox/3.0.10",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.0.10) Gecko/2009042523 Ubuntu/9.04 (jaunty) Firefox/3.0.10",\
        "Mozilla/5.0 (X11; U; Linux x86_64; rv:1.9.0.1) Gecko/2008072820 Firefox/3.0.1",\
        "Mozilla/5.0 (X11; U; Linux x86_64; pl-PL; rv:1.9.0.1) Gecko/2008071222 Ubuntu (hardy) Firefox/3.0.1",\
        "Mozilla/5.0 (X11; U; Linux x86_64; ko-KR; rv:1.9.0.1) Gecko/2008071717 Firefox/3.0.1",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.0.1) Gecko/2008071222 Firefox/3.0.1",\
        "Mozilla/5.0 (X11; U; Linux x86_64; es-ES; rv:1.9.0.1) Gecko/2008072820 Firefox/3.0.1",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.1) Gecko/2008072820 Kubuntu/8.04 (hardy) Firefox/3.0.1",\
        "Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.1) Gecko/2008070400 SUSE/3.0.1-0.1 Firefox/3.0.1",\
        "Mozilla/5.0 (X11; U; Linux i686; rv:1.9) Gecko/20080810020329 Firefox/3.0.1",\
        "Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9.0.1) Gecko/2008070208 Firefox/3.0.1",\
        "Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.1) Gecko/2008071222 Firefox/3.0.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.1) Gecko/2008070208 Firefox/3.0.0",\
        "Mozilla/6.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:2.0.0.0) Gecko/20061028 Firefox/3.0",\
        "Mozilla/5.0 (X11; U; Linux x86_64; pl-PL; rv:1.9) Gecko/2008060309 Firefox/3.0",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9) Gecko/2008061017 Firefox/3.0",\
        "Mozilla/5.0 (X11; U; Linux x86_64; es-AR; rv:1.9) Gecko/2008061015 Ubuntu/8.04 (hardy) Firefox/3.0",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9) Gecko/2008062908 Firefox/3.0 (Debian-3.0~rc2-2)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9) Gecko/2008061317 (Gentoo) Firefox/3.0",\
        "Mozilla/5.0 (X11; U; Linux i686; tr-TR; rv:1.9.0) Gecko/2008061600 SUSE/3.0-1.2 Firefox/3.0",\
        "Mozilla/5.0 (X11; U; Linux i686; sk; rv:1.9) Gecko/2008061015 Firefox/3.0",\
        "Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9) Gecko/2008061812 Firefox/3.0",\
        "Mozilla/5.0 (X11; U; Linux i686; nl; rv:1.9) Gecko/2008061015 Firefox/3.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; de; rv:1.9.0.15) Gecko/2009101601 Firefox 2.1 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.8.1) Gecko/20060918 Firefox/2.0b2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.12) Gecko/20080208 Firefox/2.0b2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; pl; rv:1.8.1.1) Gecko/20061204 Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.8.1) Gecko/20060918 Firefox/2.0b2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1b2) Gecko/20060821 Firefox/2.0b2",\
        "Mozilla/5.0 (X11; U; Linux i686; pl; rv:1.8.1b1) Gecko/20060710 Firefox/2.0b1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.1b1) Gecko/20060710 Firefox/2.0b1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1b1) Gecko/20060707 Firefox/2.0b1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ca; rv:1.8.1b1) Gecko/20060710 Firefox/2.0b1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1b1) Gecko/20060710 Firefox/2.0b1",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1b1) Gecko/20060710 Firefox/2.0b1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; es-ES; rv:1.8) Gecko/20060321 Firefox/2.0a1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8) Gecko/20060322 Firefox/2.0a1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.16) Gecko/20080702 Firefox/2.0.9.9",\
        "Mozilla/5.0 (X11; U; SunOS sun4v; es-ES; rv:1.8.1.9) Gecko/20071127 Firefox/2.0.0.9",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.9) Gecko/20071025 Firefox/2.0.0.9",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.9) Gecko/20071105 Firefox/2.0.0.9",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.9) Gecko/20071103 Firefox/2.0.0.9 (Swiftfox)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.9) Gecko/20071025 FreeBSD/i386 Firefox/2.0.0.9",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.9) Gecko/20071025 Firefox/2.0.0.9",\
        "Mozilla/5.0 (Windows; Windows NT 5.1; en-US; rv:1.8.1.9) Gecko/20071025 Firefox/2.0.0.9",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; it; rv:1.8.1.9) Gecko/20071025 Firefox/2.0.0.9",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; da; rv:1.8.1.9) Gecko/20071025 Firefox/2.0.0.9",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.8.1.9) Gecko/20071025 Firefox/2.0.0.9",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.17pre) Gecko/20080715 Firefox/2.0.0.8pre",\
        "Mozilla/5.0 (X11; U; Windows NT i686; fr; rv:1.9.0.1) Gecko/2008070206 Firefox/2.0.0.8",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8) Gecko/20071022 Ubuntu/7.10 (gutsy) Firefox/2.0.0.8",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.12) Gecko/20080129 Firefox/2.0.0.8 (Debian-2.0.0.12-1)",\
        "Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.8.1.8) Gecko/20071022 Ubuntu/7.10 (gutsy) Firefox/2.0.0.8",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.9.0.1) Gecko/2008070206 Firefox/2.0.0.8",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.8.1.8) Gecko/20071022 Ubuntu/7.10 (gutsy) Firefox/2.0.0.8",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.8) Gecko/20071022 Firefox/2.0.0.8",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.8) Gecko/20071008 FreeBSD/i386 Firefox/2.0.0.8",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.8) Gecko/20061201 Firefox/2.0.0.8",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.1.8) Gecko/20071008 Ubuntu/7.10 (gutsy) Firefox/2.0.0.8",\
        "Mozilla/5.0 (X11; U; Linux x86_64; pl; rv:1.8.1.7) Gecko/20071009 Firefox/2.0.0.7",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.8.1.7) Gecko/20070914 Firefox/2.0.0.7",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.7) Gecko/20070923 Firefox/2.0.0.7 (Swiftfox)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.7) Gecko/20070914 Firefox/2.0.0.7 (Ubuntu-feisty)",\
        "Mozilla/5.0 (X11; U; Linux i386; en-US; rv:1.8.1.7) Gecko/20070914 Firefox/2.0.0.7",\
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:1.8.1.7) Gecko/20070914 Firefox/2.0.0.7",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; it-IT; rv:1.8.1.7) Gecko/20070914 Firefox/2.0.0.7",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en_US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.7",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.8.1.7) Gecko/20070914 Firefox/2.0.0.7",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; nl; rv:1.8.1.7) Gecko/20070914 Firefox/2.0.0.7",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; de-DE; rv:1.8.1.6) Gecko/20070805 Firefox/2.0.0.6",\
        "Mozilla/5.0 (X11; U; OpenBSD sparc64; en-US; rv:1.8.1.6) Gecko/20070816 Firefox/2.0.0.6",\
        "Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.8.1.6) Gecko/20070819 Firefox/2.0.0.6",\
        "Mozilla/5.0 (X11; U; OpenBSD i386; de-DE; rv:1.8.1.6) Gecko/20080429 Firefox/2.0.0.6",\
        "Mozilla/5.0 (X11; U; NetBSD sparc64; fr-FR; rv:1.8.1.6) Gecko/20070822 Firefox/2.0.0.6",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.6) Gecko/20061201 Firefox/2.0.0.6 (Ubuntu-feisty)",\
        "Mozilla/5.0 (X11; U; Linux x86; en-US; rv:1.8.1.6) Gecko/20061201 Firefox/2.0.0.6 (Ubuntu-feisty)",\
        "Mozilla/5.0 (X11; U; Linux i686; ja; rv:1.8.1.6) Gecko/20061201 Firefox/2.0.0.6 (Ubuntu-feisty)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.6) Gecko/20070831 Firefox/2.0.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.6) Gecko/20070804 Firefox/2.0.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; Ubuntu 7.04; de-CH; rv:1.8.1.5) Gecko/20070309 Firefox/2.0.0.5",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008100320 Firefox/2.0.0.5",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.5) Gecko/20070725 Firefox/2.0.0.5",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.5) Gecko/20070718 Fedora/2.0.0.5-1.fc7 Firefox/2.0.0.5",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.5) Gecko/20061201 Firefox/2.0.0.5 (Ubuntu-feisty)",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.8.1.5) Gecko/20060911 SUSE/2.0.0.5-1.2 Firefox/2.0.0.5",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-GB; rv:1.8.1.5) Gecko/20070718 Fedora/2.0.0.5-1.fc7 Firefox/2.0.0.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.8.1.5) Gecko/20070713 Firefox/2.0.0.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de; rv:1.8.1.5) Gecko/20070713 Firefox/2.0.0.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP; rv:1.8.1.5) Gecko/20070713 Firefox/2.0.0.5",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.8.1.4) Gecko/20070622 Firefox/2.0.0.4",\
        "Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.4) Gecko/20070622 Firefox/2.0.0.4",\
        "Mozilla/5.0 (X11; U; Linux x86_64; pl; rv:1.8.1.4) Gecko/20070611 Firefox/2.0.0.4",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.4) Gecko/20070604 Firefox/2.0.0.4",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.4) Gecko/20070515 Firefox/2.0.0.4",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.4) Gecko/20061201 Firefox/2.0.0.4 (Ubuntu-feisty)",\
        "Mozilla/5.0 (X11; U; Linux i686; it; rv:1.8.1.4) Gecko/20060601 Firefox/2.0.0.4 (Ubuntu-edgy)",\
        "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.4) Gecko/20061201 Firefox/2.0.0.4 (Ubuntu-feisty)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.4) Gecko/20070531 Firefox/2.0.0.4 (Swiftfox)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.4) Gecko/20070530 Fedora/2.0.0.4-1.fc7 Firefox/2.0.0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.3pre) Gecko/20070307 Firefox/2.0.0.3pre (Swiftfox)",\
        "Mozilla/5.0 (X11; U; SunOS sun4v; en-US; rv:1.8.1.3) Gecko/20070321 Firefox/2.0.0.3",\
        "Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.3) Gecko/20070423 Firefox/2.0.0.3",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.8.1.3) Gecko/20070322 Firefox/2.0.0.3",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.3) Gecko/20070415 Firefox/2.0.0.3",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.3) Gecko/20070322 Firefox/2.0.0.3",\
        "Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.3) Gecko/20070310 Firefox/2.0.0.3 (Debian-2.0.0.3-1)",\
        "Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.8.1.3) Gecko/20061201 Firefox/2.0.0.3 (Ubuntu-feisty)",\
        "Mozilla/5.0 (X11; U; Linux i686; nb-NO; rv:1.8.1.3) Gecko/20070310 Firefox/2.0.0.3 (Debian-2.0.0.3-1)",\
        "Mozilla/5.0 (X11; U; Linux i686; it; rv:1.8.1.3) Gecko/20070410 Firefox/2.0.0.3",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.8.1.3) Gecko/20070310 Firefox/2.0.0.3 (Debian-2.0.0.3-2)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; pl-PL; rv:1.8.1.2pre) Gecko/20061023 SUSE/2.0.0.1-0.1 Firefox/2.0.0.2pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070118 Firefox/2.0.0.2pre",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.22pre) Gecko/20090327 Ubuntu/7.10 (gutsy) Firefox/2.0.0.22pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.21",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.20",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.20",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.20",\
        "Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.8.1.20) Gecko/20090225 Firefox/2.0.0.20",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.20",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; ru; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.20",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.20 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; de; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.20 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.20 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.20",\
        "Mozilla/5.0 (X11; U; Linux; en-US; rv:1.8.1.2) Gecko/20070219 Firefox/2.0.0.2",\
        "Mozilla/5.0 (X11; U; Linux i686; sv-SE; rv:1.8.1.2) Gecko/20061023 SUSE/2.0.0.2-1.1 Firefox/2.0.0.2",\
        "Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.8.1.2) Gecko/20060601 Firefox/2.0.0.2 (Ubuntu-edgy)",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.8.1.2) Gecko/20060601 Firefox/2.0.0.2 (Ubuntu-edgy)",\
        "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.2) Gecko/20070220 Firefox/2.0.0.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.2) Gecko/20070220 Firefox/2.0.0.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.2) Gecko/20070314 Firefox/2.0.0.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.2) Gecko/20070225 Firefox/2.0.0.2 (Swiftfox)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.2) Gecko/20070220 Firefox/2.0.0.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.2) Gecko/20061201 Firefox/2.0.0.2",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.8.1.19) Gecko/20081216 Ubuntu/7.10 (gutsy) Firefox/2.0.0.19",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.19) Gecko/20081216 Fedora/2.0.0.19-1.fc8 Firefox/2.0.0.19 pango-text",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.8.1.19) Gecko/20081213 SUSE/2.0.0.19-0.1 Firefox/2.0.0.19",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.19",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.18) Gecko/20081113 Ubuntu/8.04 (hardy) Firefox/2.0.0.18",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.18) Gecko/20081113 Ubuntu/8.04 (hardy) Firefox/2.0.0.18",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.18) Gecko/20080921 SUSE/2.0.0.18-0.1 Firefox/2.0.0.18",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.18) Gecko/20081029 Firefox/2.0.0.18",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; es-ES; rv:1.8.1.18) Gecko/20081029 Firefox/2.0.0.18",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.4; en-US; rv:1.9.0.4) Gecko/20081029 Firefox/2.0.0.18",\
        "Mozilla/5.0 (X11; U; Linux i686; fr-FR; rv:1.8.1.17) Gecko/20080829 Firefox/2.0.0.17",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.17) Gecko/20080922 Ubuntu/7.10 (gutsy) Firefox/2.0.0.17",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.17) Gecko/20080829 Firefox/2.0.0.17",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.17) Gecko/20080829 Firefox/2.0.0.17",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.8.1.16) Gecko/20080702 Firefox/2.0.0.17",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.16) Gecko/20080702 Firefox/2.0.0.17",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; pl; rv:1.8.1.17) Gecko/20080829 Firefox/2.0.0.17",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr-FR; rv:1.8.1.17) Gecko/20080829 Firefox/2.0.0.17",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; fr; rv:1.8.1.17) Gecko/20080829 Firefox/2.0.0.17",\
        "Mozilla/5.0 (U; Windows NT 5.1; en-GB; rv:1.8.1.17) Gecko/20080808 Firefox/2.0.0.17",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.8.1.16) Gecko/20080715 Fedora/2.0.0.16-1.fc8 Firefox/2.0.0.16",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.16) Gecko/20080718 Ubuntu/8.04 (hardy) Firefox/2.0.0.16",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080718 Ubuntu/8.04 (hardy) Firefox/2.0.0.16",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080715 Firefox/2.0.0.16",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.1.16) Gecko/20080715 Ubuntu/7.10 (gutsy) Firefox/2.0.0.16",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.8.1.16) Gecko/20080718 Ubuntu/8.04 (hardy) Firefox/2.0.0.16",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.16) Gecko/20080716 Firefox/2.0.0.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.8.1.16) Gecko/20080702 Firefox/2.0.0.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; es-ES; rv:1.8.1.16) Gecko/20080702 Firefox/2.0.0.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.8.1.16) Gecko/20080702 Firefox/2.0.0.16",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.15) Gecko/20080702 Ubuntu/8.04 (hardy) Firefox/2.0.0.15",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; sv-SE; rv:1.8.1.15) Gecko/20080623 Firefox/2.0.0.15",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; sk; rv:1.8.1.15) Gecko/20080623 Firefox/2.0.0.15",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.1.15) Gecko/20080623 Firefox/2.0.0.15",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.8.1.14) Gecko/20080418 Firefox/2.0.0.14",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.6) Gecko/2010012717 Firefox/2.0.0.14",\
        "Mozilla/5.0 (X11; U; Linux i686; it; rv:1.8.1.14) Gecko/20080420 Firefox/2.0.0.14",\
        "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.14) Gecko/20080419 Ubuntu/8.04 (hardy) Firefox/2.0.0.14",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.14) Gecko/20080525 Firefox/2.0.0.14",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.14) Gecko/20080428 Firefox/2.0.0.14",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.14) Gecko/20080417 Firefox/2.0.0.14",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.14) Gecko/20080410 SUSE/2.0.0.14-0.4 Firefox/2.0.0.14",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.14) Gecko/20061201 Firefox/2.0.0.14 (Ubuntu-feisty)",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.8.1.14) Gecko/20080410 SUSE/2.0.0.14-0.1 Firefox/2.0.0.14",\
        "User-Agent:Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) Gecko/20080311 Firefox/2.0.0.13",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.13) Gecko/20080208 Mandriva/2.0.0.13-1mdv2008.1 (2008.1) Firefox/2.0.0.13",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.13) Gecko/20080325 Firefox/2.0.0.13",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.13) Gecko/20080316 SUSE/2.0.0.13-0.1 Firefox/2.0.0.13",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.8.1.13) Gecko/20080325 Ubuntu/7.10 (gutsy) Firefox/2.0.0.13",\
        "Mozilla/5.0 (X11; U; Linux i686 Gentoo; en-US; rv:1.8.1.13) Gecko/20080413 Firefox/2.0.0.13 (Gentoo Linux)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; de; rv:1.8.1.13) Gecko/20080311 Firefox/2.0.0.13",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1.13) Gecko/20080311 Firefox/2.0.0.13 (.NET CLR 3.0.04506.30)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; es-ES; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.13",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.1) Gecko/2008070208 Firefox/2.0.0.13",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1.12pre) Gecko/20080122 Firefox/2.0.0.12pre",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.8.1.12) Gecko/20080210 Firefox/2.0.0.12",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.12) Gecko/20080214 Firefox/2.0.0.12",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12",\
        "Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.8.1.12) Gecko/20080208 Fedora/2.0.0.12-1.fc8 Firefox/2.0.0.12",\
        "Mozilla/5.0 (X11; U; Linux x86; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/8.04 (hardy) Firefox/2.0.0.12",\
        "Mozilla/5.0 (X11; U; Linux i686; fr-FR; rv:1.8.1.6) Gecko/20080208 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12",\
        "Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.12) Gecko/20080208 Firefox/2.0.0.12",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.12) Gecko/20080201 Firefox/2.0.0.12 Mnenhy/0.7.5.666",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.1.12) Gecko/20080203 SUSE/2.0.0.12-2.1 Firefox/2.0.0.12",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.8.1.11) Gecko/20080118 Firefox/2.0.0.11",\
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-TW; rv:1.8.1.11) Gecko/20071204 Ubuntu/7.10 (gutsy) Firefox/2.0.0.11",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.11) Gecko/20071201 Firefox/2.0.0.11",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.11) Gecko/20070914 Mandriva/2.0.0.11-1.1mdv2008.0 (2008.0) Firefox/2.0.0.11",\
        "Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.8.1.11) Gecko/20071204 Ubuntu/7.10 (gutsy) Firefox/2.0.0.11",\
        "Mozilla/5.0 (X11; U; Linux i686; ja; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.8.1.8) Gecko/20071022 Ubuntu/7.10 (gutsy) Firefox/2.0.0.11",\
        "Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.1.11) Gecko/20071204 Ubuntu/7.10 (gutsy) Firefox/2.0.0.11",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.11) Gecko/20080201 Firefox/2.0.0.11",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.11) Gecko/20071204 Ubuntu/7.10 (gutsy) Firefox/2.0.0.11",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.10) Gecko/20061201 Firefox/2.0.0.10 (Ubuntu-feisty)",\
        "Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.8.1.10) Gecko/20071128 Fedora/2.0.0.10-2.fc7 Firefox/2.0.0.10",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.17) Gecko/20080827 Firefox/2.0.0.10 (Debian-2.0.0.17-0etch1)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.10) Gecko/20071203 Ubuntu/7.10 (gutsy) Firefox/2.0.0.10",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.10) Gecko/20071126 Ubuntu/7.10 (gutsy) Firefox/2.0.0.10",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.10) Gecko/20071115 Firefox/2.0.0.10",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.10) Gecko/20061201 Firefox/2.0.0.10 (Ubuntu-feisty)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.1.10) Gecko/20071126 Ubuntu/7.10 (gutsy) Firefox/2.0.0.10",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.10) Gecko/20071115 Firefox/2.0.0.10",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.10) Gecko/20071015 SUSE/2.0.0.10-0.1 Firefox/2.0.0.10",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.8.1.1) Gecko/20060601 Firefox/2.0.0.1 (Ubuntu-edgy)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.1) Gecko/20060601 Firefox/2.0.0.1 (Ubuntu-edgy)",\
        "Mozilla/5.0 (X11; U; Linux i686; pl; rv:1.8.1.1) Gecko/20061204 Firefox/2.0.0.1 (Ubuntu-edgy)",\
        "Mozilla/5.0 (X11; U; Linux i686; hu; rv:1.8.1.1) Gecko/20061208 Firefox/2.0.0.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.3) Gecko/20061201 Firefox/2.0.0.1 (Ubuntu-feisty)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20070110 Firefox/2.0.0.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061208 Firefox/2.0.0.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Firefox/2.0.0.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.1.2pre) Gecko/20061023 Firefox/2.0.0.1",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.8.1.1) Gecko/20061220 Firefox/2.0.0.1 (Swiftfox)",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; de-DE; rv:1.9.1b4) Gecko/20090428 Firefox/2.0.0.0",\
        "Mozilla/5.0 (X11; Linux i686; U; pl; rv:1.8.1) Gecko/20061208 Firefox/2.0.0",\
        "Mozilla/5.0 (Windows NT 6.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0",\
        "Mozilla/5.0 (Windows NT 6.0; U; sv; rv:1.8.1) Gecko/20061208 Firefox/2.0.0",\
        "Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0",\
        "Mozilla/5.0 (X11;U;Linux i686;en-US;rv:1.8.1) Gecko/2006101022 Firefox/2.0",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0",\
        "Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1) Gecko/20061128 Firefox/2.0",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1) Gecko/20061023 SUSE/2.0-37 Firefox/2.0",\
        "Mozilla/5.0 (X11; U; Linux x86-64; en-US; rv:1.8.1) Gecko/20061010 Firefox/2.0",\
        "Mozilla/5.0 (X11; U; Linux i686; tr-TR; rv:1.8.1) Gecko/20061023 SUSE/2.0-30 Firefox/2.0",\
        "Mozilla/5.0 (X11; U; Linux i686; pl; rv:1.8.1) Gecko/20061127 Firefox/2.0",\
        "Mozilla/5.0 (X11; U; Linux i686; pl; rv:1.8.1) Gecko/20061010 Firefox/2.0 Ubuntu",\
        "Mozilla/5.0 (X11; U; Linux i686; pl; rv:1.8.1) Gecko/20061003 Firefox/2.0 Ubuntu",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; ; rv:1.8.0.7) Gecko/20060917 Firefox/1.9.0.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; ; rv:1.8.0.1) Gecko/20060111 Firefox/1.9.0",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a1) Gecko/20060217 Firefox/1.6a1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a1) Gecko/20051215 Firefox/1.6a1 (Swiftfox)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2 x64; en-US; rv:1.9a1) Gecko/20060214 Firefox/1.6a1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a1) Gecko/20060121 Firefox/1.6a1",\
        "Mozilla/5.0 (Windows NT 5.1; rv:1.9a1) Gecko/20060217 Firefox/1.6a1",\
        "Mozilla/5.0 (X11; U; OpenBSD amd64; en-US; rv:1.8.0.9) Gecko/20070101 Firefox/1.5.0.9",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.9) Gecko/20071025 Firefox/1.5.0.9 (Debian-2.0.0.9-2)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.9) Gecko/20070126 Ubuntu/dapper-security Firefox/1.5.0.9",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.9) Gecko/20061221 Fedora/1.5.0.9-1.fc5 Firefox/1.5.0.9",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.9) Gecko/20061215 Red Hat/1.5.0.9-0.1.el4 Firefox/1.5.0.9",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.9) Gecko/20060911 SUSE/1.5.0.9-0.2 Firefox/1.5.0.9",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.8.0.9) Gecko/20061206 Firefox/1.5.0.9",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.0.9) Gecko/20061206 Firefox/1.5.0.9",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR; rv:1.8.0.9) Gecko/20061206 Firefox/1.5.0.9",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja; rv:1.8.0.9) Gecko/20061206 Firefox/1.5.0.9",\
        "Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.8.0.8) Gecko/20061110 Firefox/1.5.0.8",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.8.0.8) Gecko/20061213 Firefox/1.5.0.8",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.8) Gecko/20061110 Firefox/1.5.0.8",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.8) Gecko/20061025 Firefox/1.5.0.8",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.8) Gecko/20060802 Mandriva/1.5.0.8-1.1mdv2007.0 (2007.0) Firefox/1.5.0.8",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.8.0.8) Gecko/20061115 Ubuntu/dapper-security Firefox/1.5.0.8",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.8.0.8) Gecko/20060911 SUSE/1.5.0.8-0.2 Firefox/1.5.0.8",\
        "Mozilla/5.0 (X11; U; Linux Gentoo i686; pl; rv:1.8.0.8) Gecko/20061219 Firefox/1.5.0.8",\
        "Mozilla/5.0 (X11; U; FreeBSD amd64; en-US; rv:1.8.0.8) Gecko/20061116 Firefox/1.5.0.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.8) Gecko/20061025 Firefox/1.5.0.8",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.8.0.7) Gecko/20060915 Firefox/1.5.0.7",\
        "Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.8.0.7) Gecko/20060920 Firefox/1.5.0.7",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.0.7) Gecko/20060924 Firefox/1.5.0.7",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.0.7) Gecko/20060919 Firefox/1.5.0.7",\
        "Mozilla/5.0 (X11; U; Linux i686; sk; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7",\
        "Mozilla/5.0 (X11; U; Linux i686; pl; rv:1.8.0.7) Gecko/20060914 Firefox/1.5.0.7 (Swiftfox)",\
        "Mozilla/5.0 (X11; U; Linux i686; ko-KR; rv:1.8.0.7) Gecko/20060913 Fedora/1.5.0.7-1.fc5 Firefox/1.5.0.7 pango-text",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.8.0.7) Gecko/20060921 Ubuntu/dapper-security Firefox/1.5.0.7",\
        "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.0.7) Gecko/20060830 Firefox/1.5.0.7 (Debian-1.5.dfsg+1.5.0.7-1~bpo.1)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-ZW; rv:1.8.0.7) Gecko/20061018 Firefox/1.5.0.7",\
        "Mozilla/5.0 (X11; U; Linux i686; pt-BR; rv:1.8.0.6) Gecko/20060728 Firefox/1.5.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.8.0.6) Gecko/20060728 Firefox/1.5.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.6) Gecko/20060808 Fedora/1.5.0.6-2.fc5 Firefox/1.5.0.6 pango-text",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.6) Gecko/20060803 Firefox/1.5.0.6 (Swiftfox)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.6) Gecko/20060728 SUSE/1.5.0.6-0.1 Firefox/1.5.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.6) Gecko/20060728 Firefox/1.5.0.6 (Debian-1.5.dfsg+1.5.0.6-1)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.0.6) Gecko/20060808 Fedora/1.5.0.6-2.fc5 Firefox/1.5.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); zh-TW; rv:1.8.0.6) Gecko/20060728 Firefox/1.5.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.0.6) Gecko/20060728 SUSE/1.5.0.6-1.2 Firefox/1.5.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); de; rv:1.8.0.6) Gecko/20060728 SUSE/1.5.0.6-1.3 Firefox/1.5.0.6",\
        "Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.0.5) Gecko/20060728 Firefox/1.5.0.5",\
        "Mozilla/5.0 (X11; U; NetBSD i386; en-US; rv:1.8.0.5) Gecko/20060818 Firefox/1.5.0.5",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.0.5) Gecko/20060731 Ubuntu/dapper-security Firefox/1.5.0.5",\
        "Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.8.0.5) Gecko/20060731 Ubuntu/dapper-security Firefox/1.5.0.5 Mnenhy/0.7.4.666",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.5) Gecko/20060831 Firefox/1.5.0.5",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.5) Gecko/20060813 Firefox/1.5.0.5",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.5) Gecko/20060806 Firefox/1.5.0.5",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.5) Gecko/20060801 Firefox/1.5.0.5",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.5) Gecko/20060719 Firefox/1.5.0.5",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.8.0.5) Gecko/20060731 Ubuntu/dapper-security Firefox/1.5.0.5",\
        "Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.8.0.4) Gecko/20060628 Firefox/1.5.0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.8.0.4) Gecko/20060508 Firefox/1.5.0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; pl; rv:1.8.0.4) Gecko/20060614 Fedora/1.5.0.4-1.2.fc5 Firefox/1.5.0.4 pango-text Mnenhy/0.7.4.0",\
        "Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.8.0.4) Gecko/20060608 Ubuntu/dapper-security Firefox/1.5.0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.0.4) Gecko/20060608 Ubuntu/dapper-security Firefox/1.5.0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.4) Gecko/20060716 Firefox/1.5.0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.4) Gecko/20060704 Firefox/1.5.0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.4) Gecko/20060614 Fedora/1.5.0.4-1.2.fc5 Firefox/1.5.0.4 pango-text",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.4) Gecko/20060608 Ubuntu/dapper-security Firefox/1.5.0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.4) Gecko/20060508 Firefox/1.5.0.4",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.0.3) Gecko/20060523 Ubuntu/dapper Firefox/1.5.0.3",\
        "Mozilla/5.0 (X11; U; Linux i686; pt-BR; rv:1.8.0.3) Gecko/20060523 Ubuntu/dapper Firefox/1.5.0.3",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.3) Gecko/20060504 Fedora/1.5.0.3-1.1.fc5 Firefox/1.5.0.3 pango-text",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.3) Gecko/20060425 SUSE/1.5.0.3-7 Firefox/1.5.0.3",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.8.0.3) Gecko/20060425 SUSE/1.5.0.3-7 Firefox/1.5.0.3",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3",\
        "Mozilla/5.0 (Windows; U; Win 9x 4.90; en-US; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 4.0; en-US; rv:1.8.0.2) Gecko/20060418 Firefox/1.5.0.2;",\
        "Mozilla/5.0 (X11; U; OpenBSD sparc64; en-CA; rv:1.8.0.2) Gecko/20060429 Firefox/1.5.0.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.2) Gecko/20060419 Fedora/1.5.0.2-1.2.fc5 Firefox/1.5.0.2 pango-text",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.2) Gecko Firefox/1.5.0.2",\
        "Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.8.0.2) Gecko/20060414 Firefox/1.5.0.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-TW; rv:1.8.0.2) Gecko/20060308 Firefox/1.5.0.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR; rv:1.8.0.2) Gecko/20060308 Firefox/1.5.0.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.0.2) Gecko/20060308 Firefox/1.5.0.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; es-ES; rv:1.8.0.2) Gecko/20060308 Firefox/1.5.0.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.2) Gecko/20060406 Firefox/1.5.0.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.2) Gecko/20060308 Firefox/1.5.0.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.13pre) Gecko/20080207 Ubuntu/dapper-security Firefox/1.5.0.13pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.0.12) Gecko/20070718 Red Hat/1.5.0.12-3.el5 Firefox/1.5.0.12",\
        "Mozilla/5.0 (X11; U; Linux i686; pl; rv:1.8.0.12) Gecko/20070508 Firefox/1.5.0.12",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20071126 Fedora/1.5.0.12-7.fc6 Firefox/1.5.0.12",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070530 Fedora/1.5.0.12-1.fc6 Firefox/1.5.0.12",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.0.12) Gecko/20070718 Fedora/1.5.0.12-4.fc6 Firefox/1.5.0.12",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.8.0.12) Gecko/20070719 CentOS/1.5.0.12-3.el5.centos Firefox/1.5.0.12",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.8.0.12) Gecko/20070508 Firefox/1.5.0.12",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; sv-SE; rv:1.8.0.12) Gecko/20070508 Firefox/1.5.0.12",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ko; rv:1.8.0.12) Gecko/20070508 Firefox/1.5.0.12",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.11) Gecko/20070312 Firefox/1.5.0.11",\
        "Mozilla/5.0 (X11; U; Linux i686; cs-CZ; rv:1.8.0.11) Gecko/20070327 Ubuntu/dapper-security Firefox/1.5.0.11",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; pl; rv:1.8.0.11) Gecko/20070312 Firefox/1.5.0.11",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.0.11) Gecko/20070312 Firefox/1.5.0.11",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.0.11) Gecko/20070312 Firefox/1.5.0.11",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; es-ES; rv:1.8.0.11) Gecko/20070312 Firefox/1.5.0.11",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.11) Gecko/20070312 Firefox/1.5.0.11",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; it; rv:1.8.0.11) Gecko/20070312 Firefox/1.5.0.11",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.11) Gecko/20070312 Firefox/1.5.0.11",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de; rv:1.8.0.11) Gecko/20070312 Firefox/1.5.0.11",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.10pre) Gecko/20070211 Firefox/1.5.0.10pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.0.10) Gecko/20070409 CentOS/1.5.0.10-2.el5.centos Firefox/1.5.0.10",\
        "Mozilla/5.0 (X11; U; Linux i686; ja; rv:1.8.0.10) Gecko/20070510 Fedora/1.5.0.10-6.fc6 Firefox/1.5.0.10",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.10) Gecko/20070510 Fedora/1.5.0.10-6.fc6 Firefox/1.5.0.10",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.10) Gecko/20070302 Ubuntu/dapper-security Firefox/1.5.0.10",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.10) Gecko/20070226 Fedora/1.5.0.10-1.fc6 Firefox/1.5.0.10 pango-text",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.10) Gecko/20070221 Red Hat/1.5.0.10-0.1.el4 Firefox/1.5.0.10",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.10) Gecko/20060911 SUSE/1.5.0.10-0.2 Firefox/1.5.0.10",\
        "Mozilla/5.0 (X11; U; Linux i686; cs-CZ; rv:1.8.0.10) Gecko/20070313 Fedora/1.5.0.10-5.fc6 Firefox/1.5.0.10",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; sv-SE; rv:1.8.0.10) Gecko/20070216 Firefox/1.5.0.10",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.0.10) Gecko/20070216 Firefox/1.5.0.10",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.8.0.1) Gecko/20060206 Firefox/1.5.0.1",\
        "Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.8.0.1) Gecko/20060213 Firefox/1.5.0.1",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.0.1) Gecko/20060313 Fedora/1.5.0.1-9 Firefox/1.5.0.1 pango-text",\
        "Mozilla/5.0 (X11; U; Linux i686; pl; rv:1.8.0.1) Gecko/20060313 Fedora/1.5.0.1-9 Firefox/1.5.0.1 pango-text Mnenhy/0.7.3.0",\
        "Mozilla/5.0 (X11; U; Linux i686; pl; rv:1.8.0.1) Gecko/20060124 Firefox/1.5.0.1 Ubuntu",\
        "Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.8.0.1) Gecko/20060313 Fedora/1.5.0.1-9 Firefox/1.5.0.1 pango-text Mnenhy/0.7.3.0",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.8.0.1) Gecko/20060124 Firefox/1.5.0.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060911 Red Hat/1.5.0.7-0.1.el4 Firefox/1.5.0.1 pango-text",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060324 Ubuntu/dapper Firefox/1.5.0.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060313 Debian/1.5.dfsg+1.5.0.1-4 Firefox/1.5.0.1",\
        "Mozilla/5.0 (Windows NT 5.2; U; de; rv:1.8.0) Gecko/20060728 Firefox/1.5.0",\
        "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.0) Gecko/20060728 Firefox/1.5.0",\
        "Mozilla/5.0 (Windows 98; U; en; rv:1.8.0) Gecko/20060728 Firefox/1.5.0",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.8) Gecko/20051130 Firefox/1.5",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.8) Gecko/20051231 Firefox/1.5",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8) Gecko/20051201 Firefox/1.5",\
        "Mozilla/5.0 (X11; U; Linux i686; pl; rv:1.8) Gecko/20051111 Firefox/1.5 Ubuntu",\
        "Mozilla/5.0 (X11; U; Linux i686; lt; rv:1.6) Gecko/20051114 Firefox/1.5",\
        "Mozilla/5.0 (X11; U; Linux i686; it; rv:1.8) Gecko/20060113 Firefox/1.5",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.8) Gecko/20051111 Firefox/1.5",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8) Gecko/20060806 Firefox/1.5",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8) Gecko/20060119 Debian/1.5.dfsg-4ubuntu3 Firefox/1.5",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8) Gecko/20060111 Firefox/1.5",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8b5) Gecko/20051008 Fedora/1.5-0.5.0.beta2 Firefox/1.4.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8b5) Gecko/20051006 Firefox/1.4.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8b5) Gecko/20051006 Firefox/1.4.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8b5) Gecko/20051006 Firefox/1.4.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8b4) Gecko/20050908 Firefox/1.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.21) Gecko/20090403 Firefox/1.1.16",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.13) Gecko/20060411 Firefox/1.0.8 SUSE/1.0.8-0.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.7.13) Gecko/20060418 Fedora/1.0.8-1.1.fc4 Firefox/1.0.8",\
        "Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:1.7.13) Gecko/20060411 Firefox/1.0.8 SUSE/1.0.8-0.2",\
        "Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.7.12) Gecko/20051105 Firefox/1.0.8",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.7.13) Gecko/20060410 Firefox/1.0.8",\
        "Mozilla/5.0 (X11; U; x86_64 Linux; en_US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.7.12) Gecko/20050922 Firefox/1.0.7",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.7.12) Gecko/20050922 Fedora/1.0.7-1.1.fc4 Firefox/1.0.7",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.7.12) Gecko/20051218 Firefox/1.0.7",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.7.12) Gecko/20051010 Firefox/1.0.7 (Ubuntu package 1.0.7)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.7.12) Gecko/20050922 Fedora/1.0.7-1.1.fc4 Firefox/1.0.7",\
        "Mozilla/5.0 (X11; U; Linux ppc; da-DK; rv:1.7.12) Gecko/20051010 Firefox/1.0.7 (Ubuntu package 1.0.7)",\
        "Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.7.12) Gecko/20051010 Firefox/1.0.7 (Ubuntu package 1.0.7)",\
        "Mozilla/5.0 (X11; U; Linux i686; hu-HU; rv:1.7.12) Gecko/20051010 Firefox/1.0.7 (Ubuntu package 1.0.7)",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.7.12) Gecko/20050922 Firefox/1.0.7 (Debian package 1.0.7-1)",\
        "Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.7.10) Gecko/20050919 (No IDN) Firefox/1.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; pt-BR; rv:1.7.10) Gecko/20050717 Firefox/1.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.7.10) Gecko/20050717 Firefox/1.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; fr-FR; rv:1.7.10) Gecko/20050716 Firefox/1.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.10) Gecko/20051106 Firefox/1.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.10) Gecko/20050918 Firefox/1.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.10) Gecko/20050815 Firefox/1.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.10) Gecko/20050721 Firefox/1.0.6 (Ubuntu package 1.0.6)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.10) Gecko/20050720 Fedora/1.0.6-1.1.fc3 Firefox/1.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.10) Gecko/20050716 Firefox/1.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.9) Gecko/20050711 Firefox/1.0.5",\
        "Mozilla/5.0 (Windows; U; Windows NT5.1; en; rv:1.7.10) Gecko/20050716 Firefox/1.0.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en; rv:1.7.10) Gecko/20050716 Firefox/1.0.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.9) Gecko/20050711 Firefox/1.0.5",\
        "Mozilla/5.0 (Windows; U; Win 9x 4.90; en-US; rv:1.7.9) Gecko/20050711 Firefox/1.0.5",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.7.8) Gecko/20050512 Firefox/1.0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.7.8) Gecko/20050524 Fedora/1.0.4-4 Firefox/1.0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; fr-FR; rv:1.7.8) Gecko/20050511 Firefox/1.0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.8) Gecko/20050610 Firefox/1.0.4 (Debian package 1.0.4-3)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.8) Gecko/20050523 Firefox/1.0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.8) Gecko/20050513 Firefox/1.0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.8) Gecko/20050512 Firefox/1.0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.8) Gecko/20050511 Firefox/1.0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.10) Gecko/20070530 Firefox/1.0.4 (Debian package 1.0.4-2sarge17)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.10) Gecko/20061113 Firefox/1.0.4 (Debian package 1.0.4-2sarge13)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.7) Gecko/20050421 Firefox/1.0.3 (Debian package 1.0.3-2)",\
        "Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.7.7) Gecko/20060303 Firefox/1.0.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU; rv:1.7.7) Gecko/20050414 Firefox/1.0.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr-FR; rv:1.7.7) Gecko/20050414 Firefox/1.0.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.7) Gecko/20050414 Firefox/1.0.3 (ax)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.7.7) Gecko/20050414 Firefox/1.0.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; da-DK; rv:1.7.7) Gecko/20050414 Firefox/1.0.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7.7) Gecko/20050414 Firefox/1.0.3",\
        "Mozilla/5.0 (Windows; U; Win98; fr-FR; rv:1.7.7) Gecko/20050414 Firefox/1.0.3",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.7.7) Gecko/20050414 Firefox/1.0.3",\
        "Mozilla/5.0 (X11; U; Linux x86_64; nl-NL; rv:1.7.6) Gecko/20050318 Firefox/1.0.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.6) Gecko/20050317 Firefox/1.0.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-DE; rv:1.7.6) Gecko/20050321 Firefox/1.0.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; sv-SE; rv:1.7.6) Gecko/20050318 Firefox/1.0.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; nl-NL; rv:1.7.6) Gecko/20050318 Firefox/1.0.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr-FR; rv:1.7.6) Gecko/20050318 Firefox/1.0.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.6) Gecko/20050317 Firefox/1.0.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.7.6) Gecko/20050321 Firefox/1.0.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-GB; rv:1.7.6) Gecko/20050321 Firefox/1.0.2",\
        "Mozilla/5.0 (Windows; U; Win98; fr-FR; rv:1.7.6) Gecko/20050318 Firefox/1.0.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.6) Gecko/20050317 Firefox/1.0.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.6) Gecko/20050310 Firefox/1.0.1",\
        "Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:1.7.6) Gecko/20050322 Firefox/1.0.1",\
        "Mozilla/5.0 (X11; U; Linux i686; cs-CZ; rv:1.7.6) Gecko/20050226 Firefox/1.0.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr-FR; rv:1.7.6) Gecko/20050226 Firefox/1.0.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.6) Gecko/20050223 Firefox/1.0.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.7.6) Gecko/20050226 Firefox/1.0.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7.6) Gecko/20050225 Firefox/1.0.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:1.7.6) Gecko/20050223 Firefox/1.0.1",\
        "Mozilla/5.0 (Windows; U; Win98; fr-FR; rv:1.7.6) Gecko/20050226 Firefox/1.0.1",\
        "Mozilla/5.0 (X11; U; Linux i686; hu; rv:1.8b4) Gecko/20050827 Firefox/1.0+",\
        "Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.7.5) Gecko/20041109 Firefox/1.0",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.6) Gecko/20050405 Firefox/1.0 (Ubuntu package 1.0.2)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.5) Gecko/20050221 Firefox/1.0",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.5) Gecko/20041218 Firefox/1.0",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.5) Gecko/20041204 Firefox/1.0 (Debian package 1.0.x.2-1)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.5) Gecko/20041117 Firefox/1.0 (Debian package 1.0-2.0.0.45.linspire0.4)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.7.6) Gecko/20050405 Firefox/1.0 (Ubuntu package 1.0.2)",\
        "Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.7.5) Gecko/20041128 Firefox/1.0 (Debian package 1.0-4)",\
        "Mozilla/5.0 (X11; Linux i686; rv:1.7.5) Gecko/20041108 Firefox/1.0",\
        "Mozilla/5.0 (Windows; U; WinNT4.0; de-DE; rv:1.7.5) Gecko/20041108 Firefox/1.0",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7) Gecko/20040917 Firefox/0.9.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7) Gecko/20040803 Firefox/0.9.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7) Gecko/20040803 Firefox/0.9.3",\
        "Mozilla/5.0 (Windows; U; Win98; de-DE; rv:1.7) Gecko/20040803 Firefox/0.9.3",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7) Gecko/20040802 Firefox/0.9.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7) Gecko/20040707 Firefox/0.9.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7) Gecko/20040630 Firefox/0.9.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:1.7) Gecko/20040626 Firefox/0.9.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.7) Gecko/20040614 Firefox/0.9",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040225 Firefox/0.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.6) Gecko/20040206 Firefox/0.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.6) Gecko/20040206 Firefox/0.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:1.6) Gecko/20040206 Firefox/0.8",\
        "Mozilla/5.0 (Windows; U; Win 9x 4.90; en-US; rv:1.6) Gecko/20040206 Firefox/0.8",\
        "Mozilla/5.0 (X11; U; Linux i686; rv:1.7.3) Gecko/20041020 Firefox/0.10.1",\
        "Mozilla/5.0 (X11; U; Linux i686; rv:1.7.3) Gecko/20040914 Firefox/0.10.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; rv:1.7.3) Gecko/20041001 Firefox/0.10.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; rv:1.7.3) Gecko/20040911 Firefox/0.10.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; rv:1.7.3) Gecko/20040913 Firefox/0.10.1",\
        "Mozilla/5.0 (X11; U; Linux i686; rv:1.7.3) Gecko/20040914 Firefox/0.10",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; rv:1.7.3) Gecko/20040913 Firefox/0.10",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; rv:1.7.3) Gecko/20040913 Firefox/0.10",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; rv:1.7.3) Gecko/20040913 Firefox/0.10",\
        "Mozilla/5.0 (X11; U; Gentoo Linux x86_64; pl-PL) Gecko Firefox",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.6) Gecko/2009011913 Firefox",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; rv:1.8.1.16) Gecko/20080702 Firefox",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:2.0) Treco/20110515 Fireweb Navigator/2.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Flock/3.5.2.4599 Chrome/7.0.517.442 Safari/534.7",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Flock/3.5.0.4568 Chrome/7.0.517.440 Safari/534.7",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.19) Gecko/2010061201 Firefox/3.0.19 Flock/2.6.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.0.16) Gecko/2010021003 Firefox/3.0.16 Flock/2.5.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.7) Gecko/20091221 AppleWebKit/531.21.8 KHTML/4.3.5 (like Gecko) Firefox/3.5.7 Flock/2.5.6 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.7) Gecko/20091221 AppleWebKit/531.21.8 (KHTML, like Gecko) Firefox/3.5.7 Flock/2.5.6 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.0.16) Gecko/2010010314 Firefox/3.0.16 Flock/2.5.6",\
        "Mozilla/5.0 (X11; U; Linux x86_64; es-AR; rv:1.9.0.2) Gecko/2008091920 Firefox/3.0.2 Flock/2.0b3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.2) Gecko/2008083108 Firefox/3.0.2 Flock/2.0b3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.1) Gecko/2008071523 Firefox/3.0.1 Flock/2.0b2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9pre) Gecko/2008051917 Firefox/3.0pre Flock/2.0a1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.0.5) Gecko/2009012105 Firefox/3.0.5 Flock/2.0.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.5) Gecko/2008121620 Firefox/3.0.5 Flock/2.0.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.4) Gecko/2008112016 Firefox/3.0.4 Flock/2.0.2",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.0.4) Gecko/2008111323 Firefox/3.0.4 Flock/2.0.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.3) Gecko/2008100719 Firefox/3.0.3 Flock/2.0",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.0.3) Gecko/2008100716 Firefox/3.0.3 Flock/2.0",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.17) Gecko/20080913 Firefox/2.0.0.17 Flock/1.2.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.8.1.17) Gecko/20080915 Firefox/2.0.0.17 Flock/1.2.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.17) Gecko/20080910 Firefox/2.0.0.17 Flock/1.2.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.16) Gecko/20080714 Firefox/2.0.0.16 Flock/1.2.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.14) Gecko/20080608 Firefox/2.0.0.14 Flock/1.2.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; pl; rv:1.8.1.14) Gecko/20080519 Firefox/2.0.0.14 Flock/1.2.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.14) Gecko/20080530 Firefox/2.0.0.14 Flock/1.2.1",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.16) Gecko/20101206 Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.14) Gecko/20080514 Firefox/2.0.0.14 Flock/1.1.4",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.14) Gecko/20080414 Firefox/2.0.0.14 Flock/1.1.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.8.1.13) Gecko/20080326 Firefox/2.0.0.13 Flock/1.1.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.12) Gecko/20080304 Firefox/2.0.0.12 Flock/1.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.8) Gecko/20071018 Firefox/2.0.0.8 Flock/1.0RC3",\
        "Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.8.1.11) Gecko/20080131 Firefox/2.0.0.11 Flock/1.0.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.11) Gecko/20080126 Firefox/2.0.0.11 Flock/1.0.8",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.11) Gecko/20071206 Firefox/2.0.0.11 Flock/1.0.3",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1.8) Gecko/20071101 Firefox/2.0.0.8 Flock/1.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.8.1.7) Gecko/20070925 Firefox/2.0.0.7 Flock/0.9.1.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070801 Firefox/2.0.0.6 Flock/0.9.0.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.2) Gecko/20070307 Firefox/2.0.0.2 Flock/0.7.99",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.9) Gecko/20061219 Flock/0.7.9.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.7) Gecko/20061025 Firefox/1.5.0.8 Flock/0.7.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.7) Gecko/20060929 Firefox/1.5.0.7 Flock/0.7.6",\
        "Mozilla/5.0 (X11; U; Linux ia64; pl; rv:1.8.0.5) Gecko/20060801 Firefox/1.5.0.5 Flock/0.7.4.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.5) Gecko/20060731 Firefox/1.5.0.5 Flock/0.7.4.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.5) Gecko/20060731 Firefox/1.5.0.5 Flock/0.7.4.1",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.0.12) Gecko/20070530 Firefox/1.5.0.12 Flock/0.7.14",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.11) Gecko/20070502 Firefox/1.5.0.11 Flock/0.7.13.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.10) Gecko/20070228 Firefox/1.5.0.10 Flock/0.7.11",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.0.4) Gecko/20060620 Firefox/1.5.0.4 Flock/0.7.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.4) Gecko/20060612 Firefox/1.5.0.4 Flock/0.7.0.17.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.0.1) Gecko/20060331 Flock/0.7",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060314 Flock/0.5.13.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060217 Flock/0.5.11",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8) Gecko/20060102 Flock/0.4.11 Firefox/1.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.8b5) Gecko/20051019 Flock/0.4 Firefox/1.0+",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8b5) Gecko/20051021 Flock/0.4 Firefox/1.0+",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_1; nl-nl) AppleWebKit/532.3+ (KHTML, like Gecko) Fluid/0.9.6 Safari/532.3+",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit/528.16 (KHTML, like Gecko) Fluid/0.9.6 Safari/528.16",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko/20090327 Galeon/2.0.7",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.7) Gecko Galeon/2.0.6 (Debian 2.0.6-2.1)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.4) Gecko/20070508 (Debian-1.8.1.4-3) Galeon/2.0.2 (Debian package 2.0.2-4)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.13pre) Gecko/20080207 Galeon/2.0.1 (Ubuntu package 2.0.1-1ubuntu2) Firefox/1.5.0.13pre",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060027 (Debian-1.8.0.1-11) Galeon/2.0.1 (Debian package 2.0.1-3)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20060122 Galeon/2.0.1",\
        "Mozilla/5.0 (X11; U; Linux i686) Gecko/20030430 Galeon/1.3.4 Debian/1.3.4.20030509-1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20050929 Galeon/1.3.21",\
        "Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.7.12) Gecko/20051105 Galeon/1.3.21",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.8) Gecko/20050513 Galeon/1.3.20 (Debian package 1.3.20-1)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.3) Gecko/20041007 Galeon/1.3.18 (Debian package 1.3.18-1.1)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040510 Galeon/1.3.16",\
        "Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14",\
        "Mozilla/5.0 Galeon/1.2.8 (X11; Linux i686; U;) Gecko/20030317",\
        "Mozilla/5.0 Galeon/1.2.7 (X11; Linux i686; U;) Gecko/20021226 Debian/1.2.7-6",\
        "Mozilla/5.0 Galeon/1.2.6 (X11; Linux i686; U;) Gecko/20020913 Debian/1.2.6-2",\
        "Mozilla/5.0 Galeon/1.2.6 (X11; Linux i686; U;) Gecko/20020827",\
        "Mozilla/5.0 Galeon/1.2.5 (X11; Linux i686; U;) Gecko/20020809",\
        "Mozilla/5.0 Galeon/1.2.5 (X11; Linux i686; U;) Gecko/20020610 Debian/1.2.5-1",\
        "Mozilla/5.0 Galeon/1.2.5 (X11; Linux i586; U;) Gecko/20020623 Debian/1.2.5-0.woody.1",\
        "GranParadiso is an developer preview release for the next major version of Firefox that is being built on top of the next generation of Mozilla's layout engine, Gecko 1.9.",\
        "Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.9a8) Gecko/2007100620 GranParadiso/3.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a7) Gecko/2007080210 GranParadiso/3.0a7",\
        "Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9a4) Gecko/20070427 GranParadiso/3.0a4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a4) Gecko/2007042705 GranParadiso/3.0a4",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3) Gecko/20070322 GranParadiso/3.0a3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a2) Gecko/20070206 GranParadiso/3.0a2",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.9a1) Gecko/20061204 GranParadiso/3.0a1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a1) Gecko/20061204 GranParadiso/3.0a1 MEGAUPLOAD 1.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.9a1) Gecko/20061204 GranParadiso/3.0a1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.9) Gecko/2009042210 GranParadiso/3.0.9",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko/2009033017 GranParadiso/3.0.8",\
        "Mozilla/5.0 (X11; U; Darwin i386; en-US; rv:1.9.0.8) Gecko/2009040414 GranParadiso/3.0.8",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.9.0.7) Gecko/2009030719 GranParadiso/3.0.7 FirePHP/0.2.4",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.7) Gecko/2009030719 GranParadiso/3.0.7 FirePHP/0.2.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.4pre) Gecko/2008102405 GranParadiso/3.0.4pre",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3pre) Gecko/2008092604 GranParadiso/3.0.3pre",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.0.3pre) Gecko/2008090704 GranParadiso/3.0.3pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.2pre) Gecko/2008071405 GranParadiso/3.0.2pre",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.9) Gecko/20070314 GranParadiso/3.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.9a1) Gecko/20061204 GranParadiso/2.0",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; GreenBrowser)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; OfficeLiveConnector.1.4; OfficeLivePatch.1.3; GreenBrowser)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; GTB6; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322; GreenBrowser)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; GTB0.0; InfoPath.1; GreenBrowser)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322; InfoPath.2; GreenBrowser)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.0.04506.30; GreenBrowser)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; .NET CLR 1.0.3705; .NET CLR 1.1.4322; Media Center PC 4.0; .NET CLR 2.0.50727; InfoPath.1; GreenBrowser)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; GreenBrowser)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET CLR 1.1.4322; GreenBrowser)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; GreenBrowser)",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/417.9 (KHTML, like Gecko) Hana/1.0",\
        "Mozilla/5.0 (compatible; IBrowse 3.0; AmigaOS4.0)",\
        "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_8) AppleWebKit/537.3+ (KHTML, like Gecko) iCab/5.0 Safari/533.16",\
        "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_8) AppleWebKit/536.25+ (KHTML, like Gecko) iCab/5.0 Safari/533.16",\
        "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_8) AppleWebKit/536.15+ (KHTML, like Gecko) iCab/5.0 Safari/533.16",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8) AppleWebKit/536.15 (KHTML, like Gecko) iCab/5.0 Safari/533.16",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; nn-no) AppleWebKit/533.21.1 (KHTML, like Gecko) iCab/4.8b Safari/533.16",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-us) AppleWebKit/533.21.1 (KHTML, like Gecko) iCab/4.8 Safari/533.16",\
        "Mozilla/5.0 (compatible; iCab 3.0.5; Macintosh; U; PPC Mac OS X)",\
        "Mozilla/5.0 (compatible; iCab 3.0.3; Macintosh; U; PPC Mac OS X)",\
        "Mozilla/5.0 (compatible; iCab 3.0.2; Macintosh; U; PPC Mac OS X)",\
        "Mozilla/4.5 (compatible; iCab 2.9.9; Macintosh; U; 68K)",\
        "Mozilla/4.5 (compatible; iCab 2.9.1; Macintosh; U; PPC; Mac OS X)",\
        "Mozilla/4.5 (compatible; iCab 2.8.1; Macintosh; I; PPC)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.11) Gecko/20100721 Iceape/2.0.6",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.16) Gecko/20110302 Iceape/2.0.11",\
        "Mozilla/5.0 (X11; U; Linux ppc; fr; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.9) Gecko/20071030 Iceape/1.1.6 (Debian-1.1.6-3)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.4) Gecko/20070509 Iceape/1.1.2 (Debian-1.1.2-1)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.19) Gecko/20081204 Iceape/1.1.14 (Debian-1.1.14-1)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.13pre) Gecko/20070505 Iceape/1.0.9 (Debian-1.0.10~pre070720-0etch3)",\
        "Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.0.11) Gecko/20070217 Iceape/1.0.8 (Debian-1.0.8-4)",\
        "Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.8.0.11) Gecko/20070217 Iceape/1.0.8 (Debian-1.0.8-4)",\
        "Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.0.9) Gecko/20061219 Iceape/1.0.7 (Debian-1.0.7-2)",\
        "IceCat is the GNU version of the Firefox browser. The main difference is: it is entirely free software. While the source code from the Mozilla project is free software, the binaries that they release include additional non-free software.",\
        "Mozilla/5.0 (X11; Linux i686; rv:7.0.1) Gecko/20111106 IceCat/7.0.1",\
        "Mozilla/5.0 (X11; Linux i686; rv:2.0b8) Gecko/20101227 IceCat/4.0b8",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101214 IceCat/3.6.13 (like Firefox/3.6.13)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; it; rv:1.9.2.12) Gecko/20101114 IceCat/3.6.12 (like Firefox/3.6.12)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-CA; rv:1.9.0.3) Gecko/2008092921 IceCat/3.0.3-g1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008072716 IceCat/3.0.1-g1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.11) Gecko/20071203 IceCat/2.0.0.11-g1",\
        "Mozilla/5.0 (X11; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1 Iceweasel/15.0.1",\
        "Mozilla/5.0 (X11; Linux x86_64; rv:15.0) Gecko/20120724 Debian Iceweasel/15.0",\
        "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20120721 Debian Iceweasel/15.0",\
        "Mozilla/5.0 (X11; debian; Linux x86_64; rv:15.0) Gecko/20100101 Iceweasel/15.0",\
        "Mozilla/5.0 (X11; Linux i686; rv:14.0) Gecko/20100101 Firefox/14.0.1 Iceweasel/14.0.1",\
        "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Debian Iceweasel/14.0",\
        "Mozilla/5.0 (X11; Linux x86_64; rv:13.0) Gecko/20100101 Firefox/13.0.1 Iceweasel/13.0.1",\
        "Mozilla/5.0 (X11; Linux x86_64; rv:13.0) Gecko/20100101 Firefox/13.0 Iceweasel/13.0",\
        "Mozilla/5.0 (X11; Gentoo Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2",\
        "Mozilla/5.0 (X11; Linux x86_64; rv:10.0.7) Gecko/20100101 Firefox/10.0.7 Iceweasel/10.0.7",\
        "Mozilla/5.0 (X11; Linux i686; rv:10.0.7) Gecko/20100101 Iceweasel/10.0.7",\
        "Mozilla/5.0 (X11; Linux x86_64; rv:10.0.6) Gecko/20100101 Firefox/10.0.6 Iceweasel/10.0.6",\
        "Mozilla/5.0 (X11; Linux i686 on x86_64; rv:10.0.6) Gecko/20100101 Firefox/10.0.6 Iceweasel/10.0.6",\
        "Mozilla/5.0 (X11; Linux armv6l; rv:10.0.5) Gecko/20100101 Firefox/10.0.5 Iceweasel/10.0.5",\
        "Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 Iceweasel/10.0",\
        "Mozilla/5.0 (X11; Linux x86_64; rv:9.0.1) Gecko/20100101 Firefox/9.0.1 Iceweasel/9.0.1",\
        "Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0 Iceweasel/8.0",\
        "Mozilla/5.0 (X11; Linux x86_64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1 Iceweasel/7.0.1 Debian",\
        "Mozilla/5.0 (X11; Linux i686 on x86_64; rv:6.0.2) Gecko/20100101 Firefox/6.0.2 Iceweasel/6.0.2",\
        "Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0",\
        "Mozilla/5.0 (X11; Linux i686; rv:2.0) Gecko/20110322 Firefox/4.0 Iceweasel/4.0",\
        "Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0",\
        "Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.13) Gecko/20110109 Iceweasel/3.6.13 (like Firefox/3.6.13)",\
        "Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:1.9.1.9) Gecko/20100501 Iceweasel/3.5.9 (like Firefox/3.5.9)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100501 Iceweasel/3.5.8 (like Firefox/3.5.8)",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.1.5) Gecko/20091112 Iceweasel/3.5.5 (like Firefox/3.5.5; Debian-3.5.5-1)",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-GB; rv:1.9.1.3) Gecko/20091010 Iceweasel/3.5.3 (Debian-3.5.3-2)",\
        "Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:1.9.1.18) Gecko/20110324 Iceweasel/3.5.18 (like Firefox/3.5.18)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; it; rv:1.9.1.16) Gecko/20120921 Iceweasel/3.5.16 (like Firefox/3.5.16)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; it; rv:1.9.1.16) Gecko/20120602 Iceweasel/3.5.16 (like Firefox/3.5.16)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; hu-HU; rv:1.9.1.16) Gecko/20110107 Iceweasel/3.5.16 (like Firefox/3.5.16)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.1.16) Gecko/20120511 Iceweasel/3.5.16 (like Firefox/3.5.16)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; es-ES; rv:1.9.1.16) Gecko/20120315 Iceweasel/3.5.16 (like Firefox/3.5.16)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.16) Gecko/20120602 Iceweasel/3.5.16 (like Firefox/3.5.16)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.16) Gecko/20110107 Iceweasel/3.5.16 (Debian-3.0.5-1)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.1.16) Gecko/20120131 Iceweasel/3.5.16 (like Firefox/3.5.16)",\
        "Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.1.16) Gecko/20120602 Iceweasel/3.5.16 (like Firefox/3.5.16)",\
        "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.1.16) Gecko/20111108 Iceweasel/3.5.16 (like Firefox/3.5.16)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1) Gecko/20090704 Iceweasel/3.5 (Debian-3.5-0)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b5) Gecko/2008042623 Iceweasel/3.0b5 (Debian-3.0~b5-3)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.18) Gecko/2010021720 Iceweasel/3.0.9 (Debian-3.0.9-1)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.9.0.7) Gecko/2009030814 Iceweasel/3.0.9 (Debian-3.0.9-1)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.8) Gecko/2009033109 Gentoo Iceweasel/3.0.8",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.0.7) Gecko/2009030810 Iceweasel/3.0.7 (Debian-3.0.7-1)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.6) Gecko/2009020407 Iceweasel/3.0.7 (Debian-3.0.7-1)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko/2009032811 Iceweasel/3.0.7 (Debian-3.0.7-1)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.0.7) Gecko/2009031819 Iceweasel/3.0.6 (Debian-3.0.6-1)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.7) Gecko/2009032813 Iceweasel/3.0.6 (Debian-3.0.6-1)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.12) Gecko/2009072220 Iceweasel/3.0.6 (Debian-3.0.6-1)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.7) Gecko/2009031819 Iceweasel/3.0.6 (Debian-3.0.6-1)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.16) Gecko/2009121609 Iceweasel/3.0.6 (Debian-3.0.6-3)",\
        "Mozilla/5.0 (X11; U; Linux i686; ja; rv:1.9.0.7) Gecko/2009032803 Iceweasel/3.0.6 (Debian-3.0.6-1)",\
        "Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.0.19) Gecko/2010120923 Iceweasel/3.0.6 (Debian-3.0.6-3)",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.9.0.19) Gecko/2010102906 Iceweasel/3.0.6 (Debian-3.0.6-3)",\
        "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.11) Gecko/2009061212 Iceweasel/3.0.6 (Debian-3.0.6-1)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.7) Gecko/2009032803 Iceweasel/3.0.6 (Debian-3.0.6-1)",\
        "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.5) Gecko/2008122011 Iceweasel/3.0.5 (Debian-3.0.5-1)",\
        "Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.9.0.1) Gecko/2008072112 Iceweasel/3.0.3 (Debian-3.0.3-2)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.2) Gecko/2008090211 Ubuntu/9.04 (jaunty) Iceweasel/3.0.2",\
        "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.11) Gecko/2009061319 Iceweasel/3.0.11 (Debian-3.0.11-1)",\
        "Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.9.0.1) Gecko/2008072112 Iceweasel/3.0.1 (Debian-3.0.1-1)",\
        "Mozilla/5.0 (Linux X86; U; Debian SID; it; rv:1.9.0.1) Gecko/2008070208 Debian IceWeasel/3.0.1",\
        "Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.9) Gecko/2008062909 Iceweasel/3.0 (Debian-3.0~rc2-2)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9) Gecko/2008062113 Iceweasel/3.0 (Debian-3.0~rc2-2)",\
        "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.9) Gecko/20071025 Iceweasel/2.0.0.9",\
        "Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.8.1.8) Gecko/20071004 Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-0etch1)",\
        "Mozilla/5.0 (X11; U; Linux x64; en-US; rv:1.8.1.7) Gecko/20070914 Iceweasel/2.0.0.7 (Debian-2.0.0.7-1)",\
        "Mozilla/5.0 (X11; U; Linux x64; en-US; rv:1.8.1.6) Gecko/20070723 Iceweasel/2.0.0.6 (Debian-2.0.0.6-1)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.6) Gecko/20070723 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1) (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.4) Gecko/20070508 Iceweasel/2.0.0.4 (Debian-2.0.0.4-1)",\
        "Mozilla 5.0 (X11; U; Linux i686; en-US; rv:1.8.1.14) Gecko/200770508 Iceweasel/2.0.0.4",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.8.1.3) Gecko/20070310 Iceweasel/2.0.0.3 (Debian-2.0.0.3-1)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.8.1.3) Gecko/20070310 Iceweasel/2.0.0.3 (Debian-2.0.0.3-1)",\
        "Mozilla/5.0 (X11; U; Linux i686; pt-BR; rv:1.8.1.3) Gecko/20070310 Iceweasel/2.0.0.3 (Debian-2.0.0.3-1)",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.8.1.3) Gecko/20070310 Iceweasel/2.0.0.3 (Debian-2.0.0.3-2)",\
        "Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.1.3) Gecko/20070310 Iceweasel/2.0.0.3 (Debian-2.0.0.3-1)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.3) Gecko/20070310 Iceweasel/2.0.0.3 (Debian-2.0.0.3-1)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.13) Gecko/20080311 Firefox/2.0 Iceweasel/2.0.0.3 (Debian-2.0.0.13-1)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.1.3) Gecko/20070310 Iceweasel/2.0.0.3 (Debian-2.0.0.3-1)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.9a3) Gecko/20070409 IceWeasel/2.0.0.3",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.19) Gecko/20081202 Iceweasel/2.0.0.19 (Debian-2.0.0.19-0etch1)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.1.17) Gecko/20080827 Iceweasel/2.0.0.17 (Debian-2.0.0.17-0etch1)",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.8.1.16) Gecko/20080702 Iceweasel/2.0.0.16 (Debian-2.0.0.16-0etch1)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.15) Gecko/20080612 Iceweasel/2.0.0.15 (Debian-2.0.0.15-0etch1)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.14) Gecko/20080404 Iceweasel/2.0.0.14 (Debian-2.0.0.14-2)",\
        "Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.8.1.14) Gecko/20080404 Iceweasel/2.0.0.14 (Debian-2.0.0.14-0etch1)",\
        "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.14) Gecko/20080404 Iceweasel/2.0.0.14 (Debian-2.0.0.14-0etch1)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.14) Gecko/20080404 Iceweasel/2.0.0.14 (Debian-2.0.0.14-0etch1)",\
        "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.13) Gecko/20080311 Iceweasel/2.0.0.13 (Debian-2.0.0.13-0etch1)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.8.1.12) Gecko/20080129 Iceweasel/2.0.0.12 (Debian-2.0.0.12-1)",\
        "Mozilla/5.0 (X11; U; Linux i686; it; rv:1.8.1.12) Gecko/20080129 Iceweasel/2.0.0.12 (Debian-2.0.0.12-0etch1)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.11) Gecko/20071128 Iceweasel/2.0.0.11 (Debian-2.0.0.11-1)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; ru; rv:1.9.2.13) Gecko/20101203 IceWeasel/2.0.0.11 Mnenhy/0.8.3",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1) Gecko/20061024 Iceweasel/2.0 (Debian-2.0+dfsg-1)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Iceweasel/2.0 (Debian-2.0+dfsg-1)",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en; rv:1.8.1) Gecko/20061024 Iceweasel/2.0",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.8pre) Gecko/20061001 Firefox/1.5.0.8pre (Iceweasel)",\
        "Mozilla/5.0 (Linux) Gecko Iceweasel (Debian) Mnenhy",\
        "Mozilla/6.0 (Future Star Technologies Corp. Star-Blade OS; U; en-US) iNet Browser 2.5",\
        "Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0",\
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",\
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)",\
        "Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)",\
        "Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)",\
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",\
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7)",\
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; InfoPath.3; MS-RTC LM 8; .NET4.0C; .NET4.0E)",\
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",\
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; Tablet PC 2.0; InfoPath.3; .NET4.0C; .NET4.0E)",\
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; yie8)",\
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; FunWebProducts)",\
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/11.0.696.57)",\
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.1; SV1; .NET CLR 2.8.52393; WOW64; en-US)",\
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/4.0; GTB7.4; InfoPath.3; SV1; .NET CLR 3.1.76908; WOW64; en-US)",\
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",\
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; .NET CLR 2.7.58687; SLCC2; Media Center PC 5.0; Zune 3.4; Tablet PC 3.6; InfoPath.3)",\
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322)",\
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",\
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 3.0.04506.30)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.3; .NET4.0C; .NET4.0E; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MS-RTC LM 8)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 3.0)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MS-RTC LM 8; InfoPath.3; .NET4.0C; .NET4.0E) chromeframe/8.0.552.224",\
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",\
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; Media Center PC 3.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1)",\
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; InfoPath.1; .NET CLR 2.0.50727)",\
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; Alexa Toolbar; .NET CLR 2.0.50727)",\
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",\
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322)",\
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)",\
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 5.2)",\
        "Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; c .NET CLR 3.0.04506; .NET CLR 3.5.30707; InfoPath.1; el-GR)",\
        "Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; fr-FR)",\
        "Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.2; WOW64; .NET CLR 2.0.50727)",\
        "Mozilla/4.79 [en] (compatible; MSIE 7.0; Windows NT 5.0; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648)",\
        "Mozilla/4.0 (Mozilla/4.0; MSIE 7.0; Windows NT 5.1; FDM; SV1; .NET CLR 3.0.04506.30)",\
        "Mozilla/4.0 (compatible;MSIE 7.0;Windows NT 6.0)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; SLCC2; .NET CLR 2.0.50727; InfoPath.3; .NET4.0C; .NET4.0E; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MS-RTC LM 8)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)",\
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",\
        "Mozilla/4.0 (compatible; MSIE 6.01; Windows NT 6.0)",\
        "Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.1)",\
        "Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.0; YComp 5.0.0.0) (Compatible; ; ; Trident/4.0)",\
        "Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.0; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 4.0; .NET CLR 1.0.2914)",\
        "Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98; YComp 5.0.0.0)",\
        "Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)",\
        "Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.0; .NET CLR 1.0.3705)",\
        "Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",\
        "Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4325)",\
        "Mozilla/45.0 (compatible; MSIE 6.0; Windows NT 5.1)",\
        "Mozilla/4.01 (compatible; MSIE 6.0; Windows NT 5.1)",\
        "Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 6.0)",\
        "Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 5.0)",\
        "Mozilla/4.0 (MSIE 6.0; Windows NT 5.1)",\
        "Mozilla/4.0 (compatible;MSIE 6.0;Windows 98;Q312461)",\
        "Mozilla/4.0 (compatible; U; MSIE 6.0; Windows NT 5.1) (Compatible; ; ; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3; Tablet PC 2.0)",\
        "Mozilla/4.0 (compatible; MSIE 5.5b1; Mac_PowerPC)",\
        "Mozilla/4.0 (compatible; MSIE 5.50; Windows NT; SiteKiosk 4.8; SiteCoach 1.0)",\
        "Mozilla/4.0 (compatible; MSIE 5.50; Windows 98; SiteKiosk 4.8)",\
        "Mozilla/4.0 (compatible;MSIE 5.5; Windows 98)",\
        "Mozilla/4.0 (compatible; MSIE 5.5;)",\
        "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT5)",\
        "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 6.1; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",\
        "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30618)",\
        "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.2; .NET CLR 1.1.4322; InfoPath.2; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; FDM)",\
        "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.2; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",\
        "Mozilla/4.0 (compatible; MSIE 5.22; Mac_PowerPC)",\
        "Mozilla/4.0 (compatible; MSIE 5.2; Mac_PowerPC)",\
        "Mozilla/4.0 (compatible; MSIE 5.17; Mac_PowerPC)",\
        "Mozilla/4.0 (compatible; MSIE 5.16; Mac_PowerPC)",\
        "Mozilla/4.0 (compatible; MSIE 5.15; Mac_PowerPC)",\
        "Mozilla/4.0 (compatible; MSIE 5.14; Mac_PowerPC)",\
        "Mozilla/4.0 (compatible; MSIE 5.12; Mac_PowerPC)",\
        "Mozilla/4.0 (compatible; MSIE 5.05; Windows NT 4.0)",\
        "Mozilla/4.0 (compatible; MSIE 5.05; Windows 98; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT; Hotbar 4.1.8.0)",\
        "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT; .NET CLR 1.0.3705)",\
        "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.2.6; MSIECrawler)",\
        "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.2.6; Hotbar 3.0)",\
        "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.2.4)",\
        "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.0.0)",\
        "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; Wanadoo 5.3; Wanadoo 5.5)",\
        "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; SV1; .NET CLR 1.1.4322; .NET CLR 1.0.3705; .NET CLR 2.0.50727)",\
        "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; Q312461; T312461)",\
        "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; MSIECrawler)",\
        "Mozilla/4.0 (compatible; MSIE 5.00; Windows 98)",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT;)",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; DigExt; YComp 5.0.2.5)",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; DigExt; Hotbar 4.1.8.0)",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; DigExt; .NET CLR 1.0.3705)",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT)",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 5.9; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 5.0)",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98; YComp 5.0.2.4)",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98; DigExt; YComp 5.0.2.6; yplus 1.0)",\
        "Mozilla/4.0 (compatible; MSIE 4.5; Windows NT 5.1; .NET CLR 2.0.40607)",\
        "Mozilla/4.0 (compatible; MSIE 4.5; Mac_PowerPC)",\
        "Mozilla/4.0 PPC (compatible; MSIE 4.01; Windows CE; PPC; 240x320; Sprint:PPC-6700; PPC; 240x320)",\
        "Mozilla/4.0 (compatible; MSIE 4.01; Windows NT 5.0)",\
        "Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Sprint; SCH-i830; PPC; 240x320)",\
        "Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Sprint:SPH-ip320; Smartphone; 176x220)",\
        "Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Sprint:SCH-i320; Smartphone; 176x220)",\
        "Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Smartphone; 176x220)",\
        "Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; 240x320; PPC)",\
        "Mozilla/4.0 (compatible; MSIE 4.01; Windows CE)",\
        "Mozilla/4.0 (compatible; MSIE 4.01; Windows 98; DigExt)",\
        "Mozilla/4.0 (compatible; MSIE 4.01; Windows 95)",\
        "Mozilla/4.0 WebTV/2.6 (compatible; MSIE 4.0)",\
        "Mozilla/4.0 (compatible; MSIE 4.0; Windows 98 )",\
        "Mozilla/4.0 (compatible; MSIE 4.0; Windows 95)",\
        "Mozilla/2.0 (compatible; MSIE 4.0; Windows 98)",\
        "Mozilla/2.0 (compatible; MSIE 3.02; Windows 3.1)",\
        "Mozilla/2.0 (compatible; MSIE 3.01; Windows 95)",\
        "Mozilla/3.0 (compatible; MSIE 3.0; Windows NT 5.0)",\
        "Mozilla/2.0 (compatible; MSIE 3.0; Windows 3.1)",\
        "Mozilla/1.22 (compatible; MSIE 2.0; Windows 95)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; iRider 2.60.0008; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1250.0 Iron/22.0.2150.0 Safari/537.4",\
        "Mozilla/5.0 (X11; U; Linux amd64) Iron/21.0.1200.0 Chrome/21.0.1200.0 Safari/537.1",\
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1200.0 Iron/21.0.1200.0 Safari/537.1",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1200.0 Iron/21.0.1200.0 Safari/537.1",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1200.0 Iron/21.0.1200.0 Safari/537.1",\
        "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1200.0 Iron/21.0.1200.0 Safari/537.1",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1200.0 Iron/21.0.1200.0 Safari/537.1",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_0) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1200.0 Iron/21.0.1200.0 Safari/537.1",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1150.1 Iron/20.0.1150.1 Safari/536.11",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1150.1 Iron/20.0.1150.1 Safari/536.11",\
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1150.1 Iron/20.0.1150.1 Safari/536.11",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1150.1 Iron/20.0.1150.1 Safari/536.11",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1150.1 Iron/20.0.1150.1 Safari/536.11",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1150.0 Iron/20.0.1150.0 Safari/536.11",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1150.0 Iron/20.0.1150.0 Safari/536.11",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Iron/19.0.1100.0 Chrome/19.0.1100.0 Safari/536.5",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Iron/19.0.1100.0 Chrome/19.0.1100.0 Safari/536.5",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.11 (KHTML, like Gecko) Iron/17.0.1000.2 Chrome/17.0.1000.2 Safari/535.11",\
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.11 (KHTML, like Gecko) Iron/17.0.1000.1 Chrome/17.0.1000.1 Safari/535.11",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Iron/17.0.1000.0 Chrome/17.0.1000.0 Safari/535.11",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Iron/17.0.1000.0 Chrome/17.0.1000.0 Safari/535.11",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.11 (KHTML, like Gecko) Iron/17.0.1000.0 Chrome/17.0.1000.0 Safari/535.11",\
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.11 (KHTML, like Gecko) Iron/17.0.1000.0 Chrome/17.0.1000.0 Safari/535.11",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Iron/17.0.1000.0 Chrome/17.0.1000.0 Safari/535.11",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.7 (KHTML, like Gecko) Iron/16.0.950.0 Chrome/16.0.950.0 Safari/535.7",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Iron/16.0.950.0 Chrome/16.0.950.0 Safari/535.1",\
        "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/535.7 (KHTML, like Gecko) Iron/16.0.950.0 Chrome/16.0.950.0 Safari/535.7",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.7 (KHTML, like Gecko) Iron/16.0.950.0 Chrome/16.0.950.0 Safari/535.7",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.1 (KHTML, like Gecko) Iron/14.0.850.0 Chrome/14.0.850.0 Safari/535.1",\
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Iron/13.0.800.0 Chrome/13.0.800.0 Safari/535.1",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Iron/13.0.800.0 Chrome/13.0.800.0 Safari/535.1",\
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Iron/13.0.800.0 Chrome/13.0.800.0 Safari/535.1",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Iron/12.0.750.0 Chrome/12.0.750.0 Safari/534.30",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.30 (KHTML, like Gecko) Iron/12.0.750.0 Chrome/12.0.750.0 Safari/534.30",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.30 (KHTML, like Gecko) Iron/12.0.750.0 Chrome/12.0.750.0 Safari/534.30",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.30 (KHTML, like Gecko) Iron/12.0.750.0 Chrome/12.0.750.0 Safari/534.30",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) Iron/11.0.700.3 Chrome/11.0.700.3 Safari/534.24",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Iron/11.0.700.3 Chrome/11.0.700.3 Safari/534.24",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.24 (KHTML, like Gecko) Iron/11.0.700.3 Chrome/11.0.700.3 Safari/534.24",\
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.24 (KHTML, like Gecko) Iron/11.0.700.2 Chrome/11.0.700.2 Safari/534.24",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Iron/11.0.700.2 Chrome/11.0.700.2 Safari/534.24",\
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/534.24 (KHTML, like Gecko) Iron/11.0.700.2 Chrome/11.0.700.2 Safari/534.24",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.24 (KHTML, like Gecko) Iron/11.0.700.2 Chrome/11.0.700.2 Safari/534.24",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/534.24 (KHTML, like Gecko) Iron/11.0.700.2 Chrome/11.0.700.2 Safari/534.24",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Iron/11.0.700.1 Chrome/11.0.700.1 Safari/534.24",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.24 (KHTML, like Gecko) Iron/11.0.700.1 Chrome/11.0.700.1 Safari/534.24",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Iron/10.0.650.1 Chrome/10.0.650.1 Safari/534.16",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Iron/10.0.650.0 Chrome/10.0.650.0 Safari/534.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Iron/10.0.650.0 Chrome/10.0.650.0 Safari/534.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Iron/10.0.650.0 Chrome/10.0.650.0 Safari/534.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Iron/9.0.600.2 Chrome/9.0.600.2 Safari/534.13",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Iron/9.0.600.2 Chrome/9.0.600.2 Safari/534.13",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Iron/7.0.520.1 Chrome/7.0.520.1 Safari/534.7",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Iron/7.0.520.1 Safari/534.7",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Iron/7.0.520.1 Chrome/7.0.520.1 Safari/534.7",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Iron/7.0.520.0 Chrome/7.0.520.0 Safari/534.7",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Iron/7.0.520.0 Chrome/7.0.520.0 Safari/534.7",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Iron/6.0.475.1 Chrome/6.0.475.1 Safari/534.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Iron/6.0.475.1 Chrome/6.0.475.1 Safari/97486176.534",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Iron/6.0.475.1 Chrome/6.0.475.1 Safari/95066112.534",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Iron/6.0.475.1 Chrome/6.0.475.1 Safari/89895776.534",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Iron/6.0.475.1 Chrome/6.0.475.1 Safari/76829344.534",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Iron/6.0.475.1 Chrome/6.0.475.1 Safari/69296032.534",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Iron/6.0.475.1 Chrome/6.0.475.1 Safari/67162016.534",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Iron/6.0.475.1 Chrome/6.0.475.1 Safari/65209600.534",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Iron/6.0.475.1 Chrome/6.0.475.1 Safari/61389024.534",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Iron/6.0.475.1 Chrome/6.0.475.1 Safari/58473792.534",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Iron/6.0.475 Chrome/6.0.475.0 Safari/92861792.534",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Iron/6.0.475 Chrome/6.0.475.0 Safari/53013696.534",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Iron/6.0.475 Chrome/6.0.475.0 Safari/112818688.534",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Iron/6.0.475 Chrome/6.0.475.0 Safari/59178784.534",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Iron/6.0.475 Chrome/6.0.475.0 Safari/42721888.534",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Iron/6.0.475 Safari/534",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Iron/5.0.326.0 Chrome/5.0.326.0 Safari/533.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Iron/4.0.280.0 Chrome/4.0.275.0 Safari/532.9",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Iron/4.0.280.0 Chrome/4.0.280.0 Safari/532.9",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Iron/4.0.275.2 Chrome/4.0.275.2 Safari/532.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Iron/4.0.275.2 Chrome/4.0.275.2 Safari/532.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Iron/4.0.275.2 Chrome/4.0.275.2 Safari/532.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Iron/4.0.275.2 Chrome/4.0.275.2 Safari/532.8",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.3 (KHTML, like Gecko) Iron/4.0.227.0 Chrome/4.0.227.0 Safari/532.3",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US) AppleWebKit/532.3 (KHTML, like Gecko) Iron/4.0.227.0 Chrome/4.0.227.0 Safari/532.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.3 (KHTML, like Gecko) Iron/4.0.227.0 Chrome/4.0.227.0 Safari/532.3",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Iron/3.0.197.0 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) Chrome/0.0.0 Iron/3.0.197.0 AppleWebKit/532.0 (KHTML, like Gecko) Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/0.0.0 Safari/532.0 Iron/3.0.197.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/532.0 (KHTML, like Gecko) Iron/3.0.197.0 Safari/532.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.0 (KHTML, like Gecko) Iron/3.0.189.0 Safari/531.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.1 (KHTML, like Gecko) Iron/2.0.168.0 Safari/530.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/528.7 (KHTML, like Gecko) Iron/1.0.155.0 Safari/528.7",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.7 (KHTML, like Gecko) Iron/1.0.155.0 Safari/528.7",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/528.4 (KHTML, like Gecko) Iron/0.3.155.0 Safari/19322656.528",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.4 (KHTML, like Gecko) Iron/0.3.155.0 Safari/13506912.528",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Iron/0.2.152.0 Safari/14871328.525",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Iron/0.2.152.0 Safari/28768176.525",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Iron/0.2.152.0 Safari/12733120.525",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Iron/0.2.152.0 Safari/12542120.525",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Iron/0.2.152.0 Safari/12475112.525",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Iron/0.2.152.0 Safari/12282560.525",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Iron/0.2.152.0 Safari/12272384.525",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Iron/0.2.152.0 Safari/12079480.525",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.21pre) Gecko K-Meleon/1.7.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; pl-PL; rv:1.8.1.24pre) Gecko/20100228 K-Meleon/1.5.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.24) Gecko/20100228 K-Meleon/1.5.4",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1.24) Gecko/20100228 K-Meleon/1.5.4",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.21) Gecko/20090331 K-Meleon/1.5.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.8.1.21) Gecko/20090331 K-Meleon/1.5.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; fr-FR; rv:1.8.1.21) Gecko/20090331 K-Meleon/1.5.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; pl-PL; rv:1.8.1.22) Gecko/20090623 K-Meleon/1.5.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr-FR; rv:1.8.1.23) Gecko/20090825 K-Meleon/1.5.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; es-ES; rv:1.8.1.21) Gecko/20090331 K-Meleon/1.5.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.21) Gecko/20090331 K-Meleon/1.5.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.1.21) Gecko/20090331 K-Meleon/1.5.3",\
        "Mozilla/5.0 (Windows; U; Win 9x 4.90; de-DE; rv:1.8.1.21) Gecko/20090331 K-Meleon/1.5.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.8.1.19) Gecko/20081217 K-Meleon/1.5.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-DE; rv:1.8.1.19) Gecko/20081217 K-Meleon/1.5.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR; rv:1.8.1.21) Gecko/20090403 K-Meleon/1.5.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; pl-PL; rv:1.8.1.19) Gecko/20081217 K-Meleon/1.5.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.22pre) Gecko/20090502 K-Meleon/1.5.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.19) Gecko/20081217 K-Meleon/1.5.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.8.1.19) Gecko/20081217 K-Meleon/1.5.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:1.8.1.19) Gecko/20081217 K-Meleon/1.5.2",\
        "Mozilla/5.0 (Darwin; FreeBSD 5.6; en-GB; rv:1.9.1b3pre)Gecko/20081211 K-Meleon/1.5.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU; rv:1.8.1.17) Gecko/20080919 K-Meleon/1.5.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.17) Gecko/20080919 K-Meleon/1.5.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.1.17) Gecko/20080919 K-Meleon/1.5.1",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1.17) Gecko/20080919 K-Meleon/1.5.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.14) Gecko/20080406 K-Meleon/1.5.0b2",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.8.1.17pre) Gecko/20080716 K-Meleon/1.5.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; es-ES; rv:1.8.1.17pre) Gecko/20080716 K-Meleon/1.5.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.8.1.17pre) Gecko/20080716 K-Meleon/1.5.0",\
        "Mozilla/5.0 (Darwin; FreeBSD 5.6; en-GB; rv:1.8.1.17pre) Gecko/20080716 K-Meleon/1.5.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-EN; rv:1.8.1.8) Gecko/20071013 K-Meleon/1.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.1.5) Gecko/20070722 K-Meleon/1.11",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.17pre) Gecko/20080716 K-Meleon/1.1.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; fr-FR; rv:1.8.1.14) Gecko/20080406 K-Meleon/1.1.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.8.1.14) Gecko/20080406 K-Meleon/1.1.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR; rv:1.8.1.14) Gecko/20080406 K-Meleon/1.1.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.14) Gecko/20080406 K-Meleon/1.1.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.1.14) Gecko/20080406 K-Meleon/1.1.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; de-DE; rv:1.8.1.12) Gecko/20080203 K-Meleon/1.1.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080203 K-Meleon/1.1.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.8.1.10) Gecko/20071116 K-Meleon/1.1.3",\
        "Mozilla/5.0 (Windows; U; Win 9x 4.90; es-ES; rv:1.8.1.10) Gecko/20071116 K-Meleon/1.1.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070727 K-Meleon/1.1.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; rv:1.8.1.4) Gecko/20070511 K-Meleon/1.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.4) Gecko/20070511 K-Meleon/1.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.8.1.21) Gecko/20090403 K-Meleon/1.02",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.7) Gecko/20060917 K-Meleon/1.02",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.0.7) Gecko/20060917 K-Meleon/1.02",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en; rv:1.8.0.7) Gecko/20060917 K-Meleon/1.02",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.0.7) Gecko/20060917 K-Meleon/1.02",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.8.0.6) Gecko/20060730 K-Meleon/1.01",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; de-AT; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.8.0.1) Gecko/20060115 K-Meleon/1.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.7.12) Gecko/20050915 K-Meleon/0.9",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050610 K-Meleon/0.9",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7.12) Gecko/20050610 K-Meleon/0.9",\
        "Mozilla/5.0 (Windows; U; Win 9x 4.90; en-US; rv:1.7.5) Gecko/20041220 K-Meleon/0.9",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.5) Gecko/20031016 K-Meleon/0.8.2",\
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.5) Gecko/20031016 K-Meleon/0.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.2b) Gecko/20021016 K-Meleon 0.7",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1.4pre) Gecko/20070404 K-Ninja/2.1.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.7) Gecko/20060917 K-Ninja/2.0.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.6) Gecko/20060731 K-Ninja/2.0.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.0.1) Gecko/20080722 Firefox/3.0.1 Kapiko/3.0",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.7) Gecko Kazehakase/0.5.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.7) Gecko Kazehakase/0.5.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.7) Gecko Kazehakase/0.5.4 Debian/0.5.4-2.2",\
        "Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.8.1.16) Gecko/20080816 Firefox/2.0.0.16 Kazehakase/0.5.4",\
        "Mozilla/5.0 (X11; Linux x86_64; U;) Gecko/20070610 Kazehakase/0.4.7",\
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.7",\
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",\
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/0 Kazehakase/0.4.3 Debian/0.4.3-1ubuntu1",\
        "Mozilla/5.0 (X11; Linux i686; U; rv:1.7) Gecko/0 Kazehakase/0.4.3",\
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070224 Kazehakase/0.3.9",\
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/0 Kazehakase/0.3.9",\
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/0 Kazehakase/0.3.8",\
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20051128 Kazehakase/0.3.3 Debian/0.3.3-1",\
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20050923 Kazehakase/0.2.8 Debian/0.2.8-1ubuntu2",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; KKMAN3.2; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET CLR 1.1.4322; InfoPath.3)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; GTB6.6; KKMAN3.2; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET CLR 1.1.4322; InfoPath.2)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; KKMAN3.2; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB6.6; KKMAN3.2; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB6.5; KKMAN3.2; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Tablet PC 2.0; InfoPath.3; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; GTB6.6; KKMAN3.2; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.30729; .NET CLR 3.5.30729; .NET CLR 1.1.4322; InfoPath.2)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; KKMAN3.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB6.6; KKMAN3.2; InfoPath.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; AskTB5.6)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB6.6; KKMAN3.2; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; InfoPath.3)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; (R1 1.6); KKMAN3.2; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322; InfoPath.2)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; (R1 1.5); KKman3.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; GTB6.6; KKman3.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; OfficeLiveConnector.1.5; OfficeLivePatch.1.3; .NET CLR 3.0.30729)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; KKman3.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30618; OfficeLiveConnector.1.3; OfficeLivePatch.0.0)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; KKman3.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506; InfoPath.2; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; KKman3.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506; InfoPath.1)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; KKman3.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; GTB5; KKman3.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506; InfoPath.1)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; KKman3.0; InfoPath.2; .NET CLR 2.0.50727)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; KKman3.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; KKman3.0; .NET CLR 2.0.50727)",\
        "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; KKman2.0)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.19) Gecko/20081217 KMLite/1.1.2",\
        "Mozilla/5.0 (X11; Linux) KHTML/4.9.1 (like Gecko) Konqueror/4.9",\
        "Mozilla/5.0 (X11) KHTML/4.9.1 (like Gecko) Konqueror/4.9",\
        "Mozilla/5.0 (compatible; Konqueror/4.4; Linux) KHTML/4.4.1 (like Gecko) Fedora/4.4.1-1.fc12",\
        "Mozilla/5.0 (compatible; Konqueror/4.3; Linux) KHTML/4.3.1 (like Gecko) Fedora/4.3.1-3.fc11",\
        "Mozilla/5.0 (compatible; Konqueror/4.2; Linux; X11; x86_64) KHTML/4.2.4 (like Gecko) Fedora/4.2.4-2.fc11",\
        "Mozilla/5.0 (compatible; Konqueror/4.2; Linux) KHTML/4.2.96 (like Gecko)",\
        "Mozilla/5.0 (compatible; Konqueror/4.2; Linux) KHTML/4.2.4 (like Gecko) Fedora/4.2.4-2.fc11",\
        "Mozilla/5.0 (compatible; Konqueror/4.2; Linux) KHTML/4.2.1 (like Gecko) Fedora/4.2.1-4.fc11",\
        "Mozilla/5.0 (compatible; Konqueror/4.1; OpenBSD) KHTML/4.1.4 (like Gecko)",\
        "Mozilla/5.0 (compatible; Konqueror/4.1; Linux) KHTML/4.1.3 (like Gecko) Fedora/4.1.3-3.fc10",\
        "Mozilla/5.0 (compatible; Konqueror/4.1; DragonFly) KHTML/4.1.4 (like Gecko)",\
        "Mozilla/5.0 (compatible; Konqueror/4.0; Windows) KHTML/4.0.83 (like Gecko)",\
        "Mozilla/5.0 (compatible; Konqueror/4.0; Linux) KHTML/4.0.82 (like Gecko)",\
        "Mozilla/5.0 (compatible; Konqueror/3.5; SunOS) KHTML/3.5.1 (like Gecko)",\
        "Mozilla/5.0 (compatible; Konqueror/3.5; SunOS)",\
        "Mozilla/5.0 (compatible; Konqueror/3.5; NetBSD 3.0; X11) KHTML/3.5.2 (like Gecko)",\
        "Mozilla/5.0 (compatible; Konqueror/3.5; Linux; x86_64) KHTML/3.5.5 (like Gecko) (Debian)",\
        "Mozilla/5.0 (compatible; Konqueror/3.5; Linux; X11; i686; en_US) KHTML/3.5.6 (like Gecko) (Debian)",\
        "Mozilla/5.0 (compatible; Konqueror/3.5; Linux; i686; U; it-IT) KHTML/3.5.5 (like Gecko) (Debian)",\
        "Mozilla/5.0 (compatible; Konqueror/3.5; Linux; de) KHTML/3.5.5 (like Gecko) (Debian)",\
        "Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.7 (like Gecko) SUSE",\
        "Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.7 (like Gecko) (Debian)",\
        "Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.6 (like Gecko) (Kubuntu)",\
        "Mozilla/5.0 (compatible; Konqueror/3.4; Linux; de, en_US) KHTML/3.4.2 (like Gecko) (Debian package 4:3.4.2-4)",\
        "Mozilla/5.0 (compatible; Konqueror/3.4; Linux) KHTML/3.4.3 (like Gecko) (Kubuntu package 4:3.4.3-0ubuntu1)",\
        "Mozilla/5.0 (compatible; Konqueror/3.4; Linux) KHTML/3.4.3 (like Gecko)",\
        "Mozilla/5.0 (compatible; Konqueror/3.4; Linux) KHTML/3.4.2 (like Gecko)",\
        "Mozilla/5.0 (compatible; Konqueror/3.4; Linux) KHTML/3.4.0 (like Gecko)",\
        "Mozilla/5.0 (compatible; Konqueror/3.4; Linux 2.6.12.6; X11; i686; en_US) KHTML/3.4.3 (like Gecko)",\
        "Mozilla/5.0 (compatible; Konqueror/3.4; Linux 2.6.11; X11)",\
        "Mozilla/5.0 (compatible; Konqueror/3.4) KHTML/3.4.0 (like Gecko)",\
        "Mozilla/5.0 (compatible; Konqueror/3.3; Linux) KHTML/3.3.2 (like Gecko)",\
        "Mozilla/5.0 (compatible; Konqueror/3.3; Linux 2.6.9-1.667) (KHTML, like Gecko)",\
        "Mozilla/5.0 (compatible; Konqueror/3.3; Linux 2.6.11; X11; i686) KHTML/3.3.2 (like Gecko)",\
        "Mozilla/5.0 (compatible; Konqueror/3.3; Linux 2.6.11.12-whnetz-xenU; X11; i686; en_US) KHTML/3.3.2 (like Gecko)",\
        "Mozilla/5.0 (compatible; Konqueror/3.3; Linux 2.4.27; X11) (KHTML, like Gecko)",\
        "Mozilla/5.0 (compatible; Konqueror/3.3) KHTML/3.3.2 (like Gecko)",\
        "Mozilla/5.0 (compatible; Konqueror/3.2; Linux; X11; en_US) (KHTML, like Gecko)",\
        "Mozilla/5.0 (compatible; Konqueror/3.2; Linux 2.6.2) (KHTML, like Gecko)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20021224)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20021203)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20021119)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20021105)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20021006)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20020915)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20020905)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20020822)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20020626)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20020614)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20021224)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20021212)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20021112)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020927)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020910)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020823)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020809)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020625)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020615)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020601)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20021217)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20021204)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20021114)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020928)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020912)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020827)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020811)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020718)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020602)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020511)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20021223)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20021204)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20021110)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20021004)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020915)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020818)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020716)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020607)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020515)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020426)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021221)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021119)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021014)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020925)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020905)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020818)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020808)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020619)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020612)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020513)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc1; i686 Linux; 20021226)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc1; i686 Linux; 20021120)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc1; i686 Linux; 20021022)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc1; i686 Linux; 20020919)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc1; i686 Linux; 20020816)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc1; i686 Linux; 20020722)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc1; i686 Linux; 20020711)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc1; i686 Linux; 20020620)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc1; i686 Linux; 20020608)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1-rc1; i686 Linux; 20020515)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1; Linux; X11; i686)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1; Linux)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1; i686 Linux; 20021113)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1; i686 Linux; 20021105)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1; i686 Linux; 20021102)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1; i686 Linux; 20021007)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1; i686 Linux; 20021001)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1; i686 Linux; 20020913)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1; i686 Linux; 20020811)",\
        "Mozilla/5.0 (compatible; Konqueror/3.1; i686 Linux; 20020720)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0.0-10; Linux)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0.0; Linux)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc6; i686 Linux; 20021127)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc6; i686 Linux; 20021106)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc6; i686 Linux; 20021012)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc6; i686 Linux; 20020918)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc6; i686 Linux; 20020908)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc6; i686 Linux; 20020817)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc6; i686 Linux; 20020718)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc6; i686 Linux; 20020614)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc6; i686 Linux; 20020522)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc6; i686 Linux; 20020512)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc5; i686 Linux; 20021226)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc5; i686 Linux; 20021210)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc5; i686 Linux; 20021121)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc5; i686 Linux; 20021109)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc5; i686 Linux; 20021026)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc5; i686 Linux; 20021015)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc5; i686 Linux; 20020913)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc5; i686 Linux; 20020901)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc5; i686 Linux; 20020821)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc5; i686 Linux; 20020703)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc4; i686 Linux; 20021117)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc4; i686 Linux; 20021016)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc4; i686 Linux; 20020926)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc4; i686 Linux; 20020920)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc4; i686 Linux; 20020821)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc4; i686 Linux; 20020802)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc4; i686 Linux; 20020707)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc4; i686 Linux; 20020622)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc4; i686 Linux; 20020519)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc4; i686 Linux; 20020504)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc3; i686 Linux; 20021125)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc3; i686 Linux; 20021025)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc3; i686 Linux; 20021013)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc3; i686 Linux; 20020910)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc3; i686 Linux; 20020812)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc3; i686 Linux; 20020703)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc3; i686 Linux; 20020624)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc3; i686 Linux; 20020605)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc3; i686 Linux; 20020517)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc3; i686 Linux; 20020426)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc2; i686 Linux; 20021221)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc2; i686 Linux; 20021118)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc2; i686 Linux; 20020809)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc2; i686 Linux; 20020606)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc2; i686 Linux; 20020505)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc2; i686 Linux; 20020323)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc2; i686 Linux; 20020219)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc2; i686 Linux; 20020110)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc2; i686 Linux; 20020107)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc2; i686 Linux; 20020105)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc1; i686 Linux; 20021206)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc1; i686 Linux; 20021103)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc1; i686 Linux; 20020917)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc1; i686 Linux; 20020906)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc1; i686 Linux; 20020807)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc1; i686 Linux; 20020726)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc1; i686 Linux; 20020705)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc1; i686 Linux; 20020703)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc1; i686 Linux; 20020515)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0-rc1; i686 Linux; 20020217)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0; i686 Linux; 20021117)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0; i686 Linux; 20021012)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0; i686 Linux; 20020927)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0; i686 Linux; 20020825)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0; i686 Linux; 20020817)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0; i686 Linux; 20020728)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0; i686 Linux; 20020707)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0; i686 Linux; 20020603)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0; i686 Linux; 20020510)",\
        "Mozilla/5.0 (compatible; Konqueror/3.0; i686 Linux; 20020423)",\
        "Mozilla/5.0 (compatible; Konqueror/2.2.2; Linux)",\
        "Mozilla/5.0 (compatible; Konqueror/2.2.2)",\
        "Mozilla/5.0 (compatible; Konqueror/2.2.1; Linux)",\
        "Mozilla/5.0 (compatible; Konqueror/2.2-12; Linux)",\
        "Mozilla/5.0 (compatible; Konqueror/2.2-11; Linux)",\
        "Mozilla/5.0 (compatible; Konqueror/2.1.1; X11)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; ru-RU) AppleWebKit/533.3 (KHTML, like Gecko) Leechcraft/0.3.95-1-g84cc6b7 Safari/533.3",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Linux 2.6.26-1-amd64) Lobo/0.98.3",\
        "Mozilla/4.0 (compatible; MSIE 6.0; U; Windows;) Lobo/0.98",\
        "Mozilla/4.0 (compatible; MSIE 6.0; U; Windows;) Lobo/0.97.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2) Gecko/20070225 lolifox/0.32",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2) Gecko/20070224 lolifox/0.3.2 MEGAUPLOAD 1.0",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1) Gecko/20061127 lolifox/0.3.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1b1) Gecko/20060713 lolifox/0.2.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.28) Gecko/20120410 Firefox/3.6.28 Lunascape/6.7.1.25446",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ko; rv:1.9.2.16) Gecko/20110325 Firefox/3.6.16 Lunascape/6.4.5.23569",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ja; rv:1.9.1.15) Gecko/20101029 Firefox/3.5.15 Lunascape/6.3.4.23051 ( .NET CLR 3.5.30729; .NET4.0C)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.9.1.15) Gecko/20101029 Firefox/3.5.15 Lunascape/6.3.4.23051 ( .NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja; rv:1.9.1.15) Gecko/20101029 Firefox/3.5.15 Lunascape/6.3.4.23051 ( .NET CLR 3.5.30729; .NET4.0E)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP) AppleWebKit/533.3 (KHTML, like Gecko) Lunascape/6.3.4.23051 Safari/533.3",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET CLR 1.1.4322; InfoPath.3; .NET4.0C; Lunascape 6.3.4.23051)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; Lunascape 6.3.4.23051)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; InfoPath.2; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Lunascape 6.3.4.23051)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB6.6; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Lunascape 6.3.4.23051)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; OfficeLiveConnector.1.4; OfficeLivePatch.1.3; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Lunascape 6.3.4.23051)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; InfoPath.2; Lunascape 6.3.4.23051)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Media Center PC 5.0; SLCC1; OfficeLiveConnector.1.5; OfficeLivePatch.1.3; .NET4.0C; Lunascape 6.3.",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; OfficeLiveConnector.1.4; OfficeLivePatch.1.3; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Lunascape 6.3.3.22929)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; pt; rv:1.9.1.13) Gecko/20100917 Firefox/3.5.13 Lunascape/6.3.2.22803",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.11) Gecko/20100821 Firefox/3.5.11 Lunascape/6.3.1.22729",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja; rv:1.9.1.10) Gecko/20100624 Firefox/3.5.10 Lunascape/6.2.0.22177 ( .NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.4) Gecko/20100624 Firefox/3.6.4 Lunascape/6.2.0.22177 GTB7.1",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; SLCC1; Tablet PC 2.0; Lunascape 6.2.0.22177)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; GTB6.5; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Lunascape 6.2.0.22177)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; GTB6.5; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Lunascape 6.2.0.22177)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; Lunascape 6.2.0.22177)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; GTB6.5; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Lunascape 6.2.0.22177)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; Lunascape 6.2.0.22177)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; es-ES; rv:1.9.1.10) Gecko/20100624 Firefox/3.5.10 Lunascape/6.1.7.21880 (.NET CLR 3.5.30729)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Lunascape 6.1.7.21880)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Lunascape 6.1.7.21880)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322; Lunascape 6.1.5.21576)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja; rv:1.9.1.9) Gecko/20100331 Firefox/3.5.9 Lunascape/6.1.4.21478",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; cs-CZ) AppleWebKit/533.3 (KHTML, like Gecko) Lunascape/6.1.0.20995 Safari/533.3",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; Lunascape 6.0.3.20663)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.9.1.3) Gecko/20090804 Firefox/3.5.3 Lunascape/5.1.5.19059",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506; OfficeLiveConnector.1.3; OfficeLivePatch.1.3; Lunascape 5.1.4.5)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; MathPlayer 2.10b; .NET CLR 1.1.4322; InfoPath.1; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET CLR 1.0.3705; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Lunascape",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; InfoPath.2; .NET CLR 3.5.30729; .NET CLR 3.0.30618; Lunascape 5.1.3.4)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1) Gecko/20090701 Firefox/3.5 Lunascape/5.1.2.3",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Lunascape 5.1.2.3)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/528+ (KHTML, like Gecko, Safari/528.0) Lunascape/5.1.2.0",\
        "Mozilla/5.0 (Windows; U; ; cs-CZ) AppleWebKit/528+ (KHTML, like Gecko, Safari/528.0) Lunascape/5.1.2.0",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; GTB6; SLCC1; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322; .NET CLR 3.5.21022; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Lunascape 5.1.1.2)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; ja-JP) AppleWebKit/528+ (KHTML, like Gecko, Safari/528.0) Lunascape/5.1.1.0",\
        "Mozilla/5.0 (Windows; U; ; cs-CZ) AppleWebKit/528+ (KHTML, like Gecko, Safari/528.0) Lunascape/5.1.1.0",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; Lunascape 5.1.0.1)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1b4pre) Gecko/20090312 Firefox/3.1b4pre Lunascape/5.0.5.0",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; GTB5; SLCC1; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Lunascape 5.0.5.0)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506; OfficeLiveConnector.1.3; OfficeLivePatch.1.3; Lunascape 5.0.5.0)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; GTB6; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506; OfficeLiveConnector.1.3; OfficeLivePatch.0.0; Lunascape 5.0.5.0)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; Lunascape 5.0.5.0)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; GTB6; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Lunascape 5.0.4.0)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; Lunascape 5.0.4.0)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1b4pre) Gecko/20090312 Firefox/3.1b4pre Lunascape/5.0.3.0",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; Lunascape 5.0.3.0)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528+ (KHTML, like Gecko, Safari/528.0) Lunascape/5.0.2.0",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 2.0.50727; Lunascape 5.0 alpha3)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; Lunascape 5.0 alpha3)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506; Tablet PC 2.0; Lunascape 5.0 alpha2)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP) AppleWebKit/529 (KHTML, like Gecko, Safari/529.0) Lunascape/4.9.9.99",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Lunascape 4.9.9.97)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; ja-JP) AppleWebKit/529 (KHTML, like Gecko, Safari/529.0) Lunascape/4.9.9.96",\
        "Mozilla/5.0 (Windows; N; Windows NT 5.1; id-ID) AppleWebKit/529 (KHTML, like Gecko, Safari/529.0) Lunascape/4.9.9.94",\
        "Mozilla/5.0 (Windows; N; Windows NT 5.1; en-US) AppleWebKit/529 (KHTML, like Gecko, Safari/529.0) Lunascape/4.9.9.94",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; Lunascape 4.8.1)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Lunascape 4.0.1)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; InfoPath.1; .NET CLR 2.0.50727; Lunascape 3.0.4)",\
        
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.7.12) Gecko/20051001 Firefox/1.0.7 Madfox/0.3.2u3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",\
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; Maxthon/3.0)",\
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/4.0; WOW64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0; Maxthon 2.0)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; chromeframe; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAXTHON 2.0)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30618; MAXTHON 2.0)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30618; MAXTHON 2.0)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; MAXTHON 2.0)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; .NET CLR 1.1.4322; .NET CLR 2.0.50727; MAXTHON 2.0)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET4.0C; .NET4.0E; Maxthon 2.0)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Maxthon 2; MAXTHON 2.0)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 1.0.3705; MAXTHON 2.0)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; MAXTHON 2.0)",\
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Maxthon; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 3.0.04320)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Maxthon; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Maxthon; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; InfoPath.2; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Maxthon; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; Maxthon; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 1.1.4322; .NET CLR 3.5.21022; .NET CLR 3.0.30618; .NET CLR 3.5.30729; OfficeLiveConnector.1.3; OfficeLivePatch.0.0)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506; .NET CLR 1.1.4322; InfoPath.2)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Maxthon; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.5.21022; .NET CLR 3.5.30729; .NET CLR 3.0.30618)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2; Maxthon; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Maxthon; Maxthon; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Maxthon; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",\
        "Mozilla/5.0 (X11; Linux; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Midori/0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; pt-br; rv:1.8.1) Gecko/20061010 Firefox/2.0 Midori/0.2.0",\
        "Mozilla/5.0 (X11; U; Linux; it-it) AppleWebKit/531+ (KHTML, like Gecko) Safari/531.2+ Midori/0.2",\
        "Mozilla/5.0 (X11; U; Linux; fr-fr) AppleWebKit/532+ (KHTML, like Gecko) Safari/419.3 Midori/0.1.7",\
        "Mozilla/5.0 (X11; U; Linux; en-us; rv:1.8.1) Gecko/20061010 Firefox/2.0 Midori/0.1.6",\
        "Mozilla/5.0 (X11; U; Linux i686; de) AppleWebKit/523+ (KHTML like Gecko) midori/0.1",\
        "Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:1.8.1.9) Gecko/20071103 Midori/0.0.10",\
        "Mozilla/5.0 (X11; U; Linux x86_64; it-it) AppleWebKit/525.1+ (KHTML, like Gecko, Safari/525.1+) midori",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fr-fr) AppleWebKit/525.1+ (KHTML, like Gecko, Safari/525.1+) midori",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-us) AppleWebKit/525.1+ (KHTML, like Gecko, Safari/525.1+) midori",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-gb) AppleWebKit/525.1+ (KHTML, like Gecko, Safari/525.1+) midori",\
        "Mozilla/5.0 (X11; U; Linux x86_64; de-at) AppleWebKit/525.1+ (KHTML, like Gecko, Safari/525.1+) midori",\
        "Mozilla/5.0 (X11; U; Linux i686; zh-cn) AppleWebKit/525.1+ (KHTML, like Gecko, Safari/525.1+) midori",\
        "Mozilla/5.0 (X11; U; Linux i686; ru-ru) AppleWebKit/525.1+ (KHTML, like Gecko, Safari/525.1+) midori",\
        "Mozilla/5.0 (X11; U; Linux i686; pl-pl) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) midori",\
        "Mozilla/5.0 (X11; U; Linux i686; nl-nl) AppleWebKit/525.1+ (KHTML, like Gecko, Safari/525.1+) midori",\
        "Mozilla/5.0 (X11; U; Linux i686; hu-hu) AppleWebKit/525.1+ (KHTML, like Gecko, Safari/525.1+) midori",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:2.0a1pre) Gecko/2008060602 Minefield/4.0a1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:2.0a1pre) Gecko/2008032902 Minefield/4.0a1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.9.3a5pre) Gecko/20100605 Minefield/3.7a5pre ( .NET CLR 3.5.30729)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; ru; rv:1.9.3a4pre) Gecko/20100319 Minefield/3.7a4pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.3a4pre) Gecko/20100402 Minefield/3.7a4pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.3a3pre) Gecko/20100313 Minefield/3.7a3pre (.NET CLR 4.0.20506)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.3a3pre) Gecko/20100305 Minefield/3.7a3pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.3a3pre) Gecko/20100311 Minefield/3.7a3pre",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.3a1pre) Gecko/20091022 Minefield/3.7a1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.3a1pre) Gecko/20091013 Minefield/3.7a1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.3a1pre) Gecko/20090829 Minefield/3.7a1pre (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.3a1pre) Gecko/20091130 Minefield/3.7a1pre GTB6",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.3a1pre) Gecko/20091002 Minefield/3.7a1pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2a1pre) Gecko/20090501 Minefield/3.6a1pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2a1pre) Gecko/20090417 Minefield/3.6a1pre",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2a1pre) Gecko/20090403 Minefield/3.6a1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2a1pre) Gecko/20090707 Minefield/3.6a1pre (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2a1pre) Gecko/20090411 Minefield/3.6a1pre (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2a1pre) Gecko/20090401 Minefield/3.6a1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2a1pre) Gecko/20090709 Minefield/3.6a1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2a1pre) Gecko/20090424 Minefield/3.6a1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2a1pre) Gecko/20090415 Minefield/3.6a1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2a1pre) Gecko/20090410 Minefield/3.6a1pre",\
        "Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.2a1pre) Gecko/20090330 Kubuntu/8.10 (intrepid) Minefield/3.2a1pre",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2a1pre) Gecko/20090102 Ubuntu/9.04 (jaunty) Minefield/3.2a1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2a1pre) Gecko/20090306 Minefield/3.2a1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2a1pre) Gecko/20090210 Minefield/3.2a1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2a1pre) Gecko/20090306 Minefield/3.2a1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2a1pre) Gecko/20090219 Minefield/3.2a1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2a1pre) Gecko/20090113 Minefield/3.2a1pre",\
        "Mozilla/5.0 (Windows; U; Windows CE 6.0; en-US; rv:1.9.2a1pre) Gecko/20090219 Minefield/3.2a1pre",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.2a1pre) Gecko/20090302 Minefield/3.2a1pre",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.2a1pre) Gecko/20090224 Minefield/3.2a1pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1b2pre) Gecko/20081115 Minefield/3.1b2pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9.1b2pre) Gecko/20081026 Minefield/3.1b2pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1b3pre) Gecko/20090206 Minefield/3.1b2pre Firefox/3.0.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1b2pre) Gecko/20081026 Minefield/3.1b2pre",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.4; en-US; rv:1.9.1b2pre) Gecko/20081027 Minefield/3.1b2pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1b1pre) Gecko/20080929020931 Minefield/3.1b1pre",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1b1pre) Gecko/20080916020338 Minefield/3.1b1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1b1pre) Gecko/20080930093007 Minefield/3.1b1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1b1pre) Gecko/20080926033937 Minefield/3.1b1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1b1pre) Gecko/20080913185648 Minefield/3.1b1pre",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1b1pre) Gecko/20080908170408 Minefield/3.1b1pre",\
        "Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:1.9.1a2pre) Gecko/20080826020557 Minefield/3.1a2pre",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1a2pre) Gecko/20080826052737 Minefield/3.1a2pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1a1pre) Gecko/2008071603 Firefox Minefield/3.1a1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1a1pre) Gecko/2008062005 Minefield/3.1a1pre",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9pre) Gecko/2008061504 Minefield/3.0pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9pre) Gecko/2008041506 Minefield/3.0pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9pre) Gecko/2008040907 Minefield/3.0pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9b5pre) Gecko/2008032204 Minefield/3.0b5pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9b5pre) Gecko/2008030706 Minefield/3.0b5pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9b4pre) Gecko/2008021304 Minefield/3.0b4pre",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b3pre) Gecko/2008010404 Minefield/3.0b3pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9b3pre) Gecko/2007121805 Minefield/3.0b3pre",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b3) Gecko/2008021322 Minefield/3.0b3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9b2pre) Gecko/2007112619 Minefield/3.0b2pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9b2pre) Gecko/2007120405 Minefield/3.0b2pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9b2pre) Gecko/2007110805 Minefield/3.0b2pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9b2) Gecko/2007122607 Minefield/3.0b2",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9a9pre) Gecko/2007092705 Minefield/3.0a9pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a9pre) Gecko/2007102105 Minefield/3.0a9pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9a8pre) Gecko/2007090213 Minefield/3.0a8pre",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.9a8pre) Gecko/2007083104 Minefield/3.0a8pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9a6pre) Gecko/20070615 Minefield/3.0a6pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a6pre) Gecko/20070626 Minefield/3.0a6pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a6pre) Gecko/20070604 Minefield/3.0a6pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a6pre) Gecko/20070602 Minefield/3.0a6pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a5pre) Gecko/20070529 Minefield/3.0a5pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9a4pre) Gecko/20070427 Minefield/3.0a4pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a4pre) Gecko/20070416 Minefield/3.0a4pre",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070301 Minefield/3.0a3pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a3pre) Gecko/20070218 Minefield/3.0a3pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a2pre) Gecko/20070204 Minefield/3.0a2pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a2pre) Gecko/20061231 Minefield/3.0a2pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a2pre) Gecko/20061221 Minefield/3.0a2pre",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a2) Gecko/20070221 Minefield/3.0a2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a1) Gecko/20061111 Minefield/3.0a1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a1) Gecko/20060819 Minefield/3.0a1",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9a1) Gecko/20061007 Minefield/3.0a1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2 x64; en-US; rv:1.9a1) Gecko/20061007 Minefield/3.0a1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a1) Gecko/20061129 Minefield/3.0a1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a1) Gecko/20061124 Minefield/3.0a1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a1) Gecko/2006112204 Minefield/3.0a1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a1) Gecko/20060910 Minefield/3.0a1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a1) Gecko/20060816 Minefield/3.0a1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a1) Gecko/20060725 Minefield/3.0a1",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6.0; en-US; rv:1.9.0.7) Gecko/2009030517 Minefield/3.0.7",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9.0.3pre) Gecko/2008111500 Minefield/3.0.5pre",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071910 Minefield/3.0.1",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.6) Gecko/2009020911 Ubuntu/8.10 (intrepid) Minefield/3.0 MEGAUPLOAD 2.0",\
        "MozillaMozilla",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; it; rv:2.0b4) Gecko/20100818",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.9.2a1pre) Gecko",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; pl; rv:1.9.2.3) Gecko/20100401 Lightningquail/3.6.3",\
        "Mozilla/5.0 (X11; ; Linux i686; rv:1.9.2.20) Gecko/20110805",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.9.2.13) Gecko/20101203 iPhone",\
        "Mozilla 1.9.1b3",\
        "Mozilla 1.9.0.9",\
        "Mozilla 1.9.0.8",\
        "Mozilla 1.9.0.7",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.7) Gecko/2009021910 MEGAUPLOAD 1.0",\
        "Mozilla 1.9.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.6) Gecko/20080528",\
        "Mozilla 1.9.0.3",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008092816",\
        "Mozilla 1.9.0.2",\
        "Mozilla 1.9.0.14",\
        "Mozilla 1.9.0.10",\
        "Mozilla 1.9.0.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008072820 Ubuntu/8.04 (hardy) (Linux Mint)",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.0.1) Gecko/2008070206",\
        "Mozilla 1.9",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9) Gecko",\
        "Mozilla 1.8b2",\
        "Mozilla 1.8b",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.8b) Gecko/20050217",\
        "Mozilla 1.8a6",\
        "Mozilla 1.8a5",\
        "Mozilla 1.8a4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.8a4) Gecko/20040927",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8a3) Gecko/20040817",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8a1) Gecko/20040520",\
        "Mozilla 1.8.1a2",\
        "Mozilla 1.8.1.8",\
        "Mozilla 1.8.1.6",\
        "Mozilla 1.8.1.4",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.4) Gecko/20070508 (Debian-1.8.1.4-2ubuntu5)",\
        "Mozilla 1.8.1.3",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.8.1.3) Gecko/20070310",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.3) Gecko/20070321",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; nl-NL; rv:1.8.1.3) Gecko/20080722",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en; rv:1.8.1.2pre) Gecko/20070223",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.2) Gecko/20070208",\
        "Mozilla 1.8.1.18",\
        "Mozilla 1.8.1.16",\
        "Mozilla 1.8.1.15",\
        "Mozilla 1.8.1.13",\
        "Mozilla 1.8.1.12",\
        "Mozilla 1.8.1.11",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.11) Gecko/20071213",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1.11) Gecko/20071127",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Mozilla/5.0 (Debian-2.0.0.1+dfsg-2)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.1.1) Gecko/20061204",\
        "Mozilla 1.8.0.9",\
        "Mozilla 1.8.0.6",\
        "Mozilla 1.8.0.5",\
        "Mozilla 1.8.0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.4) Gecko/20060508",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.14eol) Gecko/20070505 (Debian-1.8.0.15~pre080614d-0etch1)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060126",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.8) Gecko/20051111",\
        "Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.7b) Gecko/20040429",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.7b) Gecko/20040316",\
        "Mozilla 1.7.9",\
        "Mozilla 1.7.8",\
        "Mozilla/5.0 (X11; U; Linux i686; rv:1.7.8) Gecko/20061113 Debian/1.7.8-1sarge8",\
        "Mozilla/5.0 (X11; U; Linux i686; rv:1.7.8) Gecko/20060628 Debian/1.7.8-1sarge7.1",\
        "Mozilla/5.0 (X11; U; Linux i686; rv:1.7.8) Gecko/20050831 Debian/1.7.8-1sarge2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.8) Gecko/20050921",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.8) Gecko/20050610",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.8) Gecko/20050512 Red Hat/1.7.8-1.1.3.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.7.8) Gecko/20050511",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.7.8) Gecko/20050511",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7.8) Gecko/20050511",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.7.8) Gecko/20050511",\
        "Mozilla 1.7.7",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.7) Gecko/20050427 Red Hat/1.7.7-1.1.3.4",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.7) Gecko/20050414",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr-FR; rv:1.7.7) Gecko/20050414",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.7.7) Gecko/20050414",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.7.7) Gecko/20050414",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.6) Gecko/20050328 Fedora/1.7.6-1.2.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU; rv:1.7.6) Gecko/20050319",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.6) Gecko/20050319",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.7.6) Gecko/20050319",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.7.6) Gecko/20050319",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.7.5) Gecko/20041221",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.5) Gecko/20041013",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.5) Gecko/20041217",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7.5) Gecko/20041217",\
        "Mozilla/5.0 (Windows NT 5.1; U; pt-br; rv:1.7.5) Gecko/20041110",\
        "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.7.5) Gecko/20041110",\
        "Mozilla/5.0 (OS/2; U; Warp 4.5; de-DE; rv:1.7.5) Gecko/20050523",\
        "Mozilla 1.7.3",\
        "Mozilla/5.0 (X11; U; Linux i686; fr-FR; rv:1.7.3) Gecko/20040913",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.3) Gecko/20040913",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr-FR; rv:1.7.3) Gecko/20040910",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.3) Gecko/20040910",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; fr-FR; rv:1.7.3) Gecko/20040910",\
        "Mozilla/5.0 (Windows; U; Win98; fr; rv:1.7.3) Gecko/20040910",\
        "Mozilla/5.0 (Windows; U; Win98; de-AT; rv:1.7.3) Gecko/20040910",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; es-ES; rv:1.7.3) Gecko/20040910",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.7.2) Gecko/20040804",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.2) Gecko/20040804",\
        "Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.7.2) Gecko/20040906",\
        "Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.7.2) Gecko/20040804",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.7.2) Gecko/20040709",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.2) Gecko/20040804",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7.2) Gecko/20040803",\
        "Mozilla/5.0 (Windows; ; Windows NT 5.1; rv:1.7.2) Gecko/20040804",\
        "Mozilla 1.7.13",\
        "Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.7.13) Gecko/20060901",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.13) Gecko/20060427 Debian/1.7.13-0ubuntu05.04",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.7.13) Gecko/20060417",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.7.13) Gecko/20060414",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.7.13) Gecko/20060414",\
        "Mozilla/4.0 (compatible; Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.13) Gecko/20060414; Windows NT 5.1)",\
        "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.7.12) Gecko/20050929",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20060216 Debian/1.7.12-1.1ubuntu2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20060202 Fedora/1.7.12-1.5.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051013 Debian/1.7.12-1ubuntu1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051007 Debian/1.7.12-1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20050923",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20050921",\
        "Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.7.12) Gecko/20060205 Debian/1.7.12-1.1",\
        "Mozilla/5.0 (X11; U; Linux i686; cs-CZ; rv:1.7.12) Gecko/20050929",\
        "Mozilla/5.0 (X11; U; AIX 5.3; en-US; rv:1.7.12) Gecko/20051025",\
        "More Mozilla 1.7.12 user agents strings -->>",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.7.11) Gecko/20050802",\
        "Mozilla/5.0 (Windows; U; WinNT4.0; de-AT; rv:1.7.11) Gecko/20050728",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.11) Gecko/20050728",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.7.11) Gecko/20050728",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.7.11) Gecko/20050728",\
        "Mozilla/5.0 (Windows; U; Win 9x 4.90; de-AT; rv:1.7.11) Gecko/20050728",\
        "Mozilla 1.7.10",\
        "Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.7.10) Gecko/20050727",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.10) Gecko/20050716",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.7.1) Gecko/20040707",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.7.1) Gecko/20040707",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7.1) Gecko/20040707",\
        "Mozilla 1.7.0.13",\
        "Mozilla 1.7",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; fr-FR; rv:1.7) Gecko/20040621",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.7) Gecko/20060120",\
        "Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.7) Gecko/20060627",\
        "Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.7) Gecko/20051027",\
        "Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.7) Gecko/20041221",\
        "Mozilla/5.0 (X11; U; FreeBSD; i386; it-IT; rv:1.7) Gecko",\
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.7) Gecko/20040616",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7) Gecko/20040616",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.7) Gecko/20040616",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.7) Gecko/20040616",\
        "Mozilla 1.6a",\
        "Mozilla 1.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040413 Debian/1.6-5",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040113",\
        "Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.6) Gecko/20040115",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; hu; rv:1.6) Gecko/20040113",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.6) Gecko/20040113",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.6) Gecko/20040113",\
        "Mozilla/5.0 (Photon; U; QNX x86pc; en-US; rv:1.6) Gecko/20040429",\
        "Mozilla 1.5b",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.5b) Gecko/20030827",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.5a) Gecko/20030718",\
        "Mozilla 1.5.1",\
        "Mozilla 1.5",\
        "Mozilla/5.0 (X11; U; Linux i686; fr-FR; rv:1.5) Gecko/20031007",\
        "Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.5) Gecko/20031007",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.5) Gecko/20030916",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.5) Gecko/20031007",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.5) Gecko/20031007",\
        "Mozilla 1.4b",\
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.4b) Gecko/20030507",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.4b) Gecko/20030427",\
        "Mozilla 1.4a",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.4a) Gecko/20030401",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.4a) Gecko/20030401",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.4a) Gecko/20030401",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.4a) Gecko/20030401",\
        "Mozilla/5.0 (X11; U; IRIX64 IP35; en-US; rv:1.4.3) Gecko/20040909",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.4.2) Gecko/20040220",\
        "Mozilla/5.0 (X11; U; Linux i686; zh-CN; rv:1.4.1) Gecko/20031114",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.4.1) Gecko/20031114",\
        "Mozilla 1.4",\
        "Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.4) Gecko/20030714 Debian/1.4-2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.4) Gecko/20030828",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.4) Gecko/20030821",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.4) Gecko/20030723",\
        "Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.4) Gecko/20030812",\
        "Mozilla/5.0 (X11; U; Linux i586; de-AT; rv:1.4) Gecko/20030908 Debian/1.4-4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.4) Gecko/20030624",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.4) Gecko/20030624",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.4) Gecko/20030624",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.4) Gecko/20030529",\
        "Mozilla 1.3b",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.3b) Gecko/20030125",\
        "Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.3b) Gecko/20030210",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.3b) Gecko/20030210",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.3b) Gecko/20030204",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.3b) Gecko/20030210",\
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.3a) Gecko/20021212",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.3a) Gecko/20021212",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.3a) Gecko/20021212",\
        "Mozilla 1.3.1",\
        "Mozilla/5.0 (X11; U; Linux i686; hu-HU; rv:1.3.1) Gecko",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.3.1) Gecko/20030425",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.3.1) Gecko/20030425",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.3.1) Gecko/20030425",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.3.1) Gecko/20030425",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.3) Gecko/20030318",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.3) Gecko/20030413",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.3) Gecko/20030327 Debian/1.3-4",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.3) Gecko/20030320",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.3) Gecko/20030313",\
        "Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.3) Gecko/20030430 Debian/1.3-5",\
        "Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.3) Gecko/20030312",\
        "Mozilla/5.0 (X11; U; HP-UX 9000/785; en-US; rv:1.3) Gecko/20030321",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.3) Gecko/20030312",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.3) Gecko/20030312",\
        "More Mozilla 1.3 user agents strings -->>",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.2b) Gecko/20021016",\
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021016",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.2b) Gecko/20021016",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US; rv:1.2b) Gecko/20021016",\
        "Mozilla 1.2a",\
        "Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.2a) Gecko/20020910",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.2a) Gecko/20020910",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.2a) Gecko/20020910",\
        "Mozilla/5.0 (Macintosh; U; PPC; en-US; rv:1.2a) Gecko/20020910",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.2.1) Gecko/20030711",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.2.1) Gecko/20021212",\
        "Mozilla/5.0 (X11; U; Linux i686;en-US; rv:1.2.1) Gecko/20030225",\
        "Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.2.1) Gecko/20021130",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.2.1) Gecko/20030409 Debian/1.2.1-9woody2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.2.1) Gecko/20030113",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.2.1) Gecko/20021208 Debian/1.2.1-2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.2.1) Gecko/20021203",\
        "Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.2.1) Gecko/20021226 Debian/1.2.1-9",\
        "Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.2.1) Gecko/20021130",\
        "More Mozilla 1.2.1 user agents strings -->>",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.2) Gecko/20021202",\
        "Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.2) Gecko/20021203",\
        "Mozilla/5.0 (X11; U; HP-UX 9000/785; en-US; rv:1.2) Gecko/20021203",\
        "Mozilla/5.0 (Windows; U; WinNT4.0; de-AT; rv:1.2) Gecko/20021126",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.2) Gecko/20021126",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US; rv:1.2) Gecko/20021126",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.1b) Gecko/20020722",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.1b) Gecko/20020721",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.1a) Gecko/20020610",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.1a) Gecko/20020611",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US; rv:1.1a) Gecko/20020610",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.1a) Gecko/20020611",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.1) Gecko/20020925",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.1) Gecko/20020827",\
        "Mozilla/5.0 (X11; U; Linux i686; it-IT; rv:1.1) Gecko/20020826",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.1) Gecko/20020829",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.1) Gecko/20020826",\
        "Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.1) Gecko/20020826",\
        "Mozilla/5.0 (X11; U; Linux i386; en-US; rv:1.1) Gecko/20020826",\
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.1) Gecko/20020826",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.1) Gecko/20020826",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; fr-FR; rv:1.1) Gecko/20020826",\
        "More Mozilla 1.1 user agents strings -->>",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0rc3) Gecko/20020529 Debian/1.0rc3-1",\
        "Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.0rc3) Gecko/20020523",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0rc2) Gecko/20020510",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.0rc2) Gecko/20020510",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.0rc2) Gecko/20020510",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.0rc2) Gecko/20020510",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.0rc1) Gecko/20020417",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.2) Gecko/20030716",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.0.2) Gecko/20021216",\
        "Mozilla 1.0.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.1) Gecko/20021122 Debian/1.0.1-2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.1) Gecko/20021003",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.1) Gecko/20020918",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.1) Gecko/20020903",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.1) Gecko/20020826",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.0.1) Gecko/20020826",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.0.1) Gecko/20020815",\
        "Mozilla/5.0 (Windows; U; Win 9x 4.90; en-US; rv:1.0.1) Gecko/20020826",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.1) Gecko/20020830",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.0.1) Gecko/20020826",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.0.0) Gecko/20020611",\
        "Mozilla/5.0 (X11; U; Linux i686; fr-FR; rv:1.0.0) Gecko/20020623 Debian/1.0.0-0.woody.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.0) Gecko/20020623 Debian/1.0.0-0.woody.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.0) Gecko/20020605",\
        "Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.0.0) Gecko/20020615 Debian/1.0.0-3",\
        "Mozilla/5.0 (X11; U; HP-UX 9000/785; en-US; rv:1.0.0) Gecko/20020605",\
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.0.0) Gecko/20020530",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.0.0) Gecko/20020530",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.0.0) Gecko/20020530",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.0.0) Gecko/20020530",\
        "More Mozilla 1.0.0 user agents strings -->>",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.9) Gecko/20020513",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.9) Gecko/20020408",\
        "Mozilla/5.0 (X11; U; Linux i586; en-US; rv:0.9.9) Gecko/20020513",\
        "Mozilla 0.9.8",\
        "Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:0.9.8) Gecko/20020204",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.8) Gecko/20020204",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:0.9.7) Gecko/20011221",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.6) Gecko/20011202",\
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:0.9.5) Gecko/20011011",\
        "Mozilla 0.9.4",\
        "Mozilla 0.9.3",\
        "Mozilla/5.0 (Macintosh; U; PPC; en-US; rv:0.9.3) Gecko/20010802",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.2.1) Gecko/20010901",\
        "Mozilla 0.9.2",\
        "Mozilla",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; cs; rv:1.9.2.6) Gecko/20100628 myibrow/4alpha2",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; MyIE2; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; MyIE2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; WinFX RunTime 3.0.50727)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; MyIE2; InfoPath.1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; MyIE2; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; MyIE2; .NET CLR 1.1.4322; Alexa Toolbar; .NET CLR 2.0.50727)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; MyIE2; InfoPath.1)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; MyIE2; .NET CLR 1.1.4322)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; MyIE2)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Q312461; MyIE2)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; MyIE2; SV1; iebar)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2a2pre) Gecko/20090908 Ubuntu/9.04 (jaunty) Namoroka/3.6a2pre GTB5 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2a2pre) Gecko/20090824 Ubuntu/9.10 (karmic) Namoroka/3.6a2pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; cs-CZ; rv:1.9.2a2pre) Gecko/20090826 Namoroka/3.6a2pre",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2a2pre) Gecko/20090906 Ubuntu/9.04 (jaunty) Namoroka/3.6a2pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2a2pre) Gecko/20090918 Namoroka/3.6a2pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; cs; rv:1.9.2a2pre) Gecko/20090912 Namoroka/3.6a2pre (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2a2pre) Gecko/20090826 Namoroka/3.6a2pre",\
        "Mozilla/5.0 (X11; U; Linux i686; pl; rv:1.9.2a1) Gecko/20090806 Namoroka/3.6a1 (Debian GNU/Linux Sid)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2a1) Gecko/20090806 Namoroka/3.6a1 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2a1) Gecko/20090806 Namoroka/3.6a1 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2a1) Gecko/20090806 Namoroka/3.6a1 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.2a1) Gecko/20090806 Namoroka/3.6a1",\
        "Mozilla/5.0 (X11; U; Linux x86_64; it; rv:1.9.2.9pre) Gecko/20100818 Ubuntu/10.04 (lucid) Namoroka/3.6.9pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100805 Namoroka/3.6.8",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.5pre) Gecko/20100526 Ubuntu/10.04 (lucid) Namoroka/3.6.5pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.3pre) Gecko/20100324 Ubuntu/9.04 (jaunty) Namoroka/3.6.3pre",\
        "Mozilla/5.0 (X11; U; NetBSD i386; en-US; rv:1.9.2.3) Gecko/20100403 Namoroka/3.6.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2.3) Gecko/20100405 Namoroka/3.6.3 ( .NET CLR 3.5.30729)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.2pre) Gecko/20100306 Namoroka/3.6.2pre",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100315 Ubuntu/9.10 (karmic) Namoroka/3.6.2pre",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100129 Ubuntu/9.10 (karmic) Namoroka/3.6.2pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.9.2.20pre) Gecko/20110718 Namoroka/3.6.20pre ( )",\
        "Mozilla/5.0 (X11; U; Linux x86_64; ru; rv:1.9.2.18pre) Gecko/20110419 Ubuntu/10.04 (lucid) Namoroka/3.6.18pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.18pre) Gecko/20110515 Ubuntu/9.10 (karmic) Namoroka/3.6.18pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.18pre) Gecko/20110419 Ubuntu/10.10 (maverick) Namoroka/3.6.18pre",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.18pre) Gecko/20110509 Ubuntu/10.10 (maverick) Namoroka/3.6.18pre",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.18pre) Gecko/20110419 Ubuntu/10.10 (maverick) Namoroka/3.6.18pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.9.2.18pre) Gecko/20110610 Namoroka/3.6.18pre ( )",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.9.2.17pre) Gecko/20110322 Ubuntu/10.10 (maverick) Namoroka/3.6.17pre",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.17pre) Gecko/20110401 Ubuntu/10.04 (lucid) Namoroka/3.6.17Pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.2.17) Gecko/20110415 Ubuntu/10.10 (maverick) Namoroka/3.6.17",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-TW; rv:1.9.2.15pre) Gecko/20110127 Namoroka/3.6.15pre (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.14pre) Gecko/20110111 Ubuntu/8.04 (hardy) Namoroka/3.6.14pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.12pre) Gecko/20101011 Ubuntu/10.04 (lucid) Namoroka/3.6.12pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.10pre) Gecko/20100826 Ubuntu/9.04 (jaunty) Namoroka/3.6.10pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.10) Gecko/20100928 Namoroka/3.6.10",\
        "Mozilla/5.0 (X11; U; Linux i686; pt-BR) AppleWebKit/533.3 (KHTML, like Gecko) Navscape/Pre-0.2 Safari/533.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR) AppleWebKit/534.12 (KHTML, like Gecko) NavscapeNavigator/Pre-0.1 Safari/534.12",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; de-de) AppleWebKit/531.22.7 (KHTML, like Gecko) NetNewsWire/3.2.7",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; de-de) AppleWebKit/525.28.3 (KHTML, like Gecko) NetNewsWire/3.1.7",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_5; en-us) AppleWebKit/525.18 (KHTML, like Gecko) NetNewsWire/3.1.7",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/418.8 (KHTML, like Gecko) NetNewsWire/2.1.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr) AppleWebKit/417.9 (KHTML, like Gecko) NetNewsWire/2.0.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/417.9 (KHTML, like Gecko) NetNewsWire/2.0",\
        "Mozilla/3.0 (compatible; NetPositive/2.2)",\
        "Mozilla/5.0 (Windows; U; Win 9x 4.90; SG; rv:1.9.2.4) Gecko/20101104 Netscape/9.1.0285",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1.8pre) Gecko/20070928 Firefox/2.0.0.7 Navigator/9.0RC1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.7pre) Gecko/20070815 Firefox/2.0.0.6 Navigator/9.0b3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.7pre) Gecko/20070815 Firefox/2.0.0.6 Navigator/9.0b3",\
        "Mozilla/5.0 (Windows; U; Windows 98; en-US; rv:1.8.1.5pre) Gecko/20070710 Firefox/2.0.0.4 Navigator/9.0b2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.11pre) Gecko/20071206 Firefox/2.0.0.11 Navigator/9.0.0.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.11pre) Gecko/20071206 Firefox/2.0.0.11 Navigator/9.0.0.5",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1.11pre) Gecko/20071206 Firefox/2.0.0.11 Navigator/9.0.0.5",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1.10pre) Gecko/20071127 Firefox/2.0.0.10 Navigator/9.0.0.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.9pre) Gecko/20071102 Firefox/2.0.0.9 Navigator/9.0.0.3",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1.9pre) Gecko/20071102 Firefox/2.0.0.9 Navigator/9.0.0.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.8.1.8pre) Gecko/20071019 Firefox/2.0.0.8 Navigator/9.0.0.1",\
        "Mozilla/5.0 (Windows; U; Windows 98; en-US; rv:1.8.1.8pre) Gecko/20071019 Firefox/2.0.0.8 Navigator/9.0.0.1",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1.8pre) Gecko/20071019 Firefox/2.0.0.8 Navigator/9.0.0.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.5) Gecko/20070321 Netscape/9.0",\
        "Mozilla/5.0 (Windows; U; Win 9x 4.90; en-US; rv:1.8.1.8pre) Gecko/20071015 Firefox/2.0.0.7 Navigator/9.0",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.5) Gecko/20070321 Netscape/8.1.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.7.5) Gecko/20060912 Netscape/8.1.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; es-AR; rv:1.7.5) Gecko/20060912 Netscape/8.1.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.5) Gecko/20060127 Netscape/8.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; es-ES; rv:1.7.5) Gecko/20060127 Netscape/8.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.5) Gecko/20060111 Netscape/8.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7.5) Gecko/20060127 Netscape/8.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.5) Gecko/20051012 Netscape/8.0.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.5) Gecko/20050817 Netscape/8.0.3.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7.5) Gecko/20050729 Netscape/8.0.3.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7.5) Gecko/20050603 Netscape/8.0.2",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.7.5) Gecko/20050603 Netscape/8.0.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.5) Gecko/20050519 Netscape/8.0.1 FirePHP/0.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7.5) Gecko/20050519 Netscape/8.0.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.2) Gecko/20040805 Netscape/7.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7.2) Gecko/20040804 Netscape/7.2 (ax)",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.7.2) Gecko/20040804 Netscape/7.2 (ax)",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; rv:1.7.2) Gecko/20040804 Netscape/7.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.4) Gecko/20030624 Netscape/7.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr-FR; rv:1.4) Gecko/20030624 Netscape/7.1 (ax)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-CA; rv:1.4) Gecko/20030624 Netscape/7.1 (ax)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.4) Gecko/20030619 Netscape/7.1 (ax)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:1.4) Gecko/20030624 Netscape/7.1 (ax)",\
        "Mozilla/5.0 (Windows; U; Win98; ja-JP; rv:1.4) Gecko/20030624 Netscape/7.1 (ax)",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko/20030624 Netscape/7.1 (ax)",\
        "Mozilla/5.0 (Windows; U; Win98; de-DE; rv:1.4) Gecko/20030619 Netscape/7.1 (ax)",\
        "Mozilla/5.0 (Windows; U; Win 9x 4.90; en-US; rv:1.4) Gecko/20030624 Netscape/7.1 (ax)",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.4) Gecko/20030624 Netscape/7.1",\
        "Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:1.0.2) Gecko/20030208 Netscape/7.02",\
        "Mozilla/5.0 (Windows; U; WinNT4.0; de-DE; rv:1.0.2) Gecko/20030208 Netscape/7.02",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.0.2) Gecko/20030208 Netscape/7.02",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; fr-FR; rv:1.0.2) Gecko/20030208 Netscape/7.02 (ax)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:1.0.2) Gecko/20030208 Netscape/7.02",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.0.2) Gecko/20030208 Netscape/7.02",\
        "Mozilla/5.0 (Windows; U; Win95; de-DE; rv:1.0.2) Gecko/20030208 Netscape/7.02",\
        "Mozilla/5.0 (Macintosh; U; PPC; ja-JP; rv:1.0.2) Gecko/20030208 Netscape/7.02",\
        "Mozilla/5.0 (Macintosh; U; PPC; en-US; rv:1.0.2) Gecko/20030208 Netscape/7.02",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-FR; rv:1.0.2) Gecko/20030208 Netscape/7.02",\
        "Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:1.0.2) Gecko/20021120 Netscape/7.01",\
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.0.2) Gecko/20021120 Netscape/7.01",\
        "Mozilla/5.0 (Windows; U; WinNT4.0; de-AT; rv:1.0.2) Gecko/20021120 Netscape/7.01",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.0.2) Gecko/20021120 Netscape/7.01",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; ja-JP; rv:1.0.2) Gecko/20021120 Netscape/7.01",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:1.0.2) Gecko/20021120 Netscape/7.01",\
        "Mozilla/5.0 (Windows; U; Win98; de-DE; rv:1.0.2) Gecko/20021120 Netscape/7.01",\
        "Mozilla/5.0 (Windows; U; Win 9x 4.90; de-DE; rv:1.0.2) Gecko/20021120 Netscape/7.01",\
        "Mozilla/5.0 (Macintosh; U; PPC; en-US; rv:1.0.2) Gecko/20021120 Netscape/7.01",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US; rv:1.0.2) Gecko/20021120 Netscape/7.01",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr-FR; rv:1.0rc2) Gecko/20020512 Netscape/7.0b1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.0rc2) Gecko/20020512 Netscape/7.0b1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:1.0rc2) Gecko/20020512 Netscape/7.0b1",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.0.1) Gecko/20020921 Netscape/7.0",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.0.1) Gecko/20020719 Netscape/7.0",\
        "Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:1.0.1) Gecko/20020823 Netscape/7.0",\
        "Mozilla/5.0 (X11; U; HP-UX 9000/785; es-ES; rv:1.0.1) Gecko/20020827 Netscape/7.0",\
        "Mozilla/5.0 (Windows; U; WinNT4.0; fr-FR; rv:1.0.1) Gecko/20020823 Netscape/7.0",\
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-GB; rv:1.0.1) Gecko/20020823 Netscape/7.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr-FR; rv:1.0.1) Gecko/20020823 Netscape/7.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.0.1) Gecko/20020823 Netscape/7.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; pt-BR; rv:1.0.1) Gecko/20020823 Netscape/7.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.0.1) Gecko/20020823 Netscape/7.0",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:0.9.4.1) Gecko/20020518 Netscape6/6.2.3",\
        "Mozilla/5.0 (X11; U; OSF1 alpha; en-US; rv:0.9.4.1) Gecko/20020517 Netscape6/6.2.3",\
        "Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:0.9.4.1) Gecko/20020508 Netscape6/6.2.3",\
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:0.9.4.1) Gecko/20020508 Netscape6/6.2.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:0.9.4.1) Gecko/20020508 Netscape6/6.2.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:0.9.4.1) Gecko/20020508 Netscape6/6.2.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; it-IT; rv:0.9.4.1) Gecko/20020508 Netscape6/6.2.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-GB; rv:0.9.4.1) Gecko/20020508 Netscape6/6.2.3",\
        "Mozilla/5.0 (Windows; U; Win98; fr-FR; rv:0.9.4.1) Gecko/20020508 Netscape6/6.2.3",\
        "Mozilla/5.0 (Windows; U; Win98; de-DE; rv:0.9.4.1) Gecko/20020508 Netscape6/6.2.3",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:0.9.4.1) Gecko/20020406 Netscape6/6.2.2",\
        "Mozilla/5.0 (Windows; U; WinNT4.0; de-DE; rv:0.9.4.1) Gecko/20020314 Netscape6/6.2.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; fr-FR; rv:0.9.4.1) Gecko/20020314 Netscape6/6.2.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:0.9.4.1) Gecko/20020314 Netscape6/6.2.2",\
        "Mozilla/5.0 (Windows; U; Win 9x 4.90; en-US; rv:0.9.4.1) Gecko/20020314 Netscape6/6.2.2",\
        "Mozilla/5.0 (Macintosh; U; PPC; en-US; rv:0.9.4.1) Gecko/20020318 Netscape6/6.2.2",\
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:0.9.4.1) Gecko/20020314 Netscape6/6.2.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:0.9.4.1) Gecko/20020314 Netscape6/6.2.2",\
        "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:0.9.4) Gecko/20011206 Netscape6/6.2.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.4) Gecko/20011126 Netscape6/6.2.1",\
        "Mozilla/5.0 (Windows; U; WinNT4.0; fr-FR; rv:0.9.4) Gecko/20011128 Netscape6/6.2.1",\
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-CA; rv:0.9.4) Gecko/20011128 Netscape6/6.2.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr-FR; rv:0.9.4) Gecko/20011128 Netscape6/6.2.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:0.9.4) Gecko/20011128 Netscape6/6.2.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:0.9.4) Gecko/20011128 Netscape6/6.2.1",\
        "Mozilla/5.0 (Windows; U; Win98; fr-FR; rv:0.9.4) Gecko/20011128 Netscape6/6.2.1",\
        "Mozilla/5.0 (Windows; U; Win98; en-GB; rv:0.9.4) Gecko/20011128 Netscape6/6.2.1",\
        "Mozilla/5.0 (Windows; U; Win 9x 4.90; fr-FR; rv:0.9.4) Gecko/20011128 Netscape6/6.2.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.4) Gecko/20011022 Netscape6/6.2",\
        "Mozilla/5.0 (Windows; U; WinNT4.0; de-DE; rv:0.9.4) Gecko/20011019 Netscape6/6.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:0.9.4) Gecko/20011019 Netscape6/6.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:0.9.4) Gecko/20011019 Netscape6/6.2",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:0.9.4) Gecko/20011019 Netscape6/6.2",\
        "Mozilla/5.0 (Windows; U; Win95; en-GB; rv:0.9.4) Gecko/20011019 Netscape6/6.2",\
        "Mozilla/5.0 (Windows; U; Win 9x 4.90; de-DE; rv:0.9.4) Gecko/20011019 Netscape6/6.2",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:0.9.1) Gecko/20010607 Netscape6/6.1b1",\
        "Mozilla/5.0 (Windows; U; WinNT4.0; fr-FR; rv:0.9.2) Gecko/20010726 Netscape6/6.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:0.9.2) Gecko/20010726 Netscape6/6.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; fr-FR; rv:0.9.2) Gecko/20010726 Netscape6/6.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:0.9.2) Gecko/20010726 Netscape6/6.1",\
        "Mozilla/5.0 (Windows; U; Win95; de-DE; rv:0.9.2) Gecko/20010726 Netscape6/6.1",\
        "Mozilla/5.0 (Macintosh; U; PPC; de-DE; rv:0.9.2) Gecko/20010726 Netscape6/6.1",\
        "Mozilla/5.0 (Windows; U; WinNT4.0; de-DE; rv:0.9.2) Gecko/20010726 Netscape6/6.1",\
        "Mozilla/5.0 (Macintosh; U; PPC; en-US; rv:0.9.2) Gecko/20010726 Netscape6/6.1",\
        "Mozilla/4.8C-SGI [en] (X11; U; IRIX64 6.5 IP27)",\
        "Mozilla/4.8 [nl] (Windows NT 6.0; U)",\
        "Mozilla/4.8 [en] (X11; U; SunOS 5.8 sun4u)",\
        "Mozilla/4.8 [en] (X11; U; Linux 2.6.12-1.1372_FC3 i686; Nav)",\
        "Mozilla/4.8 [en] (X11; U; IRIX64 6.5 IP27)",\
        "Mozilla/4.8 [en] (WinNT; U)",\
        "Mozilla/4.8 [en] (Windows NT 6.0; U)",\
        "Mozilla/4.8 [en] (Windows NT 5.1; U)",\
        "Mozilla/4.8 [en] (Win98; U)",\
        "Mozilla/4.8 [en] (FreeBSD; U)",\
        "Mozilla/4.8 [de] (X11; U; Linux 2.4.20-4GB i686)",\
        "Mozilla/4.79C-SGI [en] (X11; I; IRIX64 6.5 IP28)",\
        "Mozilla/4.79 [fr] (X11; U; Linux 2.4.18-27.7.xcustom i686)",\
        "Mozilla/4.79 [en] (X11; U; SunOS 5.8 sun4u)",\
        "Mozilla/4.79 [en] (X11; U; SunOS 5.6 sun4u)",\
        "Mozilla/4.79 [en] (X11; U; Linux 2.4.21-pre5 i686)",\
        "Mozilla/4.79 [en] (X11; U; Linux 2.4.2 i386)",\
        "Mozilla/4.79 [en] (X11; U; Linux 2.4.18-5 i686)",\
        "Mozilla/4.79 [en] (X11; U; Linux 2.4.18-10 i686)",\
        "Mozilla/4.79 [en] (X11; U; Linux 2.2.19-6.2.16 i686)",\
        "Mozilla/4.79 [en] (WinNT; U)",\
        "Mozilla/4.79 [en] (Win98; U)",\
        "Mozilla/4.78 [fr] (X11; U; Linux 2.4.8-26mdk i686)",\
        "Mozilla/4.78 [fr] (X11; U; Linux 2.4.7-10 i686)",\
        "Mozilla/4.78 [fr] (Windows NT 5.0; U)",\
        "Mozilla/4.78 [fr] (Win95; U)",\
        "Mozilla/4.78 [es] (Win98; U)",\
        "Mozilla/4.78 [en] (X11; U; SunOS 5.8 sun4u; Nav)",\
        "Mozilla/4.78 [en] (X11; U; SunOS 5.7 sun4u)",\
        "Mozilla/4.78 [en] (X11; U; Linux 2.4.9-21 i686)",\
        "Mozilla/4.78 [en] (X11; U; Linux 2.4.20-18.7 i686)",\
        "Mozilla/4.78 [en] (X11; U; Linux 2.4.2 i386)",\
        "Mozilla/4.77C-SGI [en] (X11; I; IRIX64 6.5 IP30)",\
        "Mozilla/4.77 [fr] (X11; U; Linux 2.4.4-4GB i686)",\
        "Mozilla/4.77 [fr] (X11; U; Linux 2.4.17 i686; Nav)",\
        "Mozilla/4.77 [en] (X11; U; SunOS 5.7 sun4u)",\
        "Mozilla/4.77 [en] (X11; U; Linux 2.4.20-bf2.4 i686)",\
        "Mozilla/4.77 [en] (X11; U; Linux 2.4.19-acheron i686; Nav)",\
        "Mozilla/4.77 [en] (X11; U; Linux 2.4.18-386 i686)",\
        "Mozilla/4.77 [en] (X11; U; Linux 2.4.17-lsm i686)",\
        "Mozilla/4.77 [en] (X11; U; Linux 2.2.14 i686)",\
        "Mozilla/4.77 [en] (WinNT; U)",\
        "Mozilla/4.77 [en] (Win98; U)",\
        "Mozilla/4.76C-SGI [en] (X11; I; IRIX 6.5 IP32)",\
        "Mozilla/4.76 [en] (X11; U; SunOS 5.8 sun4u; Nav)",\
        "Mozilla/4.76 [en] (X11; U; SunOS 5.8 i86pc)",\
        "Mozilla/4.76 [en] (X11; U; Linux 2.4.5 i686)",\
        "Mozilla/4.76 [en] (X11; U; Linux 2.4.18p3 i686)",\
        "Mozilla/4.76 [en] (X11; U; Linux 2.2.19pre17 i686)",\
        "Mozilla/4.76 [en] (X11; U; Linux 2.2.16 i686)",\
        "Mozilla/4.76 [en] (WinNT; U)",\
        "Mozilla/4.76 [en] (Win95; U)",\
        "Mozilla/4.76 [de] (X11; U; Linux 2.4.0-4GB i686)",\
        "Mozilla/4.76 (X11; U; Linux 2.4.10-4GB i686)",\
        "Mozilla/4.75 [fr] (X11; U; Linux 2.2.16-3smp i686)",\
        "Mozilla/4.75 [fr] (WinNT; U)",\
        "Mozilla/4.75 [fr] (Win98; U)",\
        "Mozilla/4.75 [en] (X11; U; SunOS 5.8 sun4u)",\
        "Mozilla/4.75 [en] (X11; U; SunOS 5.6 sun4u)",\
        "Mozilla/4.75 [en] (X11; U; Linux 2.2.16-3 i686)",\
        "Mozilla/4.75 [en] (WinNT; U)",\
        "Mozilla/4.75 [en] (Win98; U)",\
        "Mozilla/4.75 [de] (WinNT; U)",\
        "Mozilla/4.75 [de] (Win98; U)",\
        "Mozilla/4.74 [en] (WinNT; U)",\
        "Mozilla/4.74 [en] (Win98; U)",\
        "Mozilla/4.74 [de] (X11; U; Linux 2.2.16 i686)",\
        "Mozilla/4.74 (Macintosh; U; PPC)",\
        "Mozilla/4.73 [en] (X11; U; SunOS 5.8 sun4u)",\
        "Mozilla/4.73 [en] (WinNT; U)",\
        "Mozilla/4.73 [en] (Windows NT 5.0; U)",\
        "Mozilla/4.73 [en] (Win98; U)",\
        "Mozilla/4.73 [en] (Win95; U)",\
        "Mozilla/4.73 [de] (WinNT; U)",\
        "Mozilla/4.73 [de] (Win98; U)",\
        "Mozilla/4.73 (Macintosh; U; PPC)",\
        "Mozilla/4.73 [en] (Win95; I)",\
        "Mozilla/4.72 [fr] (X11; U; Linux 2.2.14-5.0 i686)",\
        "Mozilla/4.72 [en] (X11; U; Linux 2.2.14-5.0 i686)",\
        "Mozilla/4.72 [en] (X11; I; Linux 2.2.14 i686)",\
        "Mozilla/4.72 [en] (X11; I; Linux 2.2.13 i586)",\
        "Mozilla/4.72 [en] (WinNT; U)",\
        "Mozilla/4.72 [en] (Windows NT 5.0; U)",\
        "Mozilla/4.72 [en] (Win98;I)",\
        "Mozilla/4.72 [en] (Win98; I)",\
        "Mozilla/4.72 [de] (WinNT; U)",\
        "Mozilla/4.72 [de] (Win95; U)",\
        "Mozilla/4.71 [en] (X11; U; Linux 2.0.36 i586)",\
        "Mozilla/4.71 [en] (Win98; I)",\
        "Mozilla/4.7 [fr] (WinNT; I)",\
        "Mozilla/4.7 [fr] (Win98; I)",\
        "Mozilla/4.7 [en] (X11; U; SunOS 5.6 sun4u)",\
        "Mozilla/4.7 [en] (X11; I; SunOS 5.7 sun4u)",\
        "Mozilla/4.7 [en] (X11; I; Linux 2.2.13 i686; Nav)",\
        "Mozilla/4.7 [en] (X11; I; Linux 2.2.12 i686; Nav)",\
        "Mozilla/4.7 [en] (WinNT; I)",\
        "Mozilla/4.7 [en] (Win98; I)",\
        "Mozilla/4.7 [en-gb] (WinNT; U)",\
        "Mozilla/4.7 [en-gb] (Win98; U)",\
        "Mozilla/4.61 [ja] (X11; I; Linux 2.6.13-33cmc1 i686)",\
        "Mozilla/4.61 [en] (X11; I; SunOS 5.6 sun4u)",\
        "Mozilla/4.61 [en] (WinNT; I)",\
        "Mozilla/4.61 [en] (Win95; I)",\
        "Mozilla/4.61 [en] (OS/2; I)",\
        "Mozilla/4.61 [de] (OS/2; I)",\
        "Mozilla/4.6 [fr] (WinNT; I)",\
        "Mozilla/4.6 [en] (X11; U; SunOS 5.8 sun4u)",\
        "Mozilla/4.6 [en] (X11; I; SunOS 5.5.1 sun4u; Nav)",\
        "Mozilla/4.6 [en] (Win98; I)",\
        "Mozilla/4.6 [de] (WinNT; I)",\
        "Mozilla/4.6 [de] (Win95; I)",\
        "Mozilla/4.6 (Macintosh; I; PPC)",\
        "Mozilla/4.51 [it] (Win98; U)",\
        "Mozilla/4.51 [en] (X11; I; Linux 2.2.7 i686)",\
        "Mozilla/4.51 [en] (WinNT; I)",\
        "Mozilla/4.51 [en] (Win95; I)",\
        "Mozilla/4.51 [de] (Win98; I)",\
        "Mozilla/4.51 (Macintosh; I; PPC)",\
        "Mozilla/4.5 [it] (Win98; I)",\
        "Mozilla/4.5 [fr] (Win95; I)",\
        "Mozilla/4.5 [fr] (Macintosh; I; PPC)",\
        "Mozilla/4.5 [en] (X11; I; SunOS 5.8 sun4u)",\
        "Mozilla/4.5 [en] (X11; I; SunOS 5.6 sun4u)",\
        "Mozilla/4.5 [en] (WinNT; U)",\
        "Mozilla/4.5 [en] (Win95; I)",\
        "Mozilla/4.5 [de] (Win98; I)",\
        "Mozilla/4.5 (Macintosh; U; PPC)",\
        "Mozilla/4.5 [en] (WinNT; I)",\
        "Mozilla/4.08 [en] (WinNT; U ;Nav)",\
        "Mozilla/4.08 [en] (Win98; I ;Nav)",\
        "Mozilla/4.08 (Macintosh; I; PPC, Nav)",\
        "Mozilla/4.07 [en] (X11; I; Linux 2.0.36 i586)",\
        "Mozilla/4.07 [en] (WinNT; I)",\
        "Mozilla/4.07 [de] (Win95; I)",\
        "Mozilla/4.07 [en] (X11; I; Linux 2.0.36 i586)",\
        "Mozilla/4.06 [hu] (Win98; I)",\
        "Mozilla/4.06 [en] (X11; I; Linux 2.0.35 i686)",\
        "Mozilla/4.06 [en] (WinNT; I ;Nav)",\
        "Mozilla/4.06 [de] (Win98; I)",\
        "Mozilla/4.06 (Win95; I)",\
        "Mozilla/4.05 [en] (Win95; I)",\
        "Mozilla/4.04 [fr] (Macintosh; I; PPC, Nav)",\
        "Mozilla/4.04 [en] (WinNT; U)",\
        "Mozilla/4.04 [en] (Win95; I ;Nav)",\
        "Mozilla/4.04 [en] (Win95; I ;Nav)",\
        "Mozilla/4.03 [fr] (Win95; U)",\
        "Mozilla/4.01 [de] (WinNT; I)",\
        "Mozilla/4.0 (compatible; Mozilla/5.0 ; Linux i686)",\
        "Mozilla/3.04Gold (Macintosh; I; PPC)",\
        "Mozilla/3.02 [en] (Windows NT 5.1; U)",\
        "Mozilla/3.01Gold (Macintosh; I; 68K)",\
        "Mozilla/3.01 (Macintosh; U; PPC)",\
        "Mozilla/3.0 (Win95; I)",\
        "Mozilla/3.0 (Macintosh; I; PPC)",\
        "Mozilla/2.02Gold (Win95; I)",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US) AppleWebKit/528.16 (KHTML, like Gecko, Safari/528.16) OmniWeb/v622.8.0.112941",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-US) AppleWebKit/530.18+(KHTML, like Gecko, Safari/528.16) OmniWeb/v622.8.0",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-US) AppleWebKit/528.16 (KHTML, like Gecko, Safari/528.16) OmniWeb/v622.8.0",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US) AppleWebKit/525.18 (KHTML, like Gecko, Safari/525.20) OmniWeb/v622.6.1.0.111015",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/531.21.8+(KHTML, like Gecko, Safari/528.16) Version/5.10.3 OmniWeb/622.14.0",\
        "Mozilla/5.0 (Macintosh; U; PowerPC Mac OS X 10_5_8; en-US) AppleWebKit/531.9+(KHTML, like Gecko, Safari/528.16) OmniWeb/v622.10.0",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/420+ (KHTML, like Gecko, Safari/420) OmniWeb/v605",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/420+ (KHTML, like Gecko, Safari/420) OmniWeb/v602",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/420+ (KHTML, like Gecko, Safari) OmniWeb/v595",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.60",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.15",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/85 (KHTML, like Gecko) OmniWeb/v496",\
        "Mozilla/4.5 (compatible; OmniWeb/4.2-v435.5; Mac_PowerPC)",\
        "Mozilla/4.5 (compatible; OmniWeb/4.1.1-v424.6; Mac_PowerPC)",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/522+ (KHTML, like Gecko) OmniWeb",\
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",\
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; de) Opera 11.51",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101213 Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01",\
        "Mozilla/5.0 (Windows NT 6.1; U; de; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01",\
        "Mozilla/5.0 (Windows NT 6.0; U; ja; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.00",\
        "Mozilla/5.0 (Windows NT 5.1; U; de; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.00",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; fr) Opera 11.00",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; en) Opera 11.00",\
        "Mozilla/5.0 (Windows NT 5.2; U; ru; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.70",\
        "Mozilla/5.0 (X11; Linux x86_64; U; de; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.62",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; en) Opera 10.62",\
        "Mozilla/5.0 (Windows NT 5.1; U; Firefox/5.0; en; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.53",\
        "Mozilla/5.0 (Windows NT 5.1; U; Firefox/3.5; en; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.53",\
        "Mozilla/5.0 (Windows NT 6.1; U; en-GB; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.51",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Linux i686; en) Opera 10.51",\
        "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686; de) Opera 10.10",\
        "Mozilla/5.0 (Linux i686 ; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.70",\
        "Mozilla/5.0 (Windows NT 5.1; U; en-GB; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.61",\
        "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux x86_64; en) Opera 9.60",\
        "Mozilla/5.0 (Windows NT 5.1; U; ; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.52",\
        "Mozilla/5.0 (X11; Linux i686; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.51",\
        "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.51",\
        "Mozilla/5.0 (Windows NT 5.1; U; de; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.51",\
        "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux x86_64; en) Opera 9.50",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; en) Opera 9.50",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9b3) Gecko/2008020514 Opera 9.5",\
        "Mozilla/5.0 (Windows NT 5.1; U; es-la; rv:1.8.0) Gecko/20060728 Firefox/1.5.0 Opera 9.27",\
        "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686; en) Opera 9.27",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; es-la) Opera 9.27",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 6.0; en) Opera 9.26",\
        "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.0) Gecko/20060728 Firefox/1.5.0 Opera 9.24",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Mac_PowerPC; en) Opera 9.24",\
        "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.0) Gecko/20060728 Firefox/1.5.0 Opera 9.22",\
        "Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1; zh-cn) Opera 8.65",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) Opera 8.65 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; PPC; 320x320)Opera 8.65 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; PPC; 240x320) Opera 8.65 [zh-cn]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; PPC; 240x320) Opera 8.65 [de]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; PPC) Opera 8.65 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; PPC; 240x320) Opera 8.60 [en]",\
        "Mozilla/5.0 (Windows NT 5.1; U; pl) Opera 8.54",\
        "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686; en) Opera 8.54",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; pl) Opera 8.54",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.54",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; da) Opera 8.54",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.54",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; sv) Opera 8.53",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.53",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; en) Opera 8.53",\
        "Mozilla/5.0 (Windows NT 5.1; U; en) Opera 8.52",\
        "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686; en) Opera 8.52",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.52",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.52",\
        "Mozilla/5.0 (Windows NT 5.1; U; ru) Opera 8.51",\
        "Mozilla/5.0 (Windows NT 5.1; U; en) Opera 8.51",\
        "Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.51",\
        "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686; en) Opera 8.51",\
        "Mozilla/5.0 (Windows NT 5.1; U; en) Opera 8.50",\
        "Mozilla/5.0 (Windows NT 5.0; U; de) Opera 8.50",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; en) Opera 8.50",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; sv) Opera 8.50",\
        "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686; en) Opera 8.02",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 8.02",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; de) Opera 8.02",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; de) Opera 8.02",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; ru) Opera 8.01",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 8.01",\
        "Mozilla/5.0 (Windows NT 5.1; U; en) Opera 8.0",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; IT) Opera 8.0",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 8.0",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; de) Opera 8.0",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; en) Opera 8.0",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 7.60",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98) Opera 7.54u1 [en]",\
        "Mozilla/5.0 (X11; Linux i686; U) Opera 7.54 [en]",\
        "Mozilla/5.0 (Windows NT 5.0; U) Opera 7.54 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686) Opera 7.54 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.54 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) Opera 7.54 [pl]",\
        "Mozilla/4.0 (compatible; MSIE 5.23; Mac_PowerPC) Opera 7.54 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows ME) Opera 7.53 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.52 [en]",\
        "Mozilla/4.78 (Windows NT 5.1; U) Opera 7.51 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.51 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.50 [ru]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) Opera 7.50 [ru]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98) Opera 7.50 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; ; Linux i686) Opera 7.50 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.23 [ru]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.23 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.23 [de]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) Opera 7.23 [de]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 4.0) Opera 7.23 [de]",\
        "Mozilla/5.0 (Windows NT 5.0; U) Opera 7.21 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) Opera 7.20 [de]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98) Opera 7.20 [de]",\
        "Mozilla/5.0 (Windows NT 5.0; U) Opera 7.11 [en]",\
        "Mozilla/4.78 (Windows NT 5.0; U) Opera 7.11 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.11 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) Opera 7.11 [fr]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) Opera 7.11 [de]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows ME) Opera 7.11 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.10 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 4.0) Opera 7.10 [de]",\
        "Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.6) Gecko/2009020911 Ubuntu/8.10 (intrepid) Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.1) Opera 7.03 [de]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.1) Opera 7.03 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.0) Opera 7.03 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows ME) Opera 7.03 [de]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows 98) Opera 7.03 [de]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.1) Opera 7.02 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 4.0) Opera 7.02 [de]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows 98) Opera 7.02 [en]",\
        "Mozilla/4.78 (Windows NT 5.0; U) Opera 7.01 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.1) Opera 7.01 [de]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows 98) Opera 7.01 [en]",\
        "Mozilla/5.0 (Windows 2000; U) Opera 7.0 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.1) Opera 7.0 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.0) Opera 7.0 [de]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows ME) Opera 7.0 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows 2000) Opera 7.0 [en]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.20-4GB i686) Opera 6.12 [de]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; UNIX) Opera 6.11 [fr]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.4 i686) Opera 6.11 [en]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.19-4GB i686) Opera 6.11 [en]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.18 i686) Opera 6.11 [de]",\
        "Mozilla/5.0 (Linux 2.4.18-ltsp-1 i686; U) Opera 6.1 [en]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.18-4GB i686) Opera 6.1 [de]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows XP) Opera 6.06 [fr]",\
        "Mozilla/5.0 (Windows XP; U) Opera 6.05 [de]",\
        "Mozilla/5.0 (Windows ME; U) Opera 6.05 [de]",\
        "Mozilla/4.78 (Windows 2000; U) Opera 6.04 [de]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows XP) Opera 6.04 [en]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 4.0) Opera 6.04 [en]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 6.04 [en]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows 2000) Opera 6.04 [de]",\
        "Mozilla/5.0 (Windows 2000; U) Opera 6.03 [en]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 6.03 [en]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.20-4GB i686) Opera 6.03 [en]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.18-4GB i686) Opera 6.03 [en]",\
        "Mozilla/5.0 (Windows 2000; U) Opera 6.02 [en]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 4.0) Opera 6.02 [en]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows 95) Opera 6.02 [de]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.20-686 i686) Opera 6.02 [en]",\
        "Mozilla/5.0 (Windows 2000; U) Opera 6.01 [en]",\
        "Mozilla/4.78 (Windows 2000; U) Opera 6.01 [en]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows XP) Opera 6.01 [et]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 4.0) Opera 6.01 [en]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 6.01 [en]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 6.01 [it]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 6.01 [en]",\
        "Mozilla/4.76 (Windows NT 4.0; U) Opera 6.0 [de]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows XP) Opera 6.0 [de]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 4.0) Opera 6.0 [de]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 6.0 [en]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 6.0 [en]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows 2000) Opera 6.0 [en]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows 2000) Opera 6.0 [de]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Mac_PowerPC) Opera 6.0 [de]",\
        "Mozilla/4.76 (Windows NT 4.0; U) Opera 5.12 [en]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.12 [it]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 5.12 [it]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 5.12 [de]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 4.0) Opera 5.11 [de]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 5.1) Opera 5.02 [en]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 5.02 [en]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.8 sun4u) Opera 5.0 [en]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Linux) Opera 5.0 [en]",\
        "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.0-4GB i686) Opera 5.0 [en]",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera",\
        "Browser based on Mozilla Firefox. Developed by Avant force, the developers of Avant Browser",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090722 Firefox/3.5.1 Orca/1.2 build 2",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.7) Gecko/2009030821 Firefox/3.0.7 Orca/1.1 build 2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.6) Gecko/2009022300 Firefox/3.0.6 Orca/1.1 build 1",\
        "Mozilla/1.10 [en] (Compatible; RISC OS 3.70; Oregano 1.10)",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:19.0) Gecko/20130308 Firefox/19.0 PaleMoon/19.0.2",\
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:15.0) Gecko/20120919 Firefox/15.1.1-x64 PaleMoon/15.1.1-x64",\
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:15.0) Gecko/20120912 Firefox/15.1-x64 PaleMoon/15.1-x64",\
        "Mozilla/5.0 (Windows NT 6.1; rv:15.0) Gecko/20120911 Firefox/15.1 PaleMoon/15.1",\
        "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:15.0) Gecko/20120819 Firefox/15.0-x64 PaleMoon/15.0-x64",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120819 Firefox/15.0 PaleMoon/15.0",\
        "Mozilla/5.0 (Windows NT 6.0; rv:15.0) Gecko/20120819 Firefox/15.0 PaleMoon/15.0",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.3) Gecko/20120728 Firefox/12.3r2 PaleMoon/12.3r2",\
        "Mozilla/5.0 (Windows NT 6.0; rv:12.3) Gecko/20120728 Firefox/12.3r2 PaleMoon/12.3r2",\
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:12.3) Gecko/20120714 Firefox/12.3-x64 PaleMoon/12.3-x64",\
        "Mozilla/5.0 (Windows NT 6.1; rv:12.3) Gecko/20120717 Firefox/12.3 PaleMoon/12.3",\
        "Mozilla/5.0 (Windows NT 6.0; rv:12.3) Gecko/20120717 Firefox/12.3 PaleMoon/12.3",\
        "Mozilla/5.0 (Windows NT 5.1; rv:12.3) Gecko/20120714 Firefox/12.3 PaleMoon/12.3",\
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:12.2.1) Gecko/20120616 Firefox/12.2.1-x64 PaleMoon/12.2.1-x64",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.2.1) Gecko/20120616 Firefox/13.0 PaleMoon/12.2.1",\
        "Mozilla/5.0 (Windows NT 6.1; rv:12.2.1) Gecko/20120616 Firefox/12.2.1 PaleMoon/12.2.1",\
        "Mozilla/5.0 (Windows NT 5.1; rv:12.2.1) Gecko/20120616 Firefox/12.2.1 PaleMoon/12.2.1",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:12.2) Gecko/20120605 Firefox/12.2 PaleMoon/12.2",\
        "Mozilla/5.0 (Windows NT 5.1; rv:12.2) Gecko/20120605 Firefox/12.2 PaleMoon/12.2",\
        "Mozilla/5.0 (Windows NT 6.0; rv:12.0) Gecko/20120424 Firefox/12.0 PaleMoon/12.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP; rv:1.9.2.8) Gecko/20100817 Firefox/3.6.8 (Palemoon/3.6.8a)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; sv-SE; rv:1.9.2.32) Gecko/20120529 Firefox/3.6.32 (Palemoon/3.6.32)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; it-IT; rv:1.9.2.32) Gecko/20120529 Firefox/3.6.32 (Palemoon/3.6.32)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.2.31) Gecko/20120408 Firefox/3.6.31 (Palemoon/3.6.31)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.30) Gecko/20120217 Firefox/3.6.30 (Palemoon/3.6.30)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ja-JP; rv:1.9.2.3) Gecko/20100403 Firefox/3.6.3 (Palemoon/3.6.3)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2.3) Gecko/20100403 Firefox/3.6.3 (Palemoon/3.6.3) (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP; rv:1.9.2.3) Gecko/20100403 Firefox/3.6.3 (Palemoon/3.6.3) (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.3) Gecko/20100403 Firefox/3.6.3 (Palemoon/3.6.3)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.2) Gecko/20100324 Firefox/3.6.2 (Palemoon/3.6.2) (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101211 Firefox/3.6.13 (Palemoon/3.6.13) GTB7.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.11) Gecko/20101023 Firefox/3.6.11 (Palemoon/3.6.11) ( .NET CLR 3.5.30729; .NET4.0E)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP; rv:1.9.2) Gecko/20100206 Palemoon/3.6.0.5 (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2) Gecko/20100206 Palemoon/3.6.0.5",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.3a) Gecko/20021207 Phoenix/0.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.4a) Gecko/20030411 Phoenix/0.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.3a) Gecko/20021207 Phoenix/0.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.3a) Gecko/20030105 Phoenix/0.5",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.3a) Gecko/20021207 Phoenix/0.5",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.2b) Gecko/20021029 Phoenix/0.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.2b) Gecko/20021029 Phoenix/0.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.2b) Gecko/20021029 Phoenix/0.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.2b) Gecko/20021014 Phoenix/0.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2",\
        "Mozilla Firefox based 3D web browser by AT&T and Vizible. Discontinued",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.3) Gecko/20100402 Prism/1.0b4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2pre) Gecko/20100115 Prism/1.0b3",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.17) Gecko/2010010604 prism/0.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/527+ (KHTML, like Gecko) QtWeb Internet Browser/3.0 http://www.QtWeb.net",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527+ (KHTML, like Gecko) QtWeb Internet Browser/1.7 http://www.QtWeb.net",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/527+ (KHTML, like Gecko) QtWeb Internet Browser/1.7 http://www.QtWeb.net",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/527+ (KHTML, like Gecko) QtWeb Internet Browser/1.5 http://www.QtWeb.net",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/523.15 (KHTML, like Gecko) QtWeb Internet Browser/1.2 http://www.QtWeb.net",\
        "Mozilla/5.0 (X11; U; Linux x86_64; cs-CZ) AppleWebKit/533.3 (KHTML, like Gecko) rekonq Safari/533.3",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB) AppleWebKit/533.3 (KHTML, like Gecko) rekonq Safari/533.3",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.484 Chrome/11.0.696.71 Safari/534.24",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.478 Chrome/11.0.696.71 Safari/534.24",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.423 Chrome/11.0.696.71 Safari/534.24",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.390 Chrome/11.0.696.71 Safari/534.24",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.56.357 Chrome/11.0.696.71 Safari/534.24",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.56.357 Chrome/11.0.696.71 Safari/534.24",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_6) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.56.357 Chrome/11.0.696.71 Safari/534.24",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.56.310 Chrome/11.0.696.68 Safari/534.24",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.56.310 Chrome/11.0.696.68 Safari/534.24",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.56.292 Chrome/11.0.696.68 Safari/534.24",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.56.283 Chrome/11.0.696.65 Safari/534.24",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) RockMelt/0.9.50.549 Chrome/10.0.648.205 Safari/534.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) RockMelt/0.9.50.549 Chrome/10.0.648.205 Safari/534.16",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-US) AppleWebKit/534.16 (KHTML, like Gecko) RockMelt/0.9.50.549 Chrome/10.0.648.205 Safari/534.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) RockMelt/0.9.50.518 Chrome/10.0.648.205 Safari/534.16",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-US) AppleWebKit/534.16 (KHTML, like Gecko) RockMelt/0.9.50.518 Chrome/10.0.648.205 Safari/534.16",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) RockMelt/0.9.50.459 Chrome/10.0.648.204 Safari/534.16",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.13 (KHTML, like Gecko) RockMelt/0.9.48.59 Chrome/9.0.597.107 Safari/534.13",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.13 (KHTML, like Gecko) RockMelt/0.9.48.59 Chrome/9.0.597.107 Safari/534.13",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.13 (KHTML, like Gecko) RockMelt/0.9.48.58 Chrome/9.0.597.107 Safari/534.13",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-US) AppleWebKit/534.13 (KHTML, like Gecko) RockMelt/0.9.48.51 Chrome/9.0.597.107 Safari/534.13",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.13 (KHTML, like Gecko) RockMelt/0.9.46.126 Chrome/9.0.597.107 Safari/534.13",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.10 (KHTML, like Gecko) RockMelt/0.8.40.147 Chrome/8.0.552.231 Safari/534.10",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-US) AppleWebKit/534.10 (KHTML, like Gecko) RockMelt/0.8.40.147 Chrome/8.0.552.231 Safari/534.10",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.7 (KHTML, like Gecko) RockMelt/0.8.36.79 Chrome/7.0.517.44 Safari/534.7",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-US) AppleWebKit/534.7 (KHTML, like Gecko) RockMelt/0.8.36.74 Chrome/7.0.517.44 Safari/534.7",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.7 (KHTML, like Gecko) RockMelt/0.8.36.128 Chrome/7.0.517.44 Safari/534.7",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) RockMelt/0.8.36.116 Chrome/7.0.517.44 Safari/534.7",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) RockMelt/0.8.36.116 Chrome/7.0.517.44 Safari/534.7",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.7 (KHTML, like Gecko) RockMelt/0.8.36.116 Chrome/7.0.517.44 Safari/534.7",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; ha) AppleWebKit/534.13 (KHTML, like Gecko) RockMelt/0.445.436.1326 Chrome/12.0.632.107 Safari/534.13",\
        "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; de-at) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; tr-TR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; fr-FR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; cs-CZ) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; ja-jp) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; ko-kr) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; it-it) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; es-es) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-gb) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; sv-SE) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; it-IT) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-us) AppleWebKit/534.16+ (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; de-de) AppleWebKit/534.15+ (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",\
        "Mozilla/5.0 (Android 2.2; Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; nb-NO) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-TW) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; zh-cn) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",\
        "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5",\
        "Mozilla/5.0 (iPhone; U; ru; CPU iPhone OS 4_2_1 like Mac OS X; ru) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148a Safari/6533.18.5",\
        "Mozilla/5.0 (iPhone; U; fr; CPU iPhone OS 4_2_1 like Mac OS X; fr) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148a Safari/6533.18.5",\
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; pl-pl) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5",\
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; en-gb) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5",\
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; nb-no) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148a Safari/6533.18.5",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; th-th) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-ca) AppleWebKit/531.2+ (KHTML, like Gecko) Version/5.0 Safari/531.2+",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; es-ES) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0 Safari/533.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; ja-JP) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; fr) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; ru-ru) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; it-it) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-us) AppleWebKit/534.1+ (KHTML, like Gecko) Version/5.0 Safari/533.16",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; el-gr) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; zh-tw) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; it-it) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; nl-nl) AppleWebKit/533.16 (KHTML, like Gecko) Version/4.1 Safari/533.16",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; de-de) AppleWebKit/533.16 (KHTML, like Gecko) Version/4.1 Safari/533.16",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; nb-no) AppleWebKit/533.16 (KHTML, like Gecko) Version/4.1 Safari/533.16",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; tr) AppleWebKit/528.4+ (KHTML, like Gecko) Version/4.0dp1 Safari/526.11.2",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; de) AppleWebKit/528.4+ (KHTML, like Gecko) Version/4.0dp1 Safari/526.11.2",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-gb) AppleWebKit/528.10+ (KHTML, like Gecko) Version/4.0dp1 Safari/526.11.2",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-gb) AppleWebKit/528.4+ (KHTML, like Gecko) Version/4.0dp1 Safari/526.11.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/4.0.5 Safari/531.22.7",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-gb) AppleWebKit/531.22.7 (KHTML, like Gecko) Version/4.0.5 Safari/531.22.7",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; en-us) AppleWebKit/531.22.7 (KHTML, like Gecko) Version/4.0.5 Safari/531.22.7",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; ja-jp) AppleWebKit/531.22.7 (KHTML, like Gecko) Version/4.0.5 Safari/531.22.7",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-us) AppleWebKit/531.22.7 (KHTML, like Gecko) Version/4.0.5 Safari/531.22.7",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; ja-jp) AppleWebKit/531.22.7 (KHTML, like Gecko) Version/4.0.5 Safari/531.22.7",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/4.0.5 Safari/531.22.7",\
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_1 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 Safari/6531.22.7",\
        "Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-TW) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE) AppleWebKit/532+ (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; hu-hu) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; ru-ru) AppleWebKit/533.2+ (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; de-at) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",\
        "Mozilla/5.0 (iPhone Simulator; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7D11 Safari/531.21.10",\
        "Mozilla/5.0 (iPad; U; CPU OS 3_2_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B500 Safari/53",\
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; es-es) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B360 Safari/531.21.10",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-us) AppleWebKit/531.9 (KHTML, like Gecko) Version/4.0.3 Safari/531.9",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; en-us) AppleWebKit/532.0+ (KHTML, like Gecko) Version/4.0.3 Safari/531.9",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; fi-fi) AppleWebKit/531.9 (KHTML, like Gecko) Version/4.0.3 Safari/531.9",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6) AppleWebKit/531.4 (KHTML, like Gecko) Version/4.0.3 Safari/531.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/4.0.2 Safari/530.19.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; pl-PL) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/4.0.2 Safari/530.19.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; fr-FR) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/4.0.2 Safari/530.19.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-DE) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/4.0.2 Safari/530.19.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/4.0.2 Safari/530.19.1",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-us) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/4.0.2 Safari/530.19",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-us) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/4.0.1 Safari/530.18",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; ja-JP) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; fr-FR) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; de-DE) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; hu-HU) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fi-FI) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; ja-jp) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/3.2.3 Safari/525.28.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/525.28 (KHTML, like Gecko) Version/3.2.2 Safari/525.28.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-DE) AppleWebKit/528+ (KHTML, like Gecko) Version/3.2.2 Safari/525.28.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; nb-NO) AppleWebKit/525.28 (KHTML, like Gecko) Version/3.2.2 Safari/525.28.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr-FR) AppleWebKit/525.28 (KHTML, like Gecko) Version/3.2.2 Safari/525.28.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.28 (KHTML, like Gecko) Version/3.2.2 Safari/525.28.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-DE) AppleWebKit/528+ (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; ja-jp) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_6; fr-fr) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; sv-se) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; it-it) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; es-es) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; ru-ru) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; ko-kr) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; it-it) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; fr-fr) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/525.26.2 (KHTML, like Gecko) Version/3.2 Safari/525.26.13",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_5; en-us) AppleWebKit/525.26.2 (KHTML, like Gecko) Version/3.2 Safari/525.26.12",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_5; ja-jp) AppleWebKit/525.26.2 (KHTML, like Gecko) Version/3.2 Safari/525.26.12",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; pl-PL) AppleWebKit/525.19 (KHTML, like Gecko) Version/3.1.2 Safari/525.21",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Version/3.1.2 Safari/525.21",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; pl-PL) AppleWebKit/525.19 (KHTML, like Gecko) Version/3.1.2 Safari/525.21",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; it-IT) AppleWebKit/525+ (KHTML, like Gecko) Version/3.1.2 Safari/525.21",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB) AppleWebKit/525.19 (KHTML, like Gecko) Version/3.1.2 Safari/525.21",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_6; en-us) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_4; fr-fr) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; fr) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.22",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit/528.7+ (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.1 Safari/525.17",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.1 Safari/525.17",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ca-es) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.1 Safari/525.20",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_3; sv-se) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.1 Safari/525.20",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_3; en) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.1 Safari/525.20",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; ja-jp) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.1 Safari/525.18",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; de-de) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.1 Safari/525.20",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_3; nl-nl) AppleWebKit/527+ (KHTML, like Gecko) Version/3.1.1 Safari/525.20",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_3; hu-hu) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.1 Safari/525.20",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_3; en-ca) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.1 Safari/525.20",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; ru-RU) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; es-ES) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_4; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1 Safari/525.13",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_2; en-gb) AppleWebKit/526+ (KHTML, like Gecko) Version/3.1 iPhone",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; zh-tw) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13.3",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_2; it-it) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_2; es-es) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_2; en-us) AppleWebKit/525.9 (KHTML, like Gecko) Version/3.1 Safari/525.9",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_2; en-gb) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en) AppleWebKit/525+ (KHTML, like Gecko) Version/3.0.4 Safari/523.11",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; sv-se) AppleWebKit/523.12.2 (KHTML, like Gecko) Version/3.0.4 Safari/523.12.2",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/523.10.3 (KHTML, like Gecko) Version/3.0.4 Safari/523.10",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; en) AppleWebKit/525.3+ (KHTML, like Gecko) Version/3.0.4 Safari/523.12.2",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; sv-se) AppleWebKit/523.10.6 (KHTML, like Gecko) Version/3.0.4 Safari/523.10.6",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; ko-kr) AppleWebKit/523.15.1 (KHTML, like Gecko) Version/3.0.4 Safari/523.15",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; ja-jp) AppleWebKit/523.10.3 (KHTML, like Gecko) Version/3.0.4 Safari/523.10",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; it-it) AppleWebKit/523.10.6 (KHTML, like Gecko) Version/3.0.4 Safari/523.10.6",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; fr-fr) AppleWebKit/523.10.3 (KHTML, like Gecko) Version/3.0.4 Safari/523.10",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; es-es) AppleWebKit/523.15.1 (KHTML, like Gecko) Version/3.0.4 Safari/523.15",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en) AppleWebKit/522.15.5 (KHTML, like Gecko) Version/3.0.3 Safari/522.15.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; sv) AppleWebKit/522.15.5 (KHTML, like Gecko) Version/3.0.3 Safari/522.15.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en) AppleWebKit/522.15.5 (KHTML, like Gecko) Version/3.0.3 Safari/522.15.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; da-DK) AppleWebKit/523.11.1+ (KHTML, like Gecko) Version/3.0.3 Safari/522.15.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; cs) AppleWebKit/522.15.5 (KHTML, like Gecko) Version/3.0.3 Safari/522.15.5",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/523.3+ (KHTML, like Gecko) Version/3.0.3 Safari/522.12.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ca-es) AppleWebKit/522.11.1 (KHTML, like Gecko) Version/3.0.3 Safari/522.12.1",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-us) AppleWebKit/522.11.1 (KHTML, like Gecko) Version/3.0.3 Safari/522.12.1",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit/523.5+ (KHTML, like Gecko) Version/3.0.3 Safari/522.12.1",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit/522.11.1 (KHTML, like Gecko) Version/3.0.3 Safari/522.12.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; nl) AppleWebKit/522.13.1 (KHTML, like Gecko) Version/3.0.2 Safari/522.13.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en) AppleWebKit/522.13.1 (KHTML, like Gecko) Version/3.0.2 Safari/522.13.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; it) AppleWebKit/522.13.1 (KHTML, like Gecko) Version/3.0.2 Safari/522.13.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; el) AppleWebKit/522.13.1 (KHTML, like Gecko) Version/3.0.2 Safari/522.13.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/522.11 (KHTML, like Gecko) Version/3.0.2 Safari/522.12",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/522.11 (KHTML, like Gecko) Version/3.0.2 Safari/522.12",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit/522.11 (KHTML, like Gecko) Version/3.0.2 Safari/522.12",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; fi) AppleWebKit/522.12.1 (KHTML, like Gecko) Version/3.0.1 Safari/522.12.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; th) AppleWebKit/522.12.1 (KHTML, like Gecko) Version/3.0.1 Safari/522.12.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; nl) AppleWebKit/522.12.1 (KHTML, like Gecko) Version/3.0.1 Safari/522.12.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en) AppleWebKit/522.12.1 (KHTML, like Gecko) Version/3.0.1 Safari/522.12.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; sv-SE) AppleWebKit/523.13 (KHTML, like Gecko) Version/3.0 Safari/523.13",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/523.15 (KHTML, like Gecko) Version/3.0 Safari/523.15",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; pt) AppleWebKit/522.11.3 (KHTML, like Gecko) Version/3.0 Safari/522.11.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-TW) AppleWebKit/523.15 (KHTML, like Gecko) Version/3.0 Safari/523.15",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr-TR) AppleWebKit/523.15 (KHTML, like Gecko) Version/3.0 Safari/523.15",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru) AppleWebKit/522.11.3 (KHTML, like Gecko) Version/3.0 Safari/522.11.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR) AppleWebKit/523.15 (KHTML, like Gecko) Version/3.0 Safari/523.15",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; pl-PL) AppleWebKit/523.12.9 (KHTML, like Gecko) Version/3.0 Safari/523.12.9",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; nb) AppleWebKit/522.11.3 (KHTML, like Gecko) Version/3.0 Safari/522.11.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; hr) AppleWebKit/522.11.3 (KHTML, like Gecko) Version/3.0 Safari/522.11.3",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; sv-se) AppleWebKit/419 (KHTML, like Gecko) Safari/419.3",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; sv-se) AppleWebKit/418.9 (KHTML, like Gecko) Safari/",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; nl-nl) AppleWebKit/418.8 (KHTML, like Gecko) Safari/419.3",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/418.9 (KHTML, like Gecko) Safari/419.3",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; it-it) AppleWebKit/418.9 (KHTML, like Gecko) Safari/419.3",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fi-fi) AppleWebKit/418.8 (KHTML, like Gecko) Safari/419.3",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; es) AppleWebKit/419 (KHTML, like Gecko) Safari/419.3",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/419 (KHTML, like Gecko) Safari/419.3",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/418.8 (KHTML, like Gecko) Safari/419.3",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/418.9.1 (KHTML, like Gecko) Safari/419.3",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; tr-tr) AppleWebKit/418 (KHTML, like Gecko) Safari/417.9.3",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; sv-se) AppleWebKit/417.9 (KHTML, like Gecko) Safari/417.8_Adobe",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; nl-nl) AppleWebKit/417.9 (KHTML, like Gecko) Safari/417.9.2",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; nb-no) AppleWebKit/418 (KHTML, like Gecko) Safari/417.9.3",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; it-it) AppleWebKit/417.9 (KHTML, like Gecko) Safari/417.9.2",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-fr) AppleWebKit/417.9 (KHTML, like Gecko) Safari/417.8",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr) AppleWebKit/417.9 (KHTML, like Gecko)",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; es) AppleWebKit/417.9 (KHTML, like Gecko) Safari/417.8",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/417.9 (KHTML, like Gecko) Safari/417.9.2",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/418 (KHTML, like Gecko) Safari/417.9.3",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; nl-nl) AppleWebKit/416.12 (KHTML, like Gecko) Safari/416.13",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; nl-nl) AppleWebKit/416.11 (KHTML, like Gecko) Safari/312",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/416.12 (KHTML, like Gecko) Safari/416.13",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-fr) AppleWebKit/416.12 (KHTML, like Gecko) Safari/416.13",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr) AppleWebKit/416.12 (KHTML, like Gecko) Safari/416.13_Adobe",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr) AppleWebKit/416.12 (KHTML, like Gecko) Safari/412.5",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/416.12 (KHTML, like Gecko) Safari/416.13",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-ca) AppleWebKit/416.11 (KHTML, like Gecko) Safari/416.12",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/416.11 (KHTML, like Gecko) Safari/416.12",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/416.12 (KHTML, like Gecko) Safari/416.13_Adobe",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/412.7 (KHTML, like Gecko) Safari/412.5",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-fr) AppleWebKit/412.7 (KHTML, like Gecko) Safari/412.5",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/412.7 (KHTML, like Gecko) Safari/412.5",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/412.7 (KHTML, like Gecko) Safari/412.5",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/412.7 (KHTML, like Gecko) Safari/412.5",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS; en-en) AppleWebKit/412 (KHTML, like Gecko) Safari/412",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-fr) AppleWebKit/412 (KHTML, like Gecko) Safari/412",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr) AppleWebKit/412 (KHTML, like Gecko) Safari/412",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en_US) AppleWebKit/412 (KHTML, like Gecko) Safari/412",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/412 (KHTML, like Gecko) Safari/412 Privoxy/3.0",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/412.6.2 (KHTML, like Gecko) Safari/412.2.2",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/412.6 (KHTML, like Gecko) Safari/412.2",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/412.6.2 (KHTML, like Gecko) Safari/412.2.2",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/412.6 (KHTML, like Gecko) Safari/412.2",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/412 (KHTML, like Gecko) Safari/412",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; it-it) AppleWebKit/312.8 (KHTML, like Gecko) Safari/312.6",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-fr) AppleWebKit/312.8 (KHTML, like Gecko) Safari/312.5",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/312.8.1 (KHTML, like Gecko) Safari/312.6",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/312.8 (KHTML, like Gecko) Safari/312.5",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/312.8 (KHTML, like Gecko) Safari/312.5",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/312.8.1 (KHTML, like Gecko) Safari/312.6",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/312.8 (KHTML, like Gecko) Safari/312.5",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; sv-se) AppleWebKit/312.5.1 (KHTML, like Gecko) Safari/312.3.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; it-it) AppleWebKit/312.5.1 (KHTML, like Gecko) Safari/312.3.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-fr) AppleWebKit/312.5.1 (KHTML, like Gecko) Safari/312.3.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr) AppleWebKit/312.5.2 (KHTML, like Gecko) Safari/312.3.3",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr) AppleWebKit/312.5 (KHTML, like Gecko) Safari/312.3",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; es) AppleWebKit/312.5.1 (KHTML, like Gecko) Safari/312.3.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/312.5 (KHTML, like Gecko) Safari/312.3",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/312.5.2 (KHTML, like Gecko) Safari/125",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/312.5.1 (KHTML, like Gecko) Safari/125.9",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/312.5.2 (KHTML, like Gecko) Safari/312.3.3",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-fr) AppleWebKit/312.1.1 (KHTML, like Gecko) Safari/312",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-fr) AppleWebKit/312.1 (KHTML, like Gecko) Safari/125",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-ca) AppleWebKit/312.1 (KHTML, like Gecko) Safari/312",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/312.1 (KHTML, like Gecko)",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/312.1 (KHTML, like Gecko) Safari/312",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/312.1 (KHTML, like Gecko) Safari/312.3.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-ch) AppleWebKit/312.1 (KHTML, like Gecko) Safari/312",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-fr) AppleWebKit/125.5.5 (KHTML, like Gecko) Safari/125.12",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-ch) AppleWebKit/125.5.5 (KHTML, like Gecko) Safari/125.12",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/125.5.7 (KHTML, like Gecko) Safari/125.12",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/125.5.5 (KHTML, like Gecko) Safari/125.12",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.5.7 (KHTML, like Gecko) Safari/125.12",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.5.5 (KHTML, like Gecko) Safari/125.5.5",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.5.5 (KHTML, like Gecko) Safari/125.11",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/125.5.7 (KHTML, like Gecko) Safari/125.12",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/125.5.6 (KHTML, like Gecko) Safari/125.12",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/125.5.5 (KHTML, like Gecko) Safari/125.12",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-fr) AppleWebKit/125.5 (KHTML, like Gecko) Safari/125.9",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en_CA) AppleWebKit/125.4 (KHTML, like Gecko) Safari/125.9",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-au) AppleWebKit/125.4 (KHTML, like Gecko) Safari/125.9",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.4 (KHTML, like Gecko) Safari/125.9",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/125.4 (KHTML, like Gecko) Safari/125.9",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/125.2 (KHTML, like Gecko) Safari/125.7",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.2 (KHTML, like Gecko) Safari/85.8",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.2 (KHTML, like Gecko) Safari/125.7",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/125.2 (KHTML, like Gecko) Safari/125.8",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; it-it) AppleWebKit/124 (KHTML, like Gecko) Safari/125.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/124 (KHTML, like Gecko) Safari/125",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/124 (KHTML, like Gecko) Safari/125.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-fr) AppleWebKit/85.8.5 (KHTML, like Gecko) Safari/85.8.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/85.8.5 (KHTML, like Gecko) Safari/85.8.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-gb) AppleWebKit/85.8.5 (KHTML, like Gecko) Safari/85.8.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/85.8.2 (KHTML, like Gecko) Safari/85.8.1",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/85.8.5 (KHTML, like Gecko) Safari/85",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; sv-se) AppleWebKit/85.7 (KHTML, like Gecko) Safari/85.5",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-fr) AppleWebKit/85.7 (KHTML, like Gecko) Safari/85.5",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/85.7 (KHTML, like Gecko) Safari/85.6",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/85.7 (KHTML, like Gecko) Safari/85.7",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008092816 Mobile Safari 1.1.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.8 (KHTML, like Gecko)",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fi-fi) AppleWebKit/420+ (KHTML, like Gecko) Safari/419.3",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/419.2 (KHTML, like Gecko) Safari/419.3",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-ch) AppleWebKit/85 (KHTML, like Gecko) Safari/85",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; da-dk) AppleWebKit/522+ (KHTML, like Gecko) Safari/419.3",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; it-IT) AppleWebKit/521.25 (KHTML, like Gecko) Safari/521.24",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit/522.11.1 (KHTML, like Gecko) Safari/419.3",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit (KHTML, like Gecko)",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit/528.16 (KHTML, like Gecko)",\
        "Mozilla/5.0 (Windows NT 5.2; RW; rv:7.0a1) Gecko/20091211 SeaMonkey/9.23a1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.2; WOW64; rv:1.8.0.7) Gecko/20110321 MultiZilla/4.33.2.6a SeaMonkey/8.6.55",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; RW; rv:1.8.0.7) Gecko/20110321 MultiZilla/4.33.2.6a SeaMonkey/8.6.55",\
        "Mozilla/5.0 (X11; U; Linux i686; ru; rv:33.2.3.12) Gecko/20120201 SeaMonkey/8.2.8",\
        "Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20120502 SeaMonkey/2.9.1",\
        "Mozilla/5.0 (Windows NT 5.0; rv:1.9.2.8) Gecko/20120427 Firefox/12.0 SeaMonkey/2.9",\
        "Mozilla/5.0 (X11; Linux x86_64; rv:10.0.2) Gecko/20120216 Firefox/10.0.2 SeaMonkey/2.7.2",\
        "Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",\
        "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",\
        "Mozilla/5.0 (Windows NT 5.2; rv:7.0a1) Gecko/20110622 SeaMonkey/2.4a1",\
        "Mozilla/5.0 (Windows NT 5.2; rv:7.0a1) Gecko/20110619 SeaMonkey/2.4a1",\
        "Mozilla/5.0 (Windows NT 5.2; rv:7.0a1) Gecko/20110616 SeaMonkey/2.4a1",\
        "Mozilla/5.0 (Windows NT 5.2; rv:7.0a1) Gecko/20110613 SeaMonkey/2.4a1",\
        "Mozilla/5.0 (Windows NT 5.2; rv:7.0a1) Gecko/20110607 SeaMonkey/2.4a1",\
        "Mozilla/5.0 (Windows NT 5.1; rv:7.0a1) Gecko/20110612 Firefox/7.0a1 SeaMonkey/2.4a1",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:33.0) Gecko/20100101 Firefox/33.0 SeaMonkey/2.30",\
        "Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0 SeaMonkey/2.3",\
        "Mozilla/5.0 (X11; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0 SeaMonkey/2.25",\
        "Mozilla/5.0 (Windows NT 5.1; rv:28.0) Gecko/20100101 Firefox/28.0 SeaMonkey/2.25 Lightning/3.0b1",\
        "Mozilla/5.0 (Windows NT 5.1; rv:26.0) Gecko/20100101 Firefox/26.0 SeaMonkey/2.23a1",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:24.0) Gecko/20100101 Firefox/24.0 SeaMonkey/2.21 Lightning/2.6b3",\
        "Mozilla/5.0 (X11; Linux i686; rv:7.0a1) Gecko/20110604 SeaMonkey/2.2a1pre",\
        "Mozilla/5.0 (X11; Linux i686; rv:7.0a1) Gecko/20110530 SeaMonkey/2.2a1pre",\
        "Mozilla/5.0 (X11; Linux i686; rv:2.2a1pre) Gecko/20110407 SeaMonkey/2.2a1pre",\
        "Mozilla/5.0 (Windows NT 5.2; rv:7.0a1) Gecko/20110605 SeaMonkey/2.2a1pre",\
        "Mozilla/5.0 (Windows NT 5.2; rv:7.0a1) Gecko/20110602 SeaMonkey/2.2a1pre",\
        "Mozilla/5.0 (Windows NT 5.2; rv:7.0a1) Gecko/20110530 SeaMonkey/2.2a1pre",\
        "Mozilla/5.0 (Windows NT 5.2; rv:7.0a1) Gecko/20110527 SeaMonkey/2.2a1pre",\
        "Mozilla/5.0 (Windows NT 5.2; rv:7.0a1) Gecko/20110525 SeaMonkey/2.2a1pre",\
        "Mozilla/5.0 (Windows NT 5.2; rv:6.0a1) Gecko/20110512 SeaMonkey/2.2a1pre",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0 SeaMonkey/2.20",\
        "Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20100101 Firefox/21.0 SeaMonkey/2.18a1",\
        "Mozilla/5.0 (Windows NT 5.2; rv:20.0) Gecko/20100101 Firefox/20.0 SeaMonkey/2.17",\
        "Mozilla/5.0 (Windows NT 6.0; rv:19.0) Gecko/20100101 Firefox/19.0 SeaMonkey/2.16.1",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:16.0) Gecko/20121011 Firefox/16.0 SeaMonkey/2.13.1 Lightning/1.8",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:16.0) Gecko/20121011 Firefox/16.0 SeaMonkey/2.13.1",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:16.0) Gecko/20120830 Firefox/16.0 SeaMonkey/2.13 Lightning/1.8b1",\
        "Mozilla/5.0 (Windows NT 5.1; rv:16.0) Gecko/20121007 Firefox/16.0 SeaMonkey/2.13",\
        "Mozilla/5.0 (X11; Linux x86_64; rv:15.0) Gecko/20120909 SeaMonkey/2.12.1",\
        "Mozilla/5.0 (X11; Linux i686; rv:15.0) Gecko/20120910 Firefox/15.0.1 SeaMonkey/2.12.1",\
        "Mozilla/5.0 (X11; Linux i686; rv:15.0) Gecko/20120909 Firefox/15.0.1 SeaMonkey/2.12.1",\
        "Mozilla/5.0 (Windows NT 6.1; rv:15.0) Gecko/20120909 Firefox/15.0.1 SeaMonkey/2.12.1",\
        "Mozilla/5.0 (Windows NT 5.2; rv:15.0) Gecko/20120909 Firefox/15.0.1 SeaMonkey/2.12.1",\
        "Mozilla/5.0 (Windows NT 5.1; rv:15.0) Gecko/20120909 Firefox/15.0.1 SeaMonkey/2.12.1",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:15.0) Gecko/20120909 SeaMonkey/2.12.1",\
        "Mozilla/5.0 (X11; Linux x86_64; rv:15.0) Gecko/20120826 Firefox/15.0 SeaMonkey/2.12 Lightning/1.7",\
        "Mozilla/5.0 (X11; Linux x86_64; rv:14.0) Gecko/20120817 SeaMonkey/2.11",\
        "Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20120715 Firefox/14.0.1 SeaMonkey/2.11 Lightning/1.6",\
        "Mozilla/5.0 (X11; Linux i686; rv:2.0b13pre) Gecko/20110321 SeaMonkey/2.1b3pre",\
        "Mozilla/5.0 (X11; Linux i686; rv:2.0b12pre) Gecko/20110204 SeaMonkey/2.1b3pre",\
        "Mozilla/5.0 (X11; Linux i686; rv:2.0b9pre) Gecko/20110101 SeaMonkey/2.1b2pre",\
        "Mozilla/5.0 (X11; Linux i686; rv:2.0b9pre) Gecko/20101230 SeaMonkey/2.1b2pre",\
        "Mozilla/5.0 (Windows NT 5.2; rv:2.0b9pre) Gecko/20101231 SeaMonkey/2.1b2pre",\
        "Mozilla/5.0 (Windows NT 5.2; rv:2.0b8pre) Gecko/20101014 SeaMonkey/2.1b2pre",\
        "Mozilla/5.0 (Windows NT 5.2; rv:2.0b7pre) Gecko/20100915 Firefox/4.0b7pre SeaMonkey/2.1b1pre",\
        "Mozilla/5.0 (X11; Linux i686; rv:2.0b7pre) Gecko/20101008 Firefox/4.0b7pre SeaMonkey/2.1b1",\
        "Mozilla/5.0 (Windows; Windows NT 5.2; rv:2.0b3pre) Gecko/20100803 SeaMonkey/2.1a3pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-CA; rv:1.9.3a3pre) Gecko/20100312 SeaMonkey/2.1a1pre",\
        "Mozilla/5.0 (Windows NT 5.1; rv:13.0) Gecko/20120615 Firefox/13.0.1 SeaMonkey/2.10.1",\
        "Mozilla/5.0 (X11; Linux i686; rv:13.0) Gecko/20120604 Firefox/13.0 SeaMonkey/2.10 Lightning/1.5.1",\
        "Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20110608 Firefox/4.0.1 SeaMonkey/2.1 Lightning/1.0b4pre",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0.1) Gecko/20110608 SeaMonkey/2.1",\
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20110608 Firefox/4.0.1 SeaMonkey/2.1 Lightning/1.0b4pre",\
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20110511 Firefox/4.0.1 SeaMonkey/2.1",\
        "Mozilla/5.0 (Windows NT 5.0; rv:2.0.1) Gecko/20110608 Firefox/4.0.1 SeaMonkey/2.1",\
        "Mozilla/5.0 (Windows NT 6.1; rv:1.9.1.x) Gecko/20110606 SeaMonkey/2.x Firefox/5.0",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1b3pre) Gecko/20090302 SeaMonkey/2.0b1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; rv:1.9.1b4pre) Gecko/20090419 SeaMonkey/2.0b1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1b4pre) Gecko/20090419 SeaMonkey/2.0b1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.9.1b4pre) Gecko/20090419 SeaMonkey/2.0b1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1b3pre) Gecko/20081208 SeaMonkey/2.0a3pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.9.2a1pre) Gecko/20081228 SeaMonkey/2.0a3pre",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.1b3pre) Gecko/20090223 SeaMonkey/2.0a3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; rv:1.9.1b3pre) Gecko/20081202 SeaMonkey/2.0a2",\
        "Mozilla/5.0 (X11; U; Linux i686; rv:1.9.1a2pre) Gecko/20080824052448 SeaMonkey/2.0a1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; rv:1.9b3pre) Gecko/2008010602 SeaMonkey/2.0a1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a5pre) Gecko/20070529 SeaMonkey/2.0a1pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1b1pre) Gecko/20080925121544 SeaMonkey/2.0a1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.9.1.14) Gecko/20100930 SeaMonkey/2.0.9",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; nl; rv:1.9.1.13) Gecko/20100914 Lightning/1.0b1 SeaMonkey/2.0.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.9.1.12) Gecko/20100825 SeaMonkey/2.0.7",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-CA; rv:1.9.1.11pre) Gecko/20100629 SeaMonkey/2.0.6pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-CA; rv:1.9.1.11pre) Gecko/20100625 SeaMonkey/2.0.6pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-CA; rv:1.9.1.11pre) Gecko/20100622 SeaMonkey/2.0.6pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-CA; rv:1.9.1.11pre) Gecko/20100605 SeaMonkey/2.0.6pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.11pre) Gecko/20100508 SeaMonkey/2.0.6pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.11) Gecko/20100720 Fedora/2.0.6-1.fc12 SeaMonkey/2.0.6",\
        "Mozilla/5.0 (X11; U; Linux ia64; de; rv:1.9.1.11) Gecko/20100820 Lightning/1.0b2pre SeaMonkey/2.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.11) Gecko/20100701 SeaMonkey/2.0.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.11) Gecko/20100701 SeaMonkey/2.0.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.11) Gecko/20100701 SeaMonkey/2.0.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.9.1.11) Gecko/20100701 SeaMonkey/2.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.1.10) Gecko/20100504 Lightning/1.0b1 Mnenhy/0.8.2 SeaMonkey/2.0.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.10) Gecko/20100504 Lightning/1.0b1 SeaMonkey/2.0.5",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.9pre) Gecko/20100212 SeaMonkey/2.0.4pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.1.9) Gecko/20100428 Lightning/1.0b1 SeaMonkey/2.0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.9) Gecko/20100317 Lightning/1.0b1 SeaMonkey/2.0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; nb-NO; rv:1.9.1.10) Gecko/20100623 Fedora/2.0.5-1.fc12 Fedora SeaMonkey/2.0.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; de; rv:1.9.1.8) Gecko/20100205 SeaMonkey/2.0.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.7) Gecko/20100104 SeaMonkey/2.0.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.7) Gecko/20100104 Firefox/3.5.8 (SeaMonkey/2.0.2)",\
        "Mozilla/5.0 (X11; U; Linux i686; nb-NO; rv:1.9.1.16) Gecko/20110420 SeaMonkey/2.0.14",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.19) Gecko/20110429 Gentoo/2.0.14 SeaMonkey/2.0.14",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.9.1.19) Gecko/20110420 SeaMonkey/2.0.14",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.1.19) Gecko/20110420 SeaMonkey/2.0.14",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.9.1.19) Gecko/20110420 SeaMonkey/2.0.14",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.19) Gecko/20110420 Firefox/3.5.19 SeaMonkey/2.0.14",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.9.1.19) Gecko/20110420 SeaMonkey/2.0.14",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.1.18) Gecko/20110412 Lightning/1.0b1 SeaMonkey/2.0.13",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.18) Gecko/20110320 SeaMonkey/2.0.13",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; nl; rv:1.9.1.18) Gecko/20110320 SeaMonkey/2.0.13",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.18) Gecko/20110320 SeaMonkey/2.0.13",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.18) Gecko/20110320 SeaMonkey/2.0.13",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.18) Gecko/20110320 SeaMonkey/2.0.13",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.1.18) Gecko/20110320 SeaMonkey/2.0.13",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.1.18) Gecko/20110320 SeaMonkey/2.0.13",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110303 SeaMonkey/2.0.12",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.17) Gecko/20110309 Lightning/1.0b2pre SeaMonkey/2.0.12",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20101123 SeaMonkey/2.0.11",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.9.1.16) Gecko/20101123 SeaMonkey/2.0.11",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.16) Gecko/20101123 SeaMonkey/2.0.11",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de; rv:1.9.1.16) Gecko/20101123 SeaMonkey/2.0.11",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.9.1.15) Gecko/20101027 SeaMonkey/2.0.10",\
        "Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.1.6) Gecko/20091210 SUSE/2.0.1-1.1.1 SeaMonkey/2.0.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1b3pre) Gecko/20081208 SeaMonkey/2.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a5pre) Gecko/20070527 SeaMonkey/1.5a",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a3pre) Gecko/20070317 SeaMonkey/1.5a",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a2pre) Gecko/20070109 SeaMonkey/1.5a",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a1) Gecko/20060520 SeaMonkey/1.5a",\
        "Mozilla/5.0 (OS/2; U; Warp 4.5; en-US; rv:1.9a1) Gecko/20051119 MultiZilla/1.8.1.0s SeaMonkey/1.5a",\
        "Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.9a1) Gecko/20060702 SeaMonkey/1.5a",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8) Gecko/20060301 SeaMonkey/1.1a Mnenhy/0.7.3.0",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fr-FR; rv:1.8.1.13) Gecko/20080313 SeaMonkey/1.1.9 (Ubuntu-1.1.9+nobinonly-0ubuntu1)",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.13) Gecko/20080313 SeaMonkey/1.1.9",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; pl-PL; rv:1.8.1.13) Gecko/20080313 SeaMonkey/1.1.9",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1.13) Gecko/20080313 SeaMonkey/1.1.9",\
        "Mozilla/5.0 (X11; U; Linux x86_64; fr-FR; rv:1.8.1.12) Gecko/20080209 SeaMonkey/1.1.8",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.12) Gecko/20080208 SeaMonkey/1.1.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070802 Firefox/2.0.0.11 SeaMonkey/1.1.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080201 SeaMonkey/1.1.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; fr-FR; rv:1.8.1.12) Gecko/20080201 SeaMonkey/1.1.8",\
        "Mozilla/5.0 (BeOS; U; Haiku BePC; en-US; rv:1.8.1.10pre) Gecko/20080112 SeaMonkey/1.1.7pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080201 SeaMonkey/1.1.7",\
        "Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.8.1.9) Gecko/20071030 SeaMonkey/1.1.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.1.9) Gecko/20071030 SeaMonkey/1.1.6",\
        "Mozilla/5.0 (Windows; U; WinNT3.51; en-US; rv:1.8.1.8) Gecko/20071009 SeaMonkey/1.1.5",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.6) Gecko/20070802 SeaMonkey/1.1.4 Mnenhy/0.7.5.666",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.8.1.6) Gecko/20070802 SeaMonkey/1.1.4",\
        "Mozilla/5.0 (Windows; U; Win 9x 4.90; en-GB; rv:1.8.1.6) Gecko/20070802 SeaMonkey/1.1.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; es-ES; rv:1.8.1.5) Gecko/20070716 SeaMonkey/1.1.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.8.1.5) Gecko/20070716 SeaMonkey/1.1.3",\
        "Mozilla/5.0 (X11; U; Linux i686; pt-BR; rv:1.8.1.4) Gecko/20070509 SeaMonkey/1.1.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.8.1.4) Gecko/20070509 SeaMonkey/1.1.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.8.1.4) Gecko/20070509 SeaMonkey/1.1.2",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1.24) Gecko/20100228 SeaMonkey/1.1.19",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.23) Gecko/20090908 Fedora/1.1.18-1.fc10 SeaMonkey/1.1.18",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18",\
        "Mozilla/5.0 (Windows; U; Win 9x 4.90; de-AT; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.22) Gecko/20090708 SeaMonkey/1.1.17",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.22) Gecko/20090605 SeaMonkey/1.1.17 (Ubuntu-1.1.17+nobinonly-0ubuntu1)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.22) Gecko/20090605 SeaMonkey/1.1.17 Mnenhy/0.7.6.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.8.1.22) Gecko/20090605 SeaMonkey/1.1.17",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1.22) Gecko/20090605 SeaMonkey/1.1.17",\
        "Mozilla/5.0 (X11; U; FreeBSD amd64; en-US; rv:1.8.1.21) Gecko/20090424 SeaMonkey/1.1.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-AT; rv:1.8.1.21) Gecko/20090403 SeaMonkey/1.1.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.21) Gecko/20090403 SeaMonkey/1.1.16 Mnenhy/0.7.5.666",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.21) Gecko/20090403 SeaMonkey/1.1.16",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.1.21) Gecko/20090403 SeaMonkey/1.1.16",\
        "Mozilla/5.0 (X11; U; Linux i686; ja-JP; rv:1.8.1.21) Gecko/20090322 SeaMonkey/1.1.15",\
        "Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:1.8.1.21) Gecko/20090322 SeaMonkey/1.1.15",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.21) Gecko/20090303 SeaMonkey/1.1.15 Mnenhy/0.7.6.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.1.21) Gecko/20090303 SeaMonkey/1.1.15",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.8.1.21) Gecko/20090303 SeaMonkey/1.1.15",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.19) Gecko/20081221 SeaMonkey/1.1.14",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.19) Gecko/20081216 SeaMonkey/1.1.14",\
        "Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.8.1.19) Gecko/20081204 SeaMonkey/1.1.14 Mnenhy/0.7.6.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.1.19) Gecko/20081204 SeaMonkey/1.1.14",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.21) Gecko/20090303 SeaMonkey/1.1.14",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.19) Gecko/20081204 SeaMonkey/1.1.14 Mnenhy/0.7.5.666",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.19) Gecko/20081204 MultiZilla/1.8.3.5c SeaMonkey/1.1.14",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1.19) Gecko/20081204 SeaMonkey/1.1.14",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1.19) Gecko/20081204 SeaMonkey/1.1.14",\
        "Mozilla/5.0 (Amiga; U; AmigaOS 1.3; en; rv:1.8.1.19) Gecko/20081204 SeaMonkey/1.1.14",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.18) Gecko/20081110 SUSE/1.1.13-1.10 SeaMonkey/1.1.13",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.18) Gecko/20081113 Fedora/1.1.13-1.fc8 SeaMonkey/1.1.13",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.8.1.18) Gecko/20081031 SeaMonkey/1.1.13",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; PL; rv:1.8.1.18) Gecko/20081031 SeaMonkey/1.1.13",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.18) Gecko/20081031 SeaMonkey/1.1.13",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; es-ES; rv:1.8.1.18) Gecko/20081031 SeaMonkey/1.1.13",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.17) Gecko/20080829 SeaMonkey/1.1.12 (Ubuntu-1.1.12+nobinonly-0ubuntu1)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.1.17) Gecko/20080925 Fedora/1.1.12-1.fc9 SeaMonkey/1.1.12",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.17) Gecko/20090224 SeaMonkey/1.1.12",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.8.1.17) Gecko/20080829 SeaMonkey/1.1.12",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1.17) Gecko/20080829 SeaMonkey/1.1.12",\
        "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.8.1.16) Gecko/20080716 SeaMonkey/1.1.11",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 Fedora/1.1.11-1.fc8 SeaMonkey/1.1.11",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-AT; rv:1.8.1.16) Gecko/20080702 SeaMonkey/1.1.11",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.16) Gecko/20080702 SeaMonkey/1.1.11",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.8.1.16) Gecko/20080702 SeaMonkey/1.1.11 Mnenhy/0.7.5.0",\
        "Mozilla/5.0 (Windows; U; Win 9x 4.90; en-US; rv:1.8.1.16) Gecko/20080702 SeaMonkey/1.1.11",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; PL; rv:1.8.1.15) Gecko/20080621 SeaMonkey/1.1.10",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.15) Gecko/20080621 SeaMonkey/1.1.10",\
        "Mozilla/5.0 (OS/2; U; Warp 4.5; en-US; rv:1.8.1.3pre) Gecko/20070307 SeaMonkey/1.1.1+",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.2) Gecko/20070309 SeaMonkey/1.1.1",\
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); fr; rv:1.8.1.2) Gecko/20070221 SeaMonkey/1.1.1",\
        "Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.8.1.2) Gecko/20070227 SeaMonkey/1.1.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; PL; rv:1.8.1.2) Gecko/20070222 SeaMonkey/1.1.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2) Gecko/20070222 SeaMonkey/1.1.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; fr-FR; rv:1.8.1.2) Gecko/20070222 SeaMonkey/1.1.1",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1.2) Gecko/20070222 SeaMonkey/1.1.1",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1.2) Gecko/20070221 SeaMonkey/1.1.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1.2pre) Gecko/20070111 SeaMonkey/1.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070111 SeaMonkey/1.1 Mnenhy/0.7.4.10005",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; fr-FR; rv:1.8.1.2pre) Gecko/20070111 SeaMonkey/1.1",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1.2pre) Gecko/20070111 SeaMonkey/1.1",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8) Gecko/20060102 SeaMonkey/1.0b",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.8) Gecko/20051219 SeaMonkey/1.0b",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8b4) Gecko/20050910 SeaMonkey/1.0a",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.0.14eol) Gecko/20120628 CentOS/1.0.9-40.el4.centos SeaMonkey/1.0.9",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.14eol) Gecko/20090422 CentOS/1.0.9-0.37.el3.centos3 SeaMonkey/1.0.9",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.10) Gecko/20070306 SeaMonkey/1.0.8",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.10) Gecko/20070223 Fedora/1.0.8-0.5.1.fc5 SeaMonkey/1.0.8",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.10) Gecko/20070306 SeaMonkey/1.0.8",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.9) Gecko/20061211 SeaMonkey/1.0.7",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.0.9) Gecko/20061211 SeaMonkey/1.0.7",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.0.8) Gecko/20061109 SeaMonkey/1.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.8) Gecko/20061105 Red Hat/1.0.6-0.1.el3 SeaMonkey/1.0.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.8) Gecko/20061030 MultiZilla/1.8.3.0a SeaMonkey/1.0.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.8.0.8) Gecko/20061030 SeaMonkey/1.0.6",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060914 SeaMonkey/1.0.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.8.0.7) Gecko/20060910 SeaMonkey/1.0.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.7) Gecko/20060910 SeaMonkey/1.0.5",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.0.7) Gecko/20060910 SeaMonkey/1.0.5",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.0.7) Gecko/20060910 SeaMonkey/1.0.5",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.6) Gecko/20060803 SeaMonkey/1.0.4",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.6) Gecko/20060729 SeaMonkey/1.0.4",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.0.6) Gecko/20060729 SeaMonkey/1.0.4",\
        "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.0.5) Gecko/20060805 CentOS/1.0.3-0.el4.1.centos4 SeaMonkey/1.0.3",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.4) Gecko/20060619 SeaMonkey/1.0.2",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.2) Gecko/20060630 Red Hat/1.0.1-0.1.9.EL3 SeaMonkey/1.0.1",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.0.2) Gecko/20060404 SeaMonkey/1.0.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060316 SUSE/1.0-27 SeaMonkey/1.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060130 SeaMonkey/1.0",\
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.0.1) Gecko/20060130 SeaMonkey/1.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.8.1.8) Gecko/20071008 SeaMonkey",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en_CA) AppleWebKit/522+ (KHTML, like Gecko) Shiira/1.2.3 Safari/125",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/522.10.1 (KHTML, like Gecko) Shiira/1.2.2 Safari/125",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/418.9 (KHTML, like Gecko) Shiira/1.2.2 Safari/125",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit/418.9.1 (KHTML, like Gecko) Shiira/1.2.2 Safari/125",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; pl-pl) AppleWebKit/312.8 (KHTML, like Gecko) Shiira/1.2.1 Safari/125",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/523.15.1 (KHTML, like Gecko) Shiira Safari/125",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/522.11.1 (KHTML, like Gecko) Shiira Safari/125",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419.3 (KHTML, like Gecko) Shiira Safari/125",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko) Shiira Safari/125",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-au) AppleWebKit/523.10.3 (KHTML, like Gecko) Shiira Safari/125",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-us) AppleWebKit/531.21.8 (KHTML, like Gecko) Shiira Safari/125",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_4_11; en) AppleWebKit/525.18 (KHTML, like Gecko) Shiira Safari/125",\
        "Shiretoko Alpha 1 is an early developer milestone for the next version of Firefox that is being built on top of Mozilla's Gecko 1.9.1 layout engine",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1b5pre) Gecko/20090519 Shiretoko/3.5b5pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1b4pre) Gecko/20090401 Ubuntu/9.04 (jaunty) Shiretoko/3.5b4pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1b4pre) Gecko/20090420 Shiretoko/3.5b4pre (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1b4pre) Gecko/20090411 Shiretoko/3.5b4pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.8pre) Gecko/20100112 Shiretoko/3.5.8pre",\
        "Mozilla/5.0 (X11; U; Linux i686; ja; rv:1.9.1.6) Gecko/20091216 Shiretoko/3.5.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.5pre) Gecko/20091016 Shiretoko/3.5.5pre GTB6",\
        "Mozilla/5.0 (X11; U; Darwin i386; en-US; rv:1.9.1.4) Gecko/20100311 Shiretoko/3.5.5",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.4pre) Gecko/20090921 Ubuntu/9.04 (jaunty) Shiretoko/3.5.4pre",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.3pre) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.3pre (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2 FirePHP/0.3",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090716 Ubuntu/9.04 (jaunty) Shiretoko/3.5.1",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1) Gecko/20090701 Ubuntu/9.10 (karmic) Shiretoko/3.5",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1) Gecko/20090630 Ubuntu/9.04 (jaunty) Shiretoko/3.5",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1b4pre) Gecko/20090311 Shiretoko/3.1b4pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-TW; rv:1.9.1b4pre) Gecko/20090308 Shiretoko/3.1b4pre (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1b3pre) Gecko/20090109 Shiretoko/3.1b3pre",\
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1b3pre) Gecko/20081222 Shiretoko/3.1b3pre",\
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1b3pre) Gecko/20090105 Shiretoko/3.1b3pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; pt-BR; rv:1.9.1b3pre) Gecko/20090103 Shiretoko/3.1b3pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1b3pre) Gecko/20081204 Shiretoko/3.1b3pre (.NET CLR 3.5.30729)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1b3pre) Gecko/20090104 Shiretoko/3.1b3pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1b3pre) Gecko/20090207 Shiretoko/3.1b3pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1b3pre) Gecko/20090113 Shiretoko/3.1b3pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1b3pre) Gecko/20081228 Shiretoko/3.1b3pre",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1b3pre) Gecko/20081218 Shiretoko/3.1b3pre",\
        "Japanese tabbed web browser, released by Fenrir Inc. The browser's layout engine can be changed to either Internet Explorer's Trident or Mozilla's Gecko. ",\
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; Sleipnir/2.9.7)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB0.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 1.1.4322; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; OfficeLiveConnector.1.3; OfficeLivePatch.0.0; Sleipnir/2.9.6)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; WOW64; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Sleipnir/2.9.4)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; InfoPath.2; Sleipnir/2.9.3)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; InfoPath.1; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322; Sleipnir/2.9.2)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727; Sleipnir/2.9.2)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; GTB6.3; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Sleipnir/2.9.2)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; InfoPath.2; .NET CLR 2.0.50727; Sleipnir/2.9.2)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; InfoPath.1; .NET CLR 2.0.50727; Sleipnir/2.9.2)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; Sleipnir/2.9.1)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Sleipnir/2.8.5)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; GTB6; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30618; Sleipnir/2.8.5)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30618; Sleipnir/2.8.5)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 4.0.20506; Sleipnir/2.8.5)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Sleipnir/2.8.5)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; InfoPath.1; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; msn OptimizedIE8;JAJP; Sleipnir/2.8.5)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; GTB6; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1; OfficeLiveConnector.1.3; OfficeLivePatch.0.0; Sleipnir/2.8.5)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; FDM; Sleipnir/2.8.5)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506; OfficeLiveConnector.1.3; OfficeLivePatch.1.3) Sleipnir/2.8.4",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2; WOW64; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022) Sleipnir/2.8.4",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022) Sleipnir/2.8.4",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; .NET CLR 1.1.4322; InfoPath.1; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30) Sleipnir/2.8.4",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729) Sleipnir/2.8.4",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; User-agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1); .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729) Sleipnir/2.8.4",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729) Sleipnir/2.8.4",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729) Sleipnir/2.8.3",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Sleipnir/2.8.1",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; GTB5; .NET CLR 1.1.4322; .NET CLR 2.0.50727) Sleipnir/2.8.0",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727) Sleipnir/2.8.0",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727) Sleipnir/2.7.2",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.0.3705; .NET CLR 1.1.4322; Media Center PC 4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30) Sleipnir/2.7.1",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322) Sleipnir/2.7.0",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30) Sleipnir/2.6.0",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506; InfoPath.1) Sleipnir/2.5.17",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729) Sleipnir/2.5.12",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; GTB6; .NET CLR 1.1.4322; .NET CLR 2.0.50727) Sleipnir/2.49",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727) Sleipnir/2.48",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; GTB6; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022) Sleipnir/2.46",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.0.3705; Media Center PC 3.1; .NET CLR 2.0.50727; .NET CLR 1.1.4322) Sleipnir/2.30",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; InfoPath.1) Sleipnir/2.21",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Sleipnir 2.8.4)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; SlimBrowser)",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit/528.16 (KHTML, like Gecko) Stainless/0.5.3 Safari/525.20.1",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_5; zh-tw) AppleWebKit/525.27.1 (KHTML, like Gecko) Stainless/0.4.5 Safari/525.20.1",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_5; zh-tw) AppleWebKit/525.27.1 (KHTML, like Gecko) Stainless/0.4 Safari/525.20.1",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_5; en-us) AppleWebKit/528.1 (KHTML, like Gecko) Stainless/0.3.5 Safari/525.20.1",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/528.1 (KHTML, like Gecko) Version/4.0 Safari/528.1 Stainless/0.1",\
        "Mozilla/5.0 (compatible; Sundance/0.9x)",\
        "Mozilla/5.0(Compatible; Windows; U; en-US;) Sundance/0.9",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_5; ja-jp) AppleWebKit/525.18 (KHTML, like Gecko) Sunrise/1.7.5 like Safari/5525.20.1",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_2; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Sunrise/1.7.1 like Safari/5525.18",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; fr) AppleWebKit/523.12.2 (KHTML, like Gecko) Sunrise/1.6.0 like Safari/523.12.2",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/125.5.7 (KHTML, like Gecko) SunriseBrowser/0.853",\
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/125.5.7 (KHTML, like Gecko) SunriseBrowser/0.833",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.8.1.24) Gecko/20100228 Sylera/3.0.20 SeaMonkey/1.1.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.9) Gecko/20071110 Sylera/3.0.20 SeaMonkey/1.1.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.1.9) Gecko/20071110 Sylera/3.0.20 SeaMonkey/1.1.6",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; TencentTraveler 4.0; Trident/4.0; SLCC1; Media Center PC 5.0; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30618)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; iCafeMedia; TencentTraveler 4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; QQPinyin 686; QQDownload 661; GTB6.6; TencentTraveler 4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.2)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0; .NET CLR 2.0.50727; AskTB5.6)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; TencentTraveler 4.0; GTB6.5; SV1; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) )",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; TencentTraveler 4.0; (R1 1.5); .NET CLR 2.0.50727)",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 551; QQDownload 661; TencentTraveler 4.0; (R1 1.5))",\
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QQPinyin 730; SV1; TencentTraveler 4.0; .NET CLR 2.0.50727)",\
        "Mozilla-based browser closely related to Mozilla Firefox, written for PowerPC-based Macintosh computers running Mac OS X to retain compatibility with the older architecture and older versions of the operating system",\
        "Mozilla/5.0 (Macintosh; PPC Mac OS X 10.4; rv:10.0.2) Gecko/20120217 Firefox/10.0.2 TenFourFox/G3",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; TheWorld)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; TheWorld)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; TheWorld)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET CLR 1.1.4322; Tablet PC 2.0; TheWorld)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3; TheWorld)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.2; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E; TheWorld)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB6.6; TheWorld)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; AskTbFXTV5/5.9.1.14019; TheWorld)",\
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; (R1 1.6); .NET CLR 2.0.50727; TheWorld)",\
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; TheWorld)",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1pre) Gecko/20090629 Vonkeror/1.0",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR) AppleWebKit/533.3 (KHTML, like Gecko) WeltweitimnetzBrowser/0.25 Safari/533.3",\
        "Web browser based on Mozilla Firefox",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.6) Gecko/20100121 Firefox/3.5.6 Wyzo/3.5.6",\
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.0.9) Gecko/2009042410 Firefox/3.0.9 Wyzo/3.0.3",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.0.9) Gecko/2009042410 Firefox/3.0.9 Wyzo/3.0.3",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.0.9) Gecko/2009042318 Firefox/3.0.9 Wyzo/3.0.3",\
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.0.9) Gecko/2009042318 Firefox/3.0.9 Wyzo/3.0.2",\
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070801 Firefox/2.0 Wyzo/0.5.3",\

        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
       ]