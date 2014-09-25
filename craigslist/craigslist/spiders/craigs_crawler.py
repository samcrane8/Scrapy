from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from craigslist.items import CraigslistItem

#note: base class is crawlSpider

class MySpider(CrawlSpider):
    name = "craigs_crawler"
    allowed_domains = ["sfbay.craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/npo/"]   

    # SgmlLinkExtractor: defines how you want the spider to follow the links
    # allow: defines the link href
    # restrict_xpaths: restricts the link to a certain Xpath
    # callback: calls the parsing function after each page is scraped*
    # follow: instructs whether to continue following the links as long as they exist

    rules = (Rule(SgmlLinkExtractor(allow=("index\d00\.html", ), restrict_xpaths=('//a[@class="button next"]',))
    # callback is the function called after parse returns initial page
    , callback="parse_items", follow= True),)

    def parse_items(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select('//span[@class="pl"]')
        items = []
        for titles in titles:
            item = CraigslistItem()
            item["title"] = titles.select("a/text()").extract()
            item["link"] = titles.select("a/@href").extract()
            items.append(item)
        return items