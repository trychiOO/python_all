#coding:utf-8
import  unittest
class Test_baidu(unittest.TestCase):
    def setUp(self):
        #初始化 ，在用于测试用例执行前，例如连接数据库
        return self
    def test_case1(self):
        #测试用例  以 test 开头
        print('hhh')
    @unittest.skip('跳过')
    def test_case2(self):
        return self
    def test_case3(self):
        return self
    def tearDown(self):
        #在测试用例最后执行 ，例如关闭数据库
        return self
    def method(self):
        #request
        print('func')
if __name__ == '__main__':
    # 方法一
    # unittest.main()

    #方法二
    # suit = unittest.TestSuite()
    # suit.addTest(Test_baidu('test_case1'))
    # runner = unittest.TextTestRunner()
    # runner.run(suit)


    #方法三
    # test_dir = './../../'
    # print(test_dir)
    # discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
    # runner = unittest.TextTestRunner()
    # runner.run(discover)



    print('hah')



