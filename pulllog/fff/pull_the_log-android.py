#_*_ coding:utf-8 _*_
#author:yr


import os

import time

import shutil
import pyautogui

import subprocess

seconds1 = int(input("请输入pull文件的时间："))

seconds2 = int(input("请输入下次循环的间隔时间"))


number = int(input("请输入循环次数"))



for i in range(number):

    # print("i:" + str(i) + ";number:" + str(number))

    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

    # print("now:" + now)

    os.chdir(r'E:\laqurizhi\rizhi')
     #切换到新的路径

    os.mkdir(now)

    path2 = r"E:\laqurizhi\rizhi" + "\\" + now

    print("开始")

    os.system("adb root")
	 #使用root权限

    os.system("adb remount")
	  #添加读写权限

    # os.system("adb shell logcat  > /data/log1.txt")
    #
    # time.sleep(5)
    #
    # pyautogui.hotkey('ctrl', 'c')

    p1 = subprocess.Popen(r"adb shell logcat  > /data/log1.txt ")

    time.sleep(seconds2)

    p1.kill()

    os.system(r" adb pull /tmp/log1.txt  E:\laqurizhi\rizhi")

    time.sleep(seconds1)


    shutil.move(r"E:\laqurizhi\rizhi\log1.txt", path2)


    os.system("adb shell rm -f /data/log.txt")

    # time.sleep(540)
    time.sleep(4)
            # os.system("adb shell reboot")




print("日志打印完成")






