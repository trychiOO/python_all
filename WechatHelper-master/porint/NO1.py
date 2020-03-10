from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
#driver.get("https://dueros.baidu.com/didp/main/index")
driver.get("http://www.baidu.com")
driver.find_elements_by_id("kw").send_keys('hello')
time.sleep(3)
#后退
size = driver.find_element_by_id("kw").size
print(size)
text = driver.find_element_by_id("cp").text
print(text)
driver.back()
#前进：
driver.forward()
#刷新
driver.refresh()
driver.send_keys(Keys.F1)
#截图
#driver.save_screenshot("filename")
#鼠标下拉
#ac=driver.find_element_by_xpath("//ul[@infinite-scroll-disabled]/li[last()]")
#退出
# driver.quit()
# driver.close()