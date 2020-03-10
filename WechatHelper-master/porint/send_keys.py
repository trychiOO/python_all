
# 导入库
from selenium import webdriver
# 键盘事件
from selenium.webdriver.common.keys import Keys

#鼠标事件
from selenium.webdriver.common.action_chains import ActionChains



import time

# 打开浏览器和打开百度
driver=webdriver.Chrome()
driver.get("https://www.baIDu.com/")

# 通过 ID 查找，然后输入，并点击
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id('kw').send_keys(Keys.ENTER)
time.sleep(5)

driver.quit()

# 退出浏览器 driver.quit()
