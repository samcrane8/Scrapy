# -*- coding: utf-8 -*-

# Scrapy settings for cnn project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'cnn'

SPIDER_MODULES = ['cnn.spiders']
NEWSPIDER_MODULE = 'cnn.spiders'

LOG_STDOUT = True
LOG_FILE = 'cnn.csv'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cnn (+http://www.yourdomain.com)'
