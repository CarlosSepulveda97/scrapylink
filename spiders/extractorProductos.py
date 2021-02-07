import scrapy 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from linkstore.links import LinkstoreLink





#python spider.py

class LinkstoreSpiderT3(CrawlSpider):
    name = 'test3'
    
    allowed_domain = ['https://xxxx']

    start_urls = ['https://xxxx']
    

    headers = {
        "Access-Control-Allow-Origin": "*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.473"
        ,"X-Requested-With": "XMLHttpRequest"
    }


    rules = {

        Rule(
            LinkExtractor(
                allow = (r'#!/Categoria='),
            ),
            follow = True
        ), #link categoria

        Rule(
            LinkExtractor(
                allow = r'#!/Producto='
            ),
            follow = True,
            callback = 'parse_item' 
        )
    }


    def parse_item(self, response):

        item = LinkstoreLink()

        item['url'] = response.url

        yield item