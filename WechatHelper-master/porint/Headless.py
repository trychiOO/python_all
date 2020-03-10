from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# 启动无头模式
chrome_options.add_argument('--headless')
#防止bug
chrome_options.add_argument('--disable_gpu')
#初始化
driver= webdriver.Chrome(options=chrome_options)

driver.get("http://www.baidu.com")
title_ = driver.title
#unkenow = driver.
print(title_)
cookies = driver.get_cookies()
print(cookies)


