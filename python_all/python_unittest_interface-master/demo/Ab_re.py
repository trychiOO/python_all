# -*- coding : utf-8 -*-

import requests
url_params = {'type':'top', 'key': '3392b38739ce9fff2b0415ef66582aa5'}

re = requests.get(url='http://v.juhe.cn/toutiao/index',params =url_params )
code = re.status_code

res = requests.get(url = 'https://www.baidu.com')
print(res.headers)
print(res.status_code)
# print(code)
# print(re.url)
# print(re.ok)
# print(re.headers )
# print('______')
# print(re.cookies)
# print('______')
# print(re.content)
# print('______')
# print(re.encoding)
# print('______')
# print(re.raw)
# print(re.status_code)

dict = re.json()['result']['data']
for dict_value in dict:
    data =dict_value['title'] +"  "+ dict_value['url']







