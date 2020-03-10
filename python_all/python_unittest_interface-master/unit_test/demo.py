#coding:utf-8
import requests
import unittest

class Case(unittest.TestCase):

    def test_case01(self):
        #post请求：请求正文是application/x-www-form-urlencoded
        response = requests.post(url='https://www.baidu.com',data={},headers={'Content-Type':'application/x-www-form-urlencoded'})
        self.assertNotEqual(response.url,'https://www.baidu.com','返回状态错误，不为200')
        # self.assertNotEqual( )
        print('接口正常')

    def test_case02(self):
        response = requests.get(url='https://www.baidu.com')
        # print(response1.text)
        self.assertEqual(response.status_code, 200, '返回状态错误，不为400')
        print('接口正常')

# if __name__ == '__main__':
#     unittest.main()