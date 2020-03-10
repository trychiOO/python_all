# -*- coding:utf8 -*-
import unittest
import HTMLTestRunner
#test_dir1 = r'D:\PycharmProjects\WechatHelper-master\Demo_ut'
test_dir = './'
suite = unittest.TestSuite
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
fb = open('result.html','wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fb, title='DM_Baidu', description='测试情况')
    # 生成执行用例的对象
runner.run(discover)
    # 执行测试套件
fb.close()





# suite = unittest.TestSuite()#创建测试套件
# all_cases = unittest.defaultTestLoader.discover('.','test_*.py')
# #找到某个目录下所有的以test开头的Python文件里面的测试用例
# for case in all_cases:
#             suite.addTests(case)#把所有的测试用例添加进来
# fp = open('res.html','wb')
# runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='all_tests',description='所有测试情况')
# runner.run(suite)
#         #运行测试






#
# if __name__ == '__main__':
#     # unittest.main()
#     # 使用HTMLTestRunner进行测试
#     suite = unittest.TestSuite()#多个测试用例使用测试套件
#     suite.addTest(Test("test_login_one"))#添加用例1
#     suite.addTest(Test("test_login_two"))#添加用例2
#     with open("report.html","wb") as f:
#         runner = HTMLTestRunner(
#             stream=f,#文件
#             title="58登录测试",#标题
#             description="简单的账户登录自动化测试"#描述
#         )
#         runner.run(suite)#启动测试套件
