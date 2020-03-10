# -*- coding:utf-8 -*-
import unittest
import json
import os
import configparser
from util import Get_cookies

from es_utils.fun_get_post import fun_method

class Test1(unittest.TestCase):
    global headers
    headers = {
        'cookie': 'JSESSIONID=2E82424A7758A44BC2F9026E98A1EE60;UM_distinctid=16e69c2322625c-06eb5d3e484af5-7711a3e-1fa400-16e69c232278d2',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin', 'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

    @classmethod
    def setUpClass(cls):
        # print("类执行之前的方法")
        pass
    @classmethod
    def tearDownClass(cls):
        # print("类执行之后的方法")
        pass
    #每次方法前执行
    def setUp(self):
        self.run = fun_method()
    #每次方法后执行
    def tearDown(self):
        pass
    def test_01(self):
        # headers = {'Date': 'Fri, 11 Oct 2019 11:14:27 GMT', 'Content-Type': 'application/json;charset=utf-8',
        #            'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive',
        #            'Set-Cookie': 'aliyungf_tc=AQAAAKVh/l7WJg8AIoFFeegjpeVN6qjg; Path=/; HttpOnly',
        #            'Etag': '3af2b8bbb189b4c22cd9a06e6edd0255'}
        # url_params = {'type': 'top', 'key': '3392b38739ce9fff2b0415ef66582aa5'}
        # # res = self.run.run_main(self ,url='http://v.juhe.cn/toutiao/index' ,params= url_params ,None, headers = headers , 'GET' )
        # res = self.run.run_main(url='http://v.juhe.cn/toutiao/index',params=url_params,data=None,headers=headers,method='GET')
        # print(res.url)
        # self.assertEqual(res.status_code, '200', '返回状态错误，不为200')
        # run_main(self,url,params,data,headers,method):
        headers = {
                    'cookie': 'JSESSIONID=36731B6892C63024CE5520785BB6A6FE'
            ,'sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        res= self.run.fun_main(url='https://azero.soundai.com/person/findUser',params=None,data=None,headers=headers,method='POST')
        print(res.url)
        print(res.json()['message'])
        print(res.encoding)
        # print(res.content)
        self.assertEqual(str(res.json()['message']), 'success', '请求失败，不为success')
        # code = re.status_code
        #         # url = 'https://www.baidu.com'
        #         # res = self.run.run_main(url,None,None,headers,'GET')
        #         # print(res)
        #         # self.assertEqual(res.status_code, '200', '返回状态错误，不为200')
        #         # self.assertEqual(res.get("code"), '200', '返回状态错误，不为200')
        #         # self.assertEqual(res['value']['name'],'so')
        #         # print("这是第一个测试方法")
    @unittest.skip

    def test_02(self):
        url = 'https://azero.soundai.com/index'
        headers ={
            'cookie': 'JSESSIONID=ea65694b-2d6e-408b-be2c-b4994103e7e9', 'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin', 'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

        res = self.run.fun_main(url,params= None,data = None, headers = headers, method = 'GET')
        # print(type())
        self.assertEqual(res.status_code, 200, '返回状态错误，不为200')
        # print(res.title)
        # self.assertIn('首页' ,'页面打开不正确')
        print("首页面")

    def test_03(self):
     url = 'https://azero.soundai.com/ask/home'
     res = self.run.fun_main(url, params = None, data=None ,headers= None, method = 'GET')
     print(res)
     self.assertEqual(res.status_code, 200, '返回状态错误，不为200')
     print("接入技能页面")
    def test_04(self):
     url = 'https://azero.soundai.com/ask/category'
     res = self.run.fun_main(url, params = None, data=None ,headers= None, method = 'GET')
     print(res)
     self.assertEqual(res.status_code, 200, '返回状态错误，不为200')
     print("创建技能页面")

    def test_05(self):
     url = 'https://azero.soundai.com/ask/own-skills'
     res = self.run.fun_main(url, params = None, data=None ,headers= None, method = 'GET')
     print(res)
     self.assertEqual(res.status_code, 200, '返回状态错误，不为200')
     print("已创建技能页面")
    def test_06(self):
         url = 'https://azero.soundai.com/v1/ask/skills'   #https://azero.soundai.com/v1/ask/skill/
         headers = {
             'cookie': 'JSESSIONID=ea65694b-2d6e-408b-be2c-b4994103e7e9', 'sec-fetch-mode': 'navigate',
             'sec-fetch-site': 'same-origin', 'upgrade-insecure-requests': '1',
             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
         res = self.run.fun_main(url =url, params='5df22e239810ea0008919719/1?_=1576239076717', data=None, headers=headers, method='GET')
         # me = res.json()

         # print("&&&&&&&")
         print(res.json()['message'])
         # print(me)
         # print("^^^^^")
         self.assertEqual(str(res.json()['message']), 'success', '请求失败，不为success')
         print("已创建技能_查询成功")
    def test_07(self):
         url = 'https://azero.soundai.com/v1/ask/skill/5dadaa2c3b36210006ed9c14/1?_=1572242791353'
         headers = {
             'cookie': 'JSESSIONID=ea65694b-2d6e-408b-be2c-b4994103e7e9', 'sec-fetch-mode': 'navigate',
             'sec-fetch-site': 'same-origin', 'upgrade-insecure-requests': '1',
             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

         res = self.run.fun_main(url =url, params=None, data=None, headers=headers, method='GET')
         print(res.url)
         print(res.json()['message'])
         self.assertEqual(str(res.json()['message']), 'success', '请求失败，不为success')
         print("已创建技能_查询成功")

    def test_08(self):
         url = 'https://azero.soundai.com/v1/ask/skill/5dadaa2c3b36210006ed9c14/1?_=1572242791353'
         headers = Test1.headers;

         res = self.run.fun_main(url =url, params=None, data=None, headers=headers, method='GET')
         print(res.url)
         print(res.json()['message'])
         self.assertEqual(str(res.json()['message']), 'success', '请求失败，不为success')
         print("已创建技能_查询成功")
    # 'https://azero.soundai.com/v1/ask/skill/5dadaa2c3b36210006ed9c14/1?_=1572242791353'