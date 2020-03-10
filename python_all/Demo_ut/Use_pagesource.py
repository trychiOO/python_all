# coding:utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
# chrome_options = Options()
# chrome_options.Options.add_argument("--headless")
# chrome_options.Options.add_argument("--disable_gpu")

chrome_options = Options()
chrome_options.add_argument("--headless")
# 防止bug
chrome_options.add_argument("--disable_gpu")
class JianDan():
    def __init__(self):
        self.driver =webdriver.Chrome(options=chrome_options)
        self.driver.get("http://jandan.net/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def get_page_title(self):
        self.page = self.driver.page_source
        # 非贪婪匹配，匹配所有满足'target="_blank">....</a></h2>'格式的信息，结果显示是一个列表
        self.titles = re.findall(r'target="_blank">(.*?)</a></h2>', self.page)
        for title in self.titles:
            print(title)
if __name__ == '__main__':
    jian_dan = JianDan()
    jian_dan.get_page_title()