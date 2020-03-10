#-*- coding:utf8 -*-
import os
from public import ReadConfig
import time
import logging

print(os.path.join(ReadConfig.proDir))
class MyLog:
    def __init__(self):
        # 设置日志的目录
        self.resultPath = os.path.join(ReadConfig.proDir, "results")
        if not os.path.exists(self.resultPath):
            os.mkdir(self.resultPath)
        self.logPath = os.path.join(self.resultPath, time.strftime('%Y%m%d%H%M', time.localtime(time.time())))
        if not os.path.exists(self.logPath):
            os.mkdir(self.logPath)
        #初始化
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.info())
        #创建filehander  用于写日志
        fh = logging.FileHandler(os.path.join(self.logPath ,"output.log"))
        #设置日志格式
        formater = logging.Formatter('%(asctime)s - %(name)s - %(filename)s - %(funcName)s - '
                                      '%(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
        #给log 添加 hander
        fh .setFormatter(formater)
        self.logger.addHandler(fh)
    def get_logger(self):
        """
        get logger
        :return:
        """
        return self.logger
if __name__ == '__main__':
    log = MyLog.get_log()
    log.build_case_line("instruct", **{'status': 200, 'text': '-1531917099'})
    # logger = log.get_logger()
    # logger.debug("test debug")
    # logger.info("test info")

