import pymysql

class ReadDb(object):

    conn = None

    def get_conn(self):
        if self.conn is None:
            self.conn = pymysql.connect(
                host="127.0.0.1",
                user="root",
                password="123456789",
                db="performance_schema",
                charset="utf8"
            )
            return self.conn


    def get_cursor(self):
        return self.get_conn().cursor()


    def close_cursor(self,cursor):
        if cursor:
            cursor.close()


    def close_conn(self):
        if self.conn:
            self.conn.close()
            self.conn = None


    def get_sql_one(self,sql):
        cursor = self.get_cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        data_list = []
        for i in data:
            data_list.append(i)
        self.close_cursor(cursor)
        self.close_conn()
        print(data_list)
        return data_list

if __name__ == '__main__':
    sql = "select * from accounts"
    ReadDb().get_sql_one(sql)