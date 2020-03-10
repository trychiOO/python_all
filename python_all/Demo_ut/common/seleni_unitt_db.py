# -*- coding:utf8 -*-
import unittest
from  selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--headless')

class baiduTest(unittest.TestCase):
    def  setUp(self):
        # self.driver.get('https:\\www.baidu.com')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.baseUrl='https:\\www.baidu.com'
        self.driver.implicitly_wait(6)

    def test_baidu(self):
        driver = self.driver
        driver.get(self.baseUrl)
        driver.find_elements_by_id('kw').clear()
        driver.find_element_by_id('kw').send_keys("unittest")
        driver.find_element_by_id('su').click()
        time.sleep(3)
        title=driver.title
        self.assertEqual(title, u"unittest_百度搜索")
    def tearDown(self):
        self.driver.quit()




