 # -*- coding:utf8 -*-
import unittest


class Test(unittest.TestCase):
    # 初始化 setup
    def setUp(self):
        self.i = 'ss'

    def test_case(self):
        self.assertEqual(self.i, 'ss', msg=['not 10'])

    def test_case1(self):
        self.assertIn(self.i ,'ss' ,msg=["msg"])

    @unittest.skip('skip')
    def test_case2(self):
        self.assertEqual(self.i, 20, msg=['Your input is not 20'])
    def tearDown(self):
        print('Test Over')

