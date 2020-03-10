from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import  time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.set_window_size(900,900)

Double_click=driver.find_element_by_xpath(r'//*[@id="u1"]/a[1]')
#鼠标双击  double_click()
time.sleep(2)
ActionChains(driver).double_click(Double_click).perform()
time.sleep(5)
Right_click = driver.find_element_by_xpath(r'//*[@id="s_btn_wr"]')
#右键点击 context_click
ActionChains(driver).context_click(Right_click).perform()
time.sleep(5)
#鼠标悬停   move_to_element()

Donot_move =driver.find_element_by_class_name("lavalamp-item")

ActionChains(driver).move_to_element(Donot_move).perform()

time.sleep(3)
driver.quit()



