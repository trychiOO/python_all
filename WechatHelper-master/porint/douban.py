# -*- coding: utf-8 -*-
# 导入库

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
#防止bug
chrome_options.add_argument('--disable_gpu')
#初始化
driver= webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
cookies = driver.get_cookies()
print(cookies)

# 打开浏览器和页面
# dr = webdriver.Chrome()
# # 输出当前页面地址
# dr.get("https://www.baidu.com/")
# dr.implicitly_wait(10)
# dr.find_element_by_xpath(r'//*[@id="s_xmancard_news"]/div/div[1]/ul/li[1]/span/span/a').get_attribute()
# print(dr.find_element_by_link_text('首页').get_attribute('href'))

# 退出

# 隐式等待
