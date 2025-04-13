import scrapy


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["www.baidu.com"]  #不用协议名http
    start_urls = ["https://www.baidu.com"]

    #下载器自动打包的response
    def parse(self, response):
        # print(response.text)
        # print(response.status)
        #这里不用转换etree
        lis=response.xpath('//ul[@id="hotsearch-content-wrapper"]/li')
        for i in lis:
            #这里取text还是一个选择器，要用extract取出data
            title=i.xpath('.//span[@class="title-content-title"]/text()[0]').extract()  #[0]也可以放最后，即extract后
            #等价于，区别是上面取列表，因此列表没数据访问[0]会报错；下面表示取一个没数据只是None
            # title = i.xpath('.//span[@class="title-content-title"]/text()').extract_first()
            print(title)
