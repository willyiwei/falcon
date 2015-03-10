# -*- coding: utf-8 -*-

# Scrapy settings for sttest project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'sttest'

SPIDER_MODULES = ['sttest.spiders']
NEWSPIDER_MODULE = 'sttest.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sttest (+http://www.yourdomain.com)'

###############################################################################

#
#  Followings are add by Junkai, control settings by ourself
#

CONCURRENT_REQUESTS = 20
# LOG_LEVEL = 'INFO'
RETRY_ENABLED = False
DOWNLOAD_TIMEOUT = 200
REDIRECT_ENABLED = True
AJAXCRAWL_ENABLED = True


#
# Enable random UserAgent
#
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' :None,
    'sttest.middleware.rotate_useragent.RotateUserAgentMiddleware' :400
}

ITEM_PIPELINES = {
    'sttest.pipelines.JsonWriterPipeline': 800,
}

# AUTOTHROTTLE_ENABLED = True
# AUTOTHROTTLE_START_DELAY
# AUTOTHROTTLE_MAX_DELAY = 0.5
# AUTOTHROTTLE_DEBUG
# CONCURRENT_REQUESTS_PER_DOMAIN
# CONCURRENT_REQUESTS_PER_IP
# DOWNLOAD_DELAY
