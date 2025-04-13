#处理好清洗好的数据放这里
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstscrapyItem(scrapy.Item):  #items是一个字典
    # define the fields for your item here like:
    #建模过程：爬取的内容
    title = scrapy.Field() #新闻标题
    text = scrapy.Field()  #新闻正文
    time = scrapy.Field()  #新闻时间
    author=scrapy.Field()  #新闻作者
    # pass
# if __name__=='__main__':
#     item=FirstscrapyItem()
#     item['title']='xx'
#     item['text'] = 'hh'
#     item['time'] = 'tt'
#     print(item)