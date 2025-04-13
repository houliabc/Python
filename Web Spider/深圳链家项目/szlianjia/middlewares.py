# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from random import choice

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class SzlianjiaSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class SzlianjiaDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        # 定义一个常见浏览器User-Agent列表
        # user_agent_list = [
        #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        #     "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        #     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        #     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        #     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0",
        #     "Mozilla/5.0 (X11; Linux i686; rv:89.0) Gecko/20100101 Firefox/89.0",
        #     "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:89.0) Gecko/20100101 Firefox/89.0",
        #     "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        #     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
        #     "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0)",
        #     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/3.0)",
        #     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
        #     "Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.17",
        #     "Opera/9.80 (Macintosh; Intel Mac OS X 10_15_7) Presto/2.12.388 Version/12.17",
        #     "Opera/9.80 (X11; Linux x86_64) Presto/2.12.388 Version/12.17",
        #     "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1",
        #     "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1",
        #     "Mozilla/5.0 (iPod touch; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1"
        # ]
        # request.headers.setdefault('User-Agent', choice(user_agent_list))
        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)

# class DisableCookiesMiddleware:
#     def process_request(self, request, spider):
#         request.meta['dont_merge_cookies'] = True

# from selenium import webdriver
# import pytesseract
# from PIL import Image
#
# class CaptchaMiddleware:
#     def process_response(self, request, response, spider):
#         if '人机验证' in response.text:  # 这里根据实际遇到验证码时网页的特征来判断是否出现验证码
#             driver = webdriver.Chrome()
#             driver.get(request.url)
#             driver.find_element_by_xpath('//div[@class="bk-captcha-btn"]').click()
#
#             # 找到验证码图片元素并截图
#             captcha_img = driver.find_element_by_xpath('//img[@class="image-code"]')  # 根据实际验证码图片的xpath来修改
#             captcha_img.screenshot('captcha.png')
#
#             # 使用pytesseract识别验证码
#             captcha_text = pytesseract.image_to_string(Image.open('captcha.png'))
#
#             # 找到验证码输入框并输入验证码
#             captcha_input = driver.find_element_by_xpath('//div[@class="on"]')  # 根据实际验证码输入框的xpath来修改
#             captcha_input.send_keys(captcha_text)
#
#             # 提交验证码表单（假设是通过点击按钮提交，根据实际情况修改）
#             # submit_button = driver.find_element_by_xpath('//button[@type="submit"]')
#             # submit_button.click()
#
#             # 获取提交验证码后的页面内容
#             new_response = webdriver.Remote(driver.command_executor._url, driver.session_id)
#             return new_response
#         return response