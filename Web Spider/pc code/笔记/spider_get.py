from urllib import request, parse
import time
import random

"""
目标爬取：https://tieba.baidu.com/f?kw=%E8%89%BE%E5%B0%94%E7%99%BB%E6%B3%95%E7%8E%AF&ie=utf-8
学习目标：
    urllib 库，
    get 方法爬取 html 网页，
    标准爬虫程序写法
"""

ua_list = [
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'User-Agent:Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    ' Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1',
    ' Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
]


# 定义一个爬虫类
class TiebaSpider(object):
    # 初始化url属性
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?{}'

    def get_html(self, url):
        """
        请求函数，得到页面，传统三步
        :param url:
        :return:
        """
        req = request.Request(url=url, headers={'User-Agent': random.choice(ua_list)})
        res = request.urlopen(req)
        # windows会存在乱码问题，需要使用 gbk解码，并使用ignore忽略不能处理的字节
        # linux不会存在上述问题，可以直接使用decode('utf-8')解码
        html = res.read().decode("gbk", "ignore")
        return html

    def parse_html(self):
        """
        解析函数，此处代码暂时省略，还没介绍解析模块
        :return:
        """
        pass

    def save_html(self, filename, html):
        """
        保存文件函数
        :param filename:
        :param html:
        :return:
        """
        with open(filename, 'w') as f:
            f.write(html)

    # 4.入口函数
    def run(self):
        name = "艾尔登法环"
        begin = int(input('输入起始页：'))
        stop = int(input('输入终止页：'))
        # +1 操作保证能够取到整数
        for page in range(begin, stop + 1):
            pn = (page - 1) * 50
            params = {
                'kw': name,
                'pn': str(pn)
            }
            # 拼接URL地址
            params = parse.urlencode(params)
            url = self.url.format(params)
            # 发请求
            html = self.get_html(url)
            # 定义路径
            filename = '{}-{}页.html'.format(name, page)
            self.save_html(filename, html)
            # 提示
            print('第{}页抓取成功'.format(page))
            # 每爬取一个页面随机休眠0-1秒钟的时间
            time.sleep(random.randint(0, 1))


if __name__ == '__main__':
    start = time.time()
    spider = TiebaSpider()  # 实例化一个对象spider
    spider.run()  # 调用入口函数
    end = time.time()
    # 查看程序执行时间
    print('执行时间:%.2f' % (end - start))  # 爬虫执行时间
