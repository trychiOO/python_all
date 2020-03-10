#-*- coding:utf8 -*-
import requests#导入request模块
import json
url = 'http://apis.juhe.cn/simpleWeather/query?key= 1b43db481985a3748772c8a336ecf5a2&city=北京'
# url = 'https://azero.soundai.cn/v20190530/directives'
headers  = {"Connection":'keep-alive',"Host":"httpbin.org"}#值以字典的形式传入

response = requests.post(url=url,headers=headers)#用关键字headers传入
print(response.headers)#打印出响应头
print(response.headers['Connection'])#取得部分响应头以做判断：
print(response.headers.get('Connection'))#或者这样也可以
print(response.text)