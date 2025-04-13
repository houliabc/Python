from scrapy import cmdline
#execute方法需要传入列表形式的cmd命令，列表每一个元素自动空格分割
#method 1
# cmdline.execute('scrapy crawl szyw'.split())
cmdline.execute('scrapy crawl szyw --nolog'.split())  #看错误用--nolog
#存文件，支持csv和json
# cmdline.execute('scrapy crawl szyw -o news1.csv --nolog'.split())  #通过命令行存文件，需要关闭管道


#method 2
# cmdline.execute(['scrapy','crawl','baidu'])