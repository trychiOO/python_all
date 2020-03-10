#-*- coding:utf8 -*-
import time
import requests
import urllib
import json
def get_y(a, b):
    return lambda x: a * x + b
y1 = get_y(11, 11)
print(y1(2))

L = [lambda x: x + 2, lambda x: x * 2, lambda x: x ** 2]
print("L=", L[0](1), L[1](2), L[1](3))
time.sleep = lambda x: None


print('^^^^^')
# url = "http://open.iciba.com/dsapi/"
# r = requests.Request(url)
# obj = json.dump(r)
# obj = r.json
#obj1 = ('When a man is wrapped up in himself, he makes a pretty little package.', '小编的话：现在的社会存在太多精致的利己主义者，他们视自身的利益为至上，但这种人往往都无法取得巨大成就，因为成大事者往往不拘小节，不去过分计较个人利益得失。')


#url = "http://open.iciba.com/dsapi/"
url = "https://www.tianqiapi.com/api/?verson=v1&city=北京"
r = requests.get(url)
print(type(r))
print(type(r.text))
result = json.loads(r.text)  # 字符串转字典
print("####")
print(type(result))
#dict = result
j = result['data'][1]
k = j.get("week")+" "+j.get("date")+" "+j.get("week")+" "+ j.get('tem')+" - "+j.get("tem1")+" " + j['win'][1]
#k1 = j['win'][1]
#k = j["day","date","week","tem1"]
print("^^^^^^^^^^^^^^")
print(j)
print(k)



# for i in dict["data"]["day"]:
#     print(i["alarm_type"])

#contents = r.json.loads()['data']
#print(type(contents))
#content_1 =contents[1:5]
#d = contents.get("translation")
#translation = r.json()['translation']
# print(content_1)

list = ['123','abc','@#$']

l = list[1][1]
print(l)



