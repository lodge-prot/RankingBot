import MySQLdb
import json

class MysqlWrapper:
    def __init__(self, conf="db/db_config.json"):
        with open(conf, 'r') as f:
            js = json.load(f)
            self.__user   = js["user"]
            self.__passwd = js["passwd"]
            self.__port   = js["port"] or "3306"
            self.__host   = js["host"] or "localhost"
            self.__db     = js["db"]

        # コネクション生成
        self.conn  = MySQLdb.connect(
            #unix_socket = '/Applications/MAMP/tmp/mysql/mysql.sock',
            user   = self.__user,
            passwd = self.__passwd,
            host   = self.__host,
            db     = self.__db
        )

        # メタデータ設定
        self.conn.set_character_set('utf8')
        self.cur = self.conn.cursor()
        self.cur.execute('SET NAMES utf8;')
        self.cur.execute('SET CHARACTER SET utf8;')
        self.cur.execute('SET character_set_connection=utf8;')

    def get_connection(self):
        """
        カーソル取得関数
        """
        return self.cur

    def get_data_list(self, table):
        """
        sample sql
        """
        print("====== tables ======")
        sql = 'show tables'
        self.cur.execute(sql)
        print(self.cur.fetchall())

        print("====== Colums ======")
        sql = "show columns from " + table
        self.cur.execute(sql)
        print(self.cur.fetchall())

        print("====== Results ======")
        sql = "select * from " + table
        self.cur.execute(sql)
        results = self.cur.fetchall()
        for r in results:
            print(r)
