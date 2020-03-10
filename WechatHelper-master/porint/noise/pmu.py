#-*- coding: utf-8 -*-
from selenium.webdriver import ActionChains
from selenium import webdriver
import time
import threading
import requests
driver=webdriver.Chrome()
#driver.get("https://www.baidu.com/")
# driver.get("https://music.163.com/#/discover/toplist?id=19723756")
driver.get("https://www.csdn.net/")
# driver.get("file:///C:/Users/龙龙.LAPTOP-54PEQUTO/Desktop/Selenium%20自动化爬虫.pdf")
# js="document.documentElement.scrollTop=100000"
# driver.execute_script(js)
# ac = driver.find_elements_by_id("auto-id-Wvs6HBgmcbDCEQTT")
ac = driver.find_element_by_xpath(r'//*[@id="auto-id-OCHeUuqbrsNAXN2s"]/div[2]/div[1]/div[2]/div/div/div[2]')
#driver.find_element_by_id("su").click()
ActionChains(driver).move_to_element(ac).perform()

#设置长和宽
driver.set_window_size(1000,2600)
#最大化set
time.sleep(1)
driver.maximize_window()
#driver.execute_script(js)


time.sleep(5)
#driver.find_element_by_xpath('//*[@id="13744458621564836432599"]/td[2]/div/div/div/span/a/b')
#print(txt1)
time.sleep(2)
driver.close()




