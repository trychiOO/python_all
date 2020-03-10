import sys
import pymysql
import read.readConfig as readConfig
class MyDB:
    host = readConfig.ReadConfig.get_database("hpst")
    port = readConfig.ReadConfig.get_database("port")
    username = readConfig.ReadConfig.get_database("username")
    password = readConfig.ReadConfig.get_database("password")
    database = readConfig.ReadConfig.get_database("database")

    config = {
        "host":host,
        'user': username,
        'passwd': password,
        'port': int(port),
        'db': database
    }

    def __init__(self):
        self.db = None
        self.cursor = None

    def connectDB(self):
        try:
            self.db = pymysql.connect(config)
            self.cursor = self.db.cursor()
            print("数据库连接成功")
        except ConnectionError as ex:
            print("数据库链接错误："+ex)

    #增删改查 都是这一个方法
    def executeSQL(self,sql,params):
        self.connectDB()
        self.cursor.execute(sql,params)
        self.db.commit()
        return self.cursor

    def get_one(self,cursor):
        value = cursor.fetchone()
        return value

    def closeDB(self):
        self.db.close()
        print("数据库链接关闭")