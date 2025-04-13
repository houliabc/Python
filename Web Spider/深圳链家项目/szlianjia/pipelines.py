# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
import pymysql


class SzlianjiaPipeline:
    # 按顺序执行，不用自己调用
    def open_spider(self,spider):
        print("begin")
        #存文件的方式
        # self.f=open('news.csv','w',encoding='utf-8-sig',newline='')
        # self.wt=csv.writer(self.f)
        # self.wt.writerow(['时间','标题','正文'])
        #存数据库的方式
        # self.conn = pymysql.Connect(host='localhost', user='root', password='123456', port=3306, db='lianjia')
        # self.yb = self.conn.cursor()

    #处理程序，必备的
    def process_item(self, item, spider):
        # csv
        # self.wt.writerow([item['time'],item['title'],item['text']])
        # mysql
        # self.yb.execute('insert into news values(%s,%s,%s)', (item['time'],item['title'],item['text']))  #后面要用元组

        print(item)
        print(1)
        return item
    def close_spider(self,spider):
    #     #csv
    #     # self.f.close()
    #     #mysql
    #     self.yb.close()
    #     self.conn.commit()
    #     self.conn.close()
    #
        print('done')
