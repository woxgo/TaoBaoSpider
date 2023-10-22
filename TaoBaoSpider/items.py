# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TaospiderItem(scrapy.Item):
    title = scrapy.Field()  # 标题
    price = scrapy.Field()  # 价格
    deal_count = scrapy.Field()  # 销量
    shop = scrapy.Field()  # 店铺名称
    location = scrapy.Field()  # 店铺地址

