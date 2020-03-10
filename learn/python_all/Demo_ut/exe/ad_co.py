# -*- coding:utf-8 -*-
import json ,requests
from requests.cookies import RequestsCookieJar

cookie_jar = RequestsCookieJar()
cookie_jar.set("JSESSIONID", "ea65694b-2d6e-408b-be2c-b4994103e7e9", domain="https://azero.soundai.com/")
url_te = 'https://azero.soundai.com/person/findUser'
response = requests.get(url_te, headers=cookie_jar)
# response.encoding('utf-8')
print(type(response.cookies))

# print(r)


