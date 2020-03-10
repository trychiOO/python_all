#coding:utf-8
from selenium import webdriver
import  os
import xlrd
import time
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.chrome.options import Options
chrome_options = Options()
# 启动无头模式
chrome_options.add_argument('--headless')
#防止bug
chrome_options.add_argument('--disable_gpu')
#初始化
driver= webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)
driver.maximize_window()
login_url = "https://login.soundai.com/login?redirect_url=https%3A%2F%2Fazero.soundai.com%2Findex&request_type=userLogin"
driver.get(login_url)
driver.find_element_by_xpath('//*[@id="pane-userLogin"]/form/div[1]/div/div[1]/input').send_keys("17853487243")
driver.find_element_by_xpath('//*[@id="pane-userLogin"]/form/div[2]/div/div/input').send_keys("123123chi123")
driver.find_element_by_xpath('//*[@id="pane-userLogin"]/form/div[3]/div/button').click()
time.sleep(2)
test_url= 'https://azero.soundai.com/ask/customize/simulation/5e5c891778663200082e811d'
driver.get(test_url)

read_f = xlrd.open_workbook("D:\PycharmProjects\WechatHelper-master\selenium_demo\D2\query.xlsx")
sheet = read_f.sheet_by_name
sheet = read_f.sheet_by_name('Sheet4')
col_datas = sheet.col_values(0,1)
for col_data in col_datas:
    driver.find_element_by_xpath('//*[@id="hasScreen"]/div/div[2]/textarea').send_keys(col_data)
    driver.find_element_by_xpath('//*[@id="hasScreen"]/div/div[2]/textarea').send_keys(Keys.ENTER)
    #截图
    time.sleep(3)
    name = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    driver.save_screenshot('D:\\PycharmProjects\\WechatHelper-master\\selenium_demo\\D1\\sheet4\\'+name+'.png')
    time.sleep(3)

