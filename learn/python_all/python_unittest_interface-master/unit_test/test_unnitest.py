#coding:utf-8
import unittest
from util.test_get_post import Runmain

class Test(unittest.TestCase):

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
        self.run = Runmain()

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
        headers = {'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Connection': 'Keep-Alive',
         'Content-Encoding': 'gzip', 'Content-Type': 'text/html', 'Date': 'Fri, 11 Oct 2019 11:55:47 GMT',
         'Last-Modified': 'Mon, 23 Jan 2017 13:23:55 GMT', 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18',
         'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/', 'Transfer-Encoding': 'chunked'}
        res= self.run.run_main(url='http://www.baidu.com',params=None,data=None,headers=None,method='GET')
        self.assertEqual(str(res.status_code), '200', '返回状态错误，不为200')
        print(res.url)
        # code = re.status_code
        # url = 'https://www.baidu.com'


        # res = self.run.run_main(url,None,None,headers,'GET')
        # print(res)
        # self.assertEqual(res.status_code, '200', '返回状态错误，不为200')
        # self.assertEqual(res.get("code"), '200', '返回状态错误，不为200')
        # self.assertEqual(res['value']['name'],'so')
        # print("这是第一个测试方法")


    @unittest.skip("无条件跳过此用例")
    def test_02(self):
        url = 'www.baidu.com'
        params = {"bizName":"globalSearchClient","sign":"8c8bc3ee9d6c4b7b8a390ae298cb6db5","timeMills":"1524906299999"}
        res = self.run.run_main(url,params,None,None,'GET')
        print(res)
        self.assertEqual(res['code'], '200', '返回状态错误，不为200')
        print("这是第二个测试方法")



