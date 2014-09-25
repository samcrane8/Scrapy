__author__ = 'pratik'


from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from craigslist.items import CraigslistItem

#note: base class is baseSpider

class craigslistSpider(BaseSpider):
    #name of spider
    name = "craigslist"
    #domain to start from
    allowed_domains = ["craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/npo/"]

    #method parse handles the response from crawl
    def parse(self, response):
        """
        :param response:
        method parse handles response returned from crawl.
        """
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("//span[@class='pl']")
        items = []
        for title in titles:
            item = CraigslistItem()
            item["title"] = title.select("a/text()").extract()
            item["link"] = title.select("a/@href").extract()
            items.append(item)
        return items


