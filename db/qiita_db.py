import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from db.mysqlbase import MysqlWrapper

class Qiita(MysqlWrapper):
    def __init__(self):
        super().__init__()

    def get_child(self, c, table):
        print("====== tables ======")
        sql = 'show tables'
        c.execute(sql)
        print(c.fetchall())

b = Qiita()
c = b.get_connection()
b.get_child(c, "qiita")
