# -*- coding: utf-8 -*-
from requests import request
import json
header={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
}
url = 'http://v.juhe.cn/toutiao/index?type=top&key=3392b38739ce9fff2b0415ef66582aa5'
response=request('GET',url,headers=header) #定义头信息发送请求返回response对象
#print(response.url) #返回请求的URL
print(response.status_code)  #返回状态码200
print(response.encoding)  #返回编码
#print(response.text)  #返回响应的内容以unicode表示
# print(response.headers) #返回头信息
# print(response.cookies) #返回cookies CookieJar
print(response.json()) #返回json数据

dir = response.json()
dict =dir['result']['data']

for dict_value in dict:
    print(dict_value['title'] +"  "+ dict_value['url'])

