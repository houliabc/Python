import scrapy
from szlianjia.items import SzlianjiaItem

class LianjiaSpider(scrapy.Spider):
    name = "lianjia"
    # allowed_domains = ["lianjia.com"]
    start_urls = ["https://sz.lianjia.com/ershoufang/"]

    def parse(self, response):
        print(response)
        ul=response.xpath("//ul[@class='sellListContent']/text()").extract_first()
        for i in ul:
            item=SzlianjiaItem()
            # 取详细页的信息
            a = i.xpath('.//a[@class="noresultRecommend img LOGCLICKDATA"]/@href').extract_first()
            print(a)
            if ('..' in a):
                detail_url = "https://www.szpu.edu.cn" + a[2:]
            else:
                detail_url = a
            yield scrapy.Request(
                url=detail_url,
                callback=self.detail_page,
                meta={'data':item}  # meta是一个字典，通过另一种方式取管道的item
            )
            # yield item  #回到管道里面
    #
    #     # 模拟翻页
    #     # 1、提取出部分url，组合成新的url
    #     part_url = response.css('span.p_next.p_fun a::attr(href)').extract_first()
    #     part_url = response.xpath('//span[@class="p_next p_fun"]/a/@href').extract_first()
    #     if ('szyw' in part_url):
    #         next_url = "https://www.szpu.edu.cn/xwzt/" + part_url
    #     elif (part_url == None):
    #         print("结束")
    #     else:
    #         next_url = "https://www.szpu.edu.cn/xwzt/szyw/" + part_url
    #     # 2、封装成Request请求传给引擎
    #     yield scrapy.Request(
    #         url=next_url,
    #         callback=self.parse  # 指出解析方法，不用括号
    #     )
    #
    def detail_page(self, response):  # 新闻详细页面的处理方法
        # item = response.meta['data']
        # item['housename'] = response.xpath('//div[@class="title"]/h1[@class="main"]/text()').extract_first()
        # item['coummunityname'] = response.xpath('//div[@class="communityName"]/a[@class="info "]/text()').extract_first()
        # item['address'] = response.xpath('//div[@class="areaName"]/a/text()').extract()
        # item['housetype'] = response.xpath('//div[@class="room"]/div[@class="mainInfo"]/()').extract_first()
        # item['area'] = response.xpath('//div[@class="area"]/div[@class="mainInfo"]/text()').extract_first()
        # item['floor'] = response.xpath('//div[@class="room"]/div[@class="subInfo"]/text()').extract_first()
        # item['total'] = response.xpath('//div[@class="price "]/span[@class="total"]/text()').extract_first()
        # item['unit'] = response.xpath('//div[@class="unitPrice"]/div[@span="unitPriceValue"]/text()').extract_first()
        # #this
        # item['agent'] = response.xpath('//div[@class="area"]/div[@class="mainInfo"]/text()').extract_first()
        # item['number'] = response.xpath('//div[@class="area"]/div[@class="mainInfo"]/text()').extract_first()

        item = {}
        item['housename'] = response.xpath('//div[@class="title"]/h1/text()').extract_first()
        item['coummunityname'] = response.xpath('//div[@class="communityName"]/a[1]/text()').extract_first()
        item['address'] = response.xpath('//div[@class="areaName"]/span[@class="info"]/text()').extract_first()
        item['housetype'] = response.xpath('//div[@class="room"]/div[@class="mainInfo"]/text()').extract_first()
        item['area'] = response.xpath('//div[@class="area"]/div[@class="mainInfo"]/text()').extract_first()
        item['floor'] = response.xpath('//div[@class="room"]/div[@class="subInfo"]/text()').extract_first()
        item['total'] = response.xpath('//span[@class="total"]/text()').extract_first()
        item['unit'] = response.xpath('//span[@class="unitPriceValue"]/text()').extract_first()
        item['agent'] = response.xpath('//div[@class="brokerInfoText"]/a/text()').extract_first()
        item['number'] = response.xpath('//div[@class="brokerInfoText"]/span[@class="phone"]/text()').extract_first()
        yield item