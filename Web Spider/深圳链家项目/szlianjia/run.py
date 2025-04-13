from scrapy import cmdline
#execute方法需要传入列表形式的cmd命令，列表每一个元素自动空格分割
cmdline.execute('scrapy crawl lianjia --nolog'.split())  #看错误用--nolog
# cmdline.execute('scrapy crawl lianjia'.split())  #看错误用--nolog