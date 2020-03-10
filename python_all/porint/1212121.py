# -*- coding:utf8 -*-
from __future__ import unicode_literals
import json
from threading import Timer
from wxpy import *
import requests
from urllib import request


#
# #url = "http://open.iciba.com/dsapi/"
# url = "https://www.tianqiapi.com/api/?verson=v1&city=北京"
# r = requests.get(url)
# result = json.loads(r.text)
# for i in range(3):
#      j = result['data'][i]
#      k = j.get("week") + " " + j.get("date")+" "+j.get("week")+" "+ j.get('tem')+" - "+j.get("tem1")
#      print(k)
# # j = result['data'][1]
# # k = j.get("week")+" "+j.get("date")+" "+j.get("week")+" "+ j.get('tem')+" - "+j.get("tem1")+" " + j['win'][1]
# # print(k)

def get_news():
    url = "https://www.tianqiapi.com/api/?verson=v1&city=北京"
    r = requests.get(url)
    result = json.loads(r.text)
    cy = result["city"]
    for i in range(2):
        j = result['data'][i]
        k = j.get("week") + " " + j.get("date") + " " + j.get("week") + " " + j.get('tem') + " - " + j.get("tem1")+" "+cy
        return k

def sed_news():

 if __name__ == "__main__":
    l = get_news()
    print(l)

