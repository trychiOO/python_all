# -*- conding :utf8 -*-
from public.Log import MyLog
from  public import ReadConfig
import os

rc = ReadConfig.ReadConfig('808_config.ini')

class Http:
    def __init__(self):
        self.scheme = rc.get_bs("SCHEME")
        self.ip = rc.get_bs("IP")
        self.port = rc.get_bs("POST")
        self.timeout = rc.get_bs("TIMEOUT")
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.headers = {}
        self.data = {}
        self.url = None
        self.files = {}
        self.state = 0

    def set_url(self, url):
        """
        ½Ó¿ÚÂ·¾¶
        :param url:
        :return:
        """
        self.url = "%s://%s:%s%s" % (self.scheme, self.ip, self.port, url)
        # print(self.url)

