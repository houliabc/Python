# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SzlianjiaItem(scrapy.Item):
    # 房子数据包括房子的名字，小区名城，所在地址，房型，面积大小
    # 楼层数，总价，单价，房产经济人，房产经济的电话（请参考以下样例）
    housename = scrapy.Field()
    coummunityname = scrapy.Field()
    address = scrapy.Field()
    housetype = scrapy.Field()
    area = scrapy.Field()
    floor = scrapy.Field()
    total = scrapy.Field()
    unit = scrapy.Field()
    agent = scrapy.Field()
    number = scrapy.Field()
