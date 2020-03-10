from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from bs4 import BeautifulSoup
import time

print('\n\n-----\n')


def action():
    username = input('请输入学号： ')
    passwd = input('请输入密码： ')
    course_name = input('请输入课程名称或课程班号(注意是班号不是编号)： ')

    def findId(id_):
        '''通过id寻找元素'''
        nonlocal driver
        dr = driver.find_element_by_id(id_)
        return dr

    url = 'http:///'
    driver = webdriver.Chrome()
    driver.set_window_size(1200, 350)
    driver.get(url)
    while True:
        try:
            # 写入登陆信息并登陆
            driver.get(url)
            name_field = findId("txtYHBS")
            name_field.send_keys(username)
            passwd_field = findId("txtYHMM")
            passwd_field.clear()
            passwd_field.send_keys(passwd)
            code_field = findId("txtFJM")
            v_code = input('\n请输入验证码： ')
            code_field.send_keys(v_code)
            login_button = findId("btnLogin")
            login_button.click()
            # 选择课程
            url2 = 'http://****.****.edu.cn/Secure/PaiKeXuanKe/wfrm_Xk_ReadMeCn.aspx'
            driver.get(url2)
        except UnexpectedAlertPresentException:
            print('验证码输入错误，请重新输入')
            al = driver.switch_to.alert
            al.accept()
        else:
            break
    yes_button = findId("btnYes")
    time.sleep(0.5)
    yes_button.click()
    kklb = findId("btnKkLb")
    time.sleep(0.5)
    kklb.click()
    kcfw = findId("dlstSsfw")
    kcfw.find_element_by_xpath('//option[@value="通识教育选修课"]').click()
    if course_name.isdigit():
        kcmc = findId("txtPkbh")  # 排课班号
    else:
        kcmc = findId("txtKcmc")  # 课程名称
    kcmc.send_keys(course_name)
    search_button = driver.find_element_by_id("btnSearch")
    search_button.click()

    print('\n正在抢课，请耐心等待…………………………\n\n' + '=' * 40 + '\n')

    j = 1
    error = 1
    while True:
        print('\n%s,正在尝试第%d次刷新………………' % (name, j))
        try:
            html = driver.page_source
            soup = BeautifulSoup(html, 'lxml')
            tem_list = [each for each in soup.find('tr', class_="DGItemStyle").children]
            total = tem_list[11].string
            avaliable = tem_list[12].string

            if total > avaliable:
                js = "javascript:__doPostBack('dgrdPk$ctl02$ctl00','')"
                select = driver.execute_script(js)
                time.sleep(0.1)
                confirm_button = driver.find_element_by_name('btnQr')
                confirm_button.click()
                print('\n\n缘分已到！（选课成功）')
                break
            else:
                time.sleep(1)
                refresh_button = findId("btnNewRefresh")
                refresh_button.click()

        except UnexpectedAlertPresentException:
            al = driver.switch_to.alert
            al.accept()
            ##            print('出错啦！（%d）别担心，正在恢复……' % error)
            error += 1
            time.sleep(0.5)
            driver.refresh()
        j += 1


action()

input('\n\n按ENTER键退出')