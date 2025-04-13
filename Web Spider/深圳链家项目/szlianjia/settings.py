# Scrapy settings for szlianjia project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "szlianjia"

SPIDER_MODULES = ["szlianjia.spiders"]
NEWSPIDER_MODULE = "szlianjia.spiders"

# 请求头设置
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'

# 遵守robots.txt规则
ROBOTSTXT_OBEY = False

# 并发请求数
CONCURRENT_REQUESTS = 16

# 下载延迟
DOWNLOAD_DELAY = 3
RANDOMIZE_DOWNLOAD_DELAY = True

# 启用Pipeline
ITEM_PIPELINES = {
   "szlianjia.pipelines.SzlianjiaPipeline": 300,
}

# Cookie设置
COOKIES_ENABLED = True
