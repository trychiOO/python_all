# -*- coding:utf8 -*-
import os
import configparser
import getPath as getpath

# 获取文件路径
# path = os.path.abspath(__file__)
basepath = getpath.get_basepath()
# 获取.ini的当前路径   os.path.join
config_path = os.path.join(basepath, 'config\config.ini')
conf = configparser.ConfigParser()
class ReadConfig():
    #获取属性值
    def get_http(self,name):
        value = conf.get('http' ,name)
        return value
    def get_email(self , name):
        value = conf.get("EMAIL" , name)
        return value
