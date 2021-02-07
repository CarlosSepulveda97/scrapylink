import scrapy 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class LinkstoreSpiderCat(CrawlSpider):
    name = 'extractorCategorias'
    allowed_domain = ['https://xxxxx']
    start_urls = ['https://xxxxx']
    headers = {
        "Access-Control-Allow-Origin": "*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.473"
    }

    #Debug
    #custom_settings = {
    #    'CLOSESPIDER_PAGECOUNT': 40
    #}

    rules = {

        Rule(
            LinkExtractor(
                allow = (r'#!/Categoria=')
            ),
            follow = True,
            callback = 'guardar_link'   
        ), #link categoria
    }


    def guardar_link(self, response):
        
        yield {
            'url' : response.url 
        }
             