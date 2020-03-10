# -*- coding:utf8 -*-
# from selenium import webdriver
# # import unittest
# import  json
# from  selenium  import webdriver
# from selenium.webdriver.chrome.options import Options
#
# #   使用 selenium 无头模式  进行登录
# #   获取登录后的cookies
#
# chrome_options = Options()
# # 启动无头模式
# chrome_options.add_argument('--headless')
# #防止bug
# chrome_options.add_argument('--disable_gpu')
# #初始化
# class getCookies:
#     def cookies():
#         driver = webdriver.Chrome(options=chrome_options)
#         baseUrl='https://login.soundai.com/login?redirect_url=https%3A%2F%2Fazero.soundai.com%2Findex&request_type=userLogin'
#         driver.get(baseUrl)
#         driver.find_element_by_xpath('//*[@id="pane-userLogin"]/form/div[1]/div/div[1]/input').send_keys('17853487243')
#         driver.find_element_by_xpath('//*[@id="pane-userLogin"]/form/div[2]/div/div/input').send_keys('chi902600')
#         cookies=driver.get_cookies()
#         cookies_1 = json.load(cookies)
#         print(cookies_1)
#
# if __name__ == '__main__':
#     getCookies.cookies()
#
#
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import configparser

# 打开并跳转百度页面
class GetCookies():
    def get_cookies(self,cook):
        self.cook = cook
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable_gpu')
        driver = webdriver.Chrome(options=chrome_options)
        login_url = 'https://login.soundai.com/login?redirect_url=https%3A%2F%2Fazero.soundai.com%2Findex&request_type=userLogin'
        driver.get(login_url)
        # 这里通过查找元素实现搜索
        driver.find_element_by_xpath('//*[@id="pane-userLogin"]/form/div[1]/div/div[1]/input').send_keys('17853487243')
        driver.find_element_by_xpath('//*[@id="pane-userLogin"]/form/div[2]/div/div/input').send_keys('chi902600')
        driver.find_element_by_xpath('//*[@id="pane-userLogin"]/form/div[3]/div/button').click()
        # driver.implicitly_wait(3)
        time.sleep(2)
        driver.get('https://azero.soundai.com/ask/own-skills')
        # 获取所有 cookie
        cookies = driver.get_cookies()
        # print(cookies)
        cookies_1 = cookies[0].get('value')
        print(cookies_1)

str = GetCookies()
str.get_cookies()
# if __name__ == '__main__':
#     GetCookies.get_cookies()
