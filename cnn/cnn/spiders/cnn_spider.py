__author__ = 'pratik'

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from cnn.items import CnnItem

class CnnSpider(BaseSpider):
    name = "cnn"
    allowed_domains = ["www.cnn.com"]
    start_urls = ["http://www.cnn.com/us"]


    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        headline_list = hxs.select("//*[@id='cnn_mtt1rgtarea']/ul/li")
        latest_headlines = []

        for headline in headline_list:
            latest_headline = CnnItem()
            latest_headline["title"] = headline.select("a/text()").extract()
            latest_headline["link"] = headline.select("a/@href").extract()
            latest_headlines.append(latest_headline)
        print latest_headlines
