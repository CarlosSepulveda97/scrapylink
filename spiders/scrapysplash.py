import scrapy
from scrapy.selector import Selector
from scrapy_splash import SplashRequest
from linkstore.items import LinkstoreItem
from linkstore.ToList import formaterList

class CartierSpider(scrapy.Spider):
    name = 'test6'
    
    def start_requests(self):
        urls = formaterList()
        #cont = 0
        #limit = 40 
        for url in urls:
            #if (cont==limit):
            ##    break    
            #cont+=1
            yield SplashRequest(url, self.parse, args={'wait': 5})

    def parse(self, response):
    
        yield{
            'tituloProducto' : Selector(text=response.body).xpath('//*[@id="DetalleProducto"]/header/h1/text()').extract()[0],
            'codigoProducto' : Selector(text=response.body).xpath('//*[@id="DetalleProducto"]/div/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td[2]/text()').extract()[0].strip(),
            'stockTransitoProducto' : Selector(text=response.body).xpath('//*[@id="DetalleProducto"]/div/table/tbody/tr[1]/td[2]/table/tbody/tr[3]/td[2]/text()').extract(),
            #'descripcionProducto' : '//*[@id="DetalleProducto"]/div/table/tbody/tr[2]/td/table/tbody/tr/td[1]/div',#text
            'stockProducto' : Selector(text=response.body).xpath('//*[@id="DetalleProducto"]/div/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td[2]/text()').extract()[0],
            'precioListaProducto' : Selector(text=response.body).xpath('//*[@id="DetalleProducto"]/div/table/tbody/tr[1]/td[2]/table/tbody/tr[4]/td[2]/text()').extract()[0],
            #'linkImgProducto' : '//*[@id="DetalleProducto"]/div/table/tbody/tr[1]/td[1]/div[2]/div[1]/a',#href
            #'MarcaProducto' : '//*[@id="Div_Marca"]'#title
        }



