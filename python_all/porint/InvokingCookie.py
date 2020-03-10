# COOKIE 调用

from selenium import webdriver
import time
import keyword
driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("nihao")
#driver.find_element_by_id("su").click()
driver.find_element_by_xpath(r'//*[@id="su"]').click()
time.sleep(3)
cookies = driver.get_cookie()
cookie = driver.get_cookie()
print(cookies)
driver.close()