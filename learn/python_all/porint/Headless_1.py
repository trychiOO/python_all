from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.support.wait import WebDriverWait
import keyword
import time
#开启模式
chrome_options = Options()
chrome_options.add_argument('--headless')
#防止bug
chrome_options.add_argument('--disable_gpu')
#初始化
# driver = webdriver.Chrome(ptions= chrome_options)
driver= webdriver.Chrome(options=chrome_options)
driver.get("https://www.baidu.com")
driver.find_element_by_xpath('//*[@id="kw"]').send_keys("selenium")
driver.find_element_by_id('su').click()
driver.implicitly_wait(20)
driver.save_screenshot("1.png")
driver.find_element_by_id('9').click()
driver.implicitly_wait(30)
driver.save_screenshot('2.png')
print(driver.find_element_by_link_text('知道').get_attribute('href'))
driver.quit()


