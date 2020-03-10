# -*- coding:utf-8 -*-
# import json
# import urllib3
# def get_access_token():
#     corp_id = 'ding86f5e54018c1e54835c2f4657eb6378f'
#     corp_secret= ''
#     url = 'https://oapi.dingtalk.com/gettoken?corpid=%s&corpsecret=%s' % (corp_id, corp_secret)
#     request = urllib3.Request(url)
#     response = urllib3.urlopen(request)
#     response_str = response.read()
#     response_dict = json.loads(response_str)
#     error_code_key = "errcode"
#     access_token_key = "access_token"
#     if response_dict.has_key(error_code_key) and response_dict[error_code_key] == 0 and response_dict.has_key(access_token_key):
#         return response_dict[access_token_key]
#     else:
#         return ''
#
#
# def send_text_to_users(access_token, users, text):
#     msg_type, msg = _gen_text_msg(text)
#     return _send_msg_to_users(access_token, users, msg_type, msg)
#
#
# def _gen_text_msg(text):
#     msg_type = 'text'
#     msg = {"content": text}
#     return msg_type, msg
#
#
# def _send_msg_to_users(access_token, users, msg_type, msg):
#     to_users = '|'.join(users)
#     body_dict = {
#         "touser": to_users,
#         "agentid": agent_id,
#         "msgtype": msg_type
#     }
#     body_dict[msg_type] = msg
#     body = json.dumps(body_dict)
#     return _send_msg("https://oapi.dingtalk.com/message/send?access_token=", access_token, body)

# -*- conding:utf8 -*-
from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
import json
bot = None
# def get_news():
#
#     url = "http://open.iciba.com/dsapi/"
#     r = requests.get(url)
#     contents = r.json()['content']
#     translation = r.json()['translation']
#     return contents, translation

def get_news():
    url = "https://www.tianqiapi.com/api/?verson=v1&city=北京"
    r = requests.get(url)
    result = json.loads(r.text)
    cy =result["city"]
    for i in range(3):
        j = result['data'][i]
        k = j.get("week") + " " + j.get("date") + " " + j.get("week") + " " + j.get('tem') + " - " + j.get("tem1")
        print(k)
def login_wechat():
    global bot
    bot = Bot()


def send_news():
    if bot == None:
        login_wechat()
    try:
        my_friend = bot.friends().search(u'老妈')[0]
        my_friend.send(get_news()[0])
        my_friend.send(get_news())
        my_friend.send(u"test！！")
        t = Timer(1, send_news)
        t.start()
    except:
        print(u"failed！！")
if __name__ == "__main__":
    send_news()
