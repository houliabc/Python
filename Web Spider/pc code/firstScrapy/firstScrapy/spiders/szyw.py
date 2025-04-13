import scrapy
from firstScrapy.items import FirstscrapyItem

class SzywSpider(scrapy.Spider):
    name = "szyw"
    allowed_domains = ["www.szpu.edu.cn"]  #不用协议名http
    start_urls = ["https://www.szpu.edu.cn/xwzt/szyw.htm"]
    # start_urls = ["https://www.szpu.edu.cn/xwzt/szyw/"+str(i)+".htm" for i in range(1,107)].append(start_urls)

    #下载器自动打包的response
    def parse(self, response):
        # xpath
        # lis=response.xpath('//ul[@class="list23"]/li')
        # for i in lis:
        #     title=i.xpath('.//h4/text()').extract_first()  #不会报错
        #     text = i.xpath('.//p/text()').extract_first()
        #     time = i.xpath('.//h6/text()').extract_first()
        #     #等价于，区别是上面取列表，因此列表没数据访问[0]会报错；下面表示取一个没数据只是None

        #css
        li=response.css('ul.list23 li')
        for i in li:
            item=FirstscrapyItem()
            item['title']=i.css('h4::text').extract_first()  #两个冒号取text或者属性attr(属性名)，不用引号
            item['text'] = i.css('p::text').extract_first()
            item['time']=i.css('h6::text').extract_first()
            # text_attr = i.css('p::attr(class)').extract_first()  #取属性值

            #取详细页的信息
            a=i.xpath('./a[@class="a flex"]/@href').extract_first()
            if ('..' in a):
                detail_url="https://www.szpu.edu.cn"+a[2:]
            else:
                detail_url=a
            yield scrapy.Request(
                url=detail_url,
                callback=self.detail_page,
                meta={'data':item}   #meta是一个字典，通过另一种方式取管道的item
            )
            # yield item  #回到管道里面

        #模拟翻页
        #1、提取出部分url，组合成新的url
        part_url = response.css('span.p_next.p_fun a::attr(href)').extract_first()
        part_url=response.xpath('//span[@class="p_next p_fun"]/a/@href').extract_first()
        if ('szyw' in part_url):
            next_url = "https://www.szpu.edu.cn/xwzt/"+part_url
        elif (part_url==None):
            print("结束")
        else:
            next_url = "https://www.szpu.edu.cn/xwzt/szyw/" + part_url
        #2、封装成Request请求传给引擎
        yield scrapy.Request(
            url=next_url,
            callback=self.parse  #指出解析方法，不用括号
        )

    def detail_page(self,response):   #新闻详细页面的处理方法
        item=response.meta['data']
        item['author']=response.xpath('//div[@class="v_news_content"]/p[last()]/text()').extract_first()[1:-1]
        yield item