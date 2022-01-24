import pymysql
import time
"""
    目标：完成数据库相关工具类封装
    分析：
        1.主要方法
            假设：def get_sql_one(sql):获取数据库数据
        2.辅助方法
            1.获取链接对象
            2.获取游标对象
            3.关闭游标对象
            4.关闭链接对象
"""

class ReadDB(object):
    conn = None
    def __init__(self,table):
        self.table = table
    #获取链接对象方法
    def get_conn(self):
        if self.table == 'wms':
            if self.conn is None:
                """
                self.conn = pymysql.connect(host="127.0.0.1",
                            user="root",
                            passwd="123456",
                            db="mysql",
                            charset='utf8')
                """
                self.conn = pymysql.connect(host="10.0.0.127",
                                            port=3306,
                                            user="erp",
                                            passwd="sd)*(YSHDG;l)D_FKds:D#&y}",
                                            db="supply_wms",
                                            charset='utf8')
                return self.conn
        elif self.table == 'ims':
            if self.conn is None:
                """
                self.conn = pymysql.connect(host="127.0.0.1",
                            user="root",
                            passwd="123456",
                            db="mysql",
                            charset='utf8')
                """
                self.conn = pymysql.connect(host="10.0.0.127",
                                            port=3306,
                                            user="erp",
                                            passwd="sd)*(YSHDG;l)D_FKds:D#&y}",
                                            db="supply_ims",
                                            charset='utf8')
                return self.conn

    #获取游标对象方法
    def get_cursor(self):
        return self.get_conn().cursor()


    #关闭游标对象方法
    def close_cursor(self, cursor):
        if cursor:
           cursor.close()

    #关闭链接对象
    def close_conn(self):
        if self.conn:
            self.conn.close()
            #注意：关闭连接对象后，对象还存在内存中，需要手动设置为None
            self.conn = None

    #主要方法  ->在外界调用此方法可以完成数据库相应的操作
    def get_sql_one(self, sql):
        cursor = self.get_cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        self.close_cursor(cursor)
        self.close_conn()
        return data

    def get_sql_many(self, sql, num):
        cursor = self.get_cursor()
        cursor.execute(sql)
        data = cursor.fetchmany(size=num)
        self.close_cursor(cursor)
        self.close_conn()
        return data

    def get_sql_all(self, sql):
        cursor = self.get_cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        self.close_cursor(cursor)
        self.close_conn()
        return data

    def execute(self,sql):

        db = self.get_conn()

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 删除语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交修改
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()

        # 关闭连接
        db.close()
        print('删除操作成功')

if __name__ == '__main__':
    sql = "select * from central_inventory where goods_sku_code = '53586714577' and  warehouse_id = 536;"
    sql_1 = "delete from central_inventory where goods_sku_code = '53586714577' and warehouse_id =536;"
    ReadDB().execute(sql_1)
    ReadDB().get_sql_one(sql)