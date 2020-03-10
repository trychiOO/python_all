import json
import Demo_ut
import paramunittest
import urllib.parse
import read.readExcel as readExcel
from common.configHttp import RunMain
import read.readConfig as readConfig

login_xls = readExcel.ReadExcel().get_xls("login.xls","login")
url = readConfig.ReadConfig().get_http("loginurl")

@paramunittest.parametrized(*login_xls)
class testUserLogin(Demo_ut.TestCase):
    def setParameters(self,case_name,key,city,method):
        self.case_name = str(case_name)
        self.path = str(key)
        self.data = str(city)
        self.method = str(method)

    def description(self):
        self.case_name

    def setUp(self):
        print(self.case_name + "测试开始前准备")

    #调用测试方法
    def testLogin(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):
        #将读取到的 data 转为 json格式
        data = json.loads(self.data)
        #调用 configHTTP 类中的run_main方法
        info = RunMain().run_main(self.method,url+self.path,data)
        #将得到的返回值进行格式化并取值判断
        print(info)
        res = json.loads(info)
        # if self.case_name == "login":
        #     self.assertEqual(res['code'],200)
        # if self.case_name == "login_error":
        #     self.assertEqual(res['code'],404)
        #     self.assertEqual(res['msg'], '密码错误')
        # if self.case_name == "login_null":
        #     self.assertEqual(res['code'],404)