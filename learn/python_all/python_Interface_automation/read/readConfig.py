import os
import configparser
import getPath as getpath

#获取文件路径
basepath = getpath.get_basepath()
config_path = os.path.join(basepath,'config\config.ini')
config = configparser.ConfigParser()
class ReadConfig():
    #获取名字为 [HTTP] 的属性值
    def get_http(self,name):
        value = config.get('HTTP' , name)
        return value
    def get_email(self,name):
        value = config.get('EMAIL' , name)
        return value
    def get_database(self,name):
        value = config.get('DATABASE' , name)
        return value

