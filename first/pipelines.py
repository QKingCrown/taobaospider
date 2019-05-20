# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql



class FirstPipeline(object):
    def __init__(self):
        pass
    def open_spider(self,spider):
        print('爬虫开启+++++++++++++++++++++++++++++++++++++++++')
        print('开始连接数据库')
        self.conn = pymysql.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            password = 'qin5812555',
            db = 'taobao',
            charset = 'utf8'
        )
        print('链接完成')
        self.cur = self.conn.cursor()
    def process_item(self, item, spider):
        print('=========================')
        sql = "INSERT INTO taobao1 VALUES(NULL,'%s','%s')"%(item['name'],item['money'])
        print("村一条数据")
        self.cur.execute(sql)
        self.conn.commit()
        return item
    def close_spider(self,spider):
        self.cur.close()
        self.conn.close()