# -*- coding: utf8 -*-
import os
import requests
import configparser as cparser
# 读取配置文件
basepath = os.path.dirname(os.path.dirname(__file__))
cf = cparser.ConfigParser()
cfg_path = basepath + '/config.ini'
cf.read(cfg_path)
class RequestMethod():
    # 初始化参数
    def __init__(self):
        self.base_url = cf.get('url', 'url')
        self.data = {}
        self.file = {}
    def get(self, url):
        # test_url = self.base_url + url
        test_url = self.base_url
        try:
            return requests.get(url=test_url,timeout=60)
        except TimeoutError:
            return print('%s get request timeout!' % url)

if __name__ == '__main__':
    url = cf.get('url', 'url')
    resp_data= RequestMethod().get(url)

    print(resp_data.json())
    print(resp_data.headers)
    # print(l )
