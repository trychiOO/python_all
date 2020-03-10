# -*- coding: utf8 -*-
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import io
#设置无头模式
chrome_options = Options()
chrome_options.add_argument("--headless")
# 防止bug
chrome_options.add_argument("--disable_gpu")
class yd(unittest.TestCase):
    def setUp(self):
        self.driver =webdriver.Chrome(options=chrome_options)
        self.baseurl= 'http://fanyi.youdao.com/'
        self.driver.implicitly_wait(3)
    def test_yd(self):
        driver=self.driver
        driver.get(self.baseurl)
        driver.find_element_by_id('inputOriginal').clear()
        driver.find_element_by_id('inputOriginal').send_keys(u"你好")
        #driver.find_element_by_id().click()
        driver.find_element_by_class_name('fanyi__input__bg').click()
        time.sleep(3)
        page_source=driver.page_source
        self.assertIn( "hello",page_source)

    def tearDown(self):
       # time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


#inputOriginal


