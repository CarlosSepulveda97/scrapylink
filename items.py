# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LinkstoreItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    tituloProducto = scrapy.Field()
    codigoProducto = scrapy.Field()
    stockProducto = scrapy.Field()
    stockTransitoProducto = scrapy.Field()
    precioListaProducto = scrapy.Field()
    linkImgProducto = scrapy.Field()
    MarcaProducto = scrapy.Field()
    descripcionProducto = scrapy.Field()

    pass


