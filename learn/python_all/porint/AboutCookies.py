from selenium import webdriver
import keyword
import time
import json
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
cookies = driver.get_cookies()
cookie = driver.get_cookie("value")
print(cookies)
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')
driver.find_element_by_id("su").click()
print("==============")
print(cookie)
print("==============")
cookie1=driver.get_cookie("BAIDUID")
#print (json.load(cookie1))
#print(json.dump(cookie1))
time.sleep(3)
driver.quit()


