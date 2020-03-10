from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
# 打开浏览器和网页
dr=webdriver.Chrome()     #PhtantomsJS  无头
dr.get('http://top.baidu.com/')

#进行 xpath 整合
re_dict=[]
for i in range(10):
    xpath='//*[@id="hot-list"]/li['+str(i+1)+']/a[1]'
    res = dr.find_element_by_xpath(xpath).get_attribute('title')
    # print(res)
    re_dict.append(res)

value = re_dict[0]
url='https://www.toutiao.com/search/?keyword=%s' %value
dr.get(url)
time.sleep(6)
#XPath ='//*[@id="J_section_0"]/div/div/div[1]/div'
XPath ='//*[@id="J_section_0"]/div/div/div[1]/div/div[1]/a/span'
try:
    WebDriverWait(dr, 20, 0.5).until(EC.presence_of_element_located((By.XPATH,XPath)))
finally:
    dr.find_element_by_xpath(XPath).click()
time.sleep(60)
#dr.quit()

    #print(dr.find_element_by_xpath(xpath).get_attribute('title'))
def getinfo():
    id_ = dr.find_element_by_xpath()
    content_ = dr.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/div[2]/div')
    titile_ = dr.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/h1')
