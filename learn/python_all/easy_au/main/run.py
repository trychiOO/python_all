# -*- coding: utf-8 -*-
import unittest
# from  easy_au.es_utils.fun_get_post import fun_method
from  easy_au.unit_test.test_case1 import Test1
from util import HTMLTestRunner
from  easy_au.util.send_mail import SendEmail
class RunMian:
    def __init__(self):
        self.send_mail = SendEmail()
    def runcase(self):
        suite = unittest.TestSuite()
        suite.addTests(map(Test1, ["test_01", "test_02" ,"test_03","test_04","test_05","test_06"]))
        # suite.addTests(map(Case, ["test_case01", "test_case02"]))
        st = open('../report/report.html', 'wb')
        HTMLTestRunner.HTMLTestRunner(stream=st, title=u'接口自动化测试报告', description=u'QA：chixiaochao').run(suite)
        # 发送邮件带测试报告附件
        self.send_mail.send_main()

if __name__ == '__main__':
    run = RunMian()
    run.runcase()

