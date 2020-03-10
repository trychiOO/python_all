#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import xlrd
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
# driver.set_window_size(1800 ,1800)
driver.maximize_window()
url = "https://azero.soundai.com/"
driver.get(url)
# driver.set_window_size(700,900)
#后退
# time.sleep(2)
# driver.get(url+"account/login")
login_url = "https://login.soundai.com/login?redirect_url=https%3A%2F%2Fazero.soundai.com%2Findex&request_type=userLogin"
driver.get(login_url)
driver.find_element_by_xpath('//*[@id="pane-userLogin"]/form/div[1]/div/div[1]/input').send_keys("18126467246")
driver.find_element_by_xpath('//*[@id="pane-userLogin"]/form/div[2]/div/div/input').send_keys("0987654321")
driver.find_element_by_xpath('//*[@id="pane-userLogin"]/form/div[3]/div/button').click()
time.sleep(2)
# creat_url = 'https://azero.soundai.com/ask/category'
# driver.get(creat_url)
# time.sleep(2)
# driver.add_cookie({"name":"testname_1234567890"},{"value":"testvalue_1234567890"})
test_url= 'https://azero.soundai.com/ask/customize/simulation/5e5df82a35631e0009d58ce6'
driver.get(test_url)
read_f = xlrd.open_workbook("D:\PycharmProjects\WechatHelper-master\selenium_demo\D2\query.xlsx")
# print(read_f.sheet_names())
sheet = read_f.sheet_by_name
sheet = read_f.sheet_by_name('Sheet1')
col_datas = sheet.col_values(0,1)
for col_data in col_datas:
    driver.find_element_by_xpath('//*[@id="hasScreen"]/div/div[2]/textarea').send_keys(col_data)
    driver.find_element_by_xpath('//*[@id="hasScreen"]/div/div[2]/textarea').send_keys(Keys.ENTER)
    #截图
    time.sleep(3)
    name = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    driver.save_screenshot('D:\\PycharmProjects\\WechatHelper-master\\selenium_demo\\D2\\img\\sheet4\\'+name+'.png')
    time.sleep(3)

# driver.find_element_by_id("phone_number").send_keys("17853487243")
# # time.sleep(1)
# driver.find_element_by_id("login_password_close").send_keys("123123chi123")
# #前进
# # driver.forward()
# driver.find_element_by_id("login_btn").click()
# cookies = driver.get_cookies()
# cookie = driver.get_cookie("JSESSIONID")
# print(cookies)
# print(cookie)

#
# driver.get(url+"ask/own-skills")
# driver.find_element_by_id("create_skill").click()
# driver.find_element_by_id("dialogue_skill_name").send_keys("selenium_test")
# driver.find_element_by_id("dialogue_skill_submit").click()
# # driver.find_element_by_id("bs-select-1-0").click()
# driver.find_element_by_id("description").send_keys("test"+'\n'+"selenium")
# driver.find_element_by_id("save_basis").click()
# # driver.find_element_by_xpath("/html/body/div[1]/div[3]/a[1]").click()
#刷新
# driver.refresh()
#关闭
# driver.close()
# driver.quit()



