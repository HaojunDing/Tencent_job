import pymysql


class Mysql_conn(object):
    # 魔术方法, 初始化, 构造函数
    def __init__(self):
        self.db = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, database='zhaopin')
        self.cursor = self.db.cursor()

    # 执行modify(修改)相关的操作
    def ins(self, sql, data):
        self.cursor.execute(sql, data)
        self.db.commit()

    # 魔术方法, 析构化 ,析构函数
    def __del__(self):
        self.cursor.close()
        self.db.close()
