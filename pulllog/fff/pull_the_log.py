#_*_ coding:utf-8 _*_
#author:yr


import os

import time

import shutil

seconds1 = int(input("请输入pull文件的时间："))
# 根据文件的大小和网速来确定时间             建议60s

seconds2 = int(input("请输入下次循环的间隔时间"))
                                            #建议3000s

number = int(input("请输入循环次数"))


path = str(input("请输入pull文件路径"))

len1 = int(len(path) + 1)


for i in range(number):

    # print("i:" + str(i) + ";number:" + str(number))

    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

    # print("now:" + now)

    os.chdir(r'E:\laqurizhi\rizhi')
     #切换到新的路径

    os.mkdir(now)

    path2 = r"C:\Users\龙龙.LAPTOP-54PEQUTO\Desktop\任你说日志\1米安静唤醒" + "\\" + now

    os.system(r"adb shell find %s  -name  *.log " % (path) + ">" + "a.txt")

    with open("a.txt", "r") as f:

        a = f.readlines()

        # print(a)

        a.pop()

        for i in a:

            # print("i:" + str(i) + "a:" + str(a))

            time.sleep(seconds2)

            os.system("adb pull %s " % (i))

            time.sleep(seconds1)


            # print("1")

            shutil.move(i[len1:].strip("\\r\n"), path2)

            #
            # print("2")

            time.sleep(120)

            # os.system("adb shell rm /data/wrapper/sai_config/sai_sdk_release.log ")

            # print("3")


            # print("4")

            os.system("adb shell reboot")

            time.sleep(420)

            # print("5")


print("日志打印完成")






