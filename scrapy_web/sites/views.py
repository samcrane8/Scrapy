import sys,os.path
sys.path.append('/var/qa/scrapy/cnn')
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log, signals
from scrapy.xlib.pydispatch import dispatcher
from cnn.spiders.cnn_spider import CnnSpider

def stop_reactor():
    reactor.stop()

dispatcher.connect(stop_reactor, signal=signals.spider_closed)

spider = CnnSpider()
crawler = Crawler(Settings())
crawler.configure()
crawler.crawl(spider)
crawler.start()
log.start()
log.msg('Running reactor...')
items = reactor.run() # the script will block here
print items
log.msg('Reactor stopped.')