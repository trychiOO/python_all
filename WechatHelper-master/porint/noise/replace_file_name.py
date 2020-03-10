# -*- coding=UTF-8 -*-
#
# author:SueMagic  time:2019-01-01
import os
import re
import sys

fileList = os.listdir(r"C:\Users\龙龙.LAPTOP-54PEQUTO\Desktop\wpn")
# 输出此文件夹中包含的文件名称
print(str(fileList)[:])
# 得到进程当前工作目录
currentpath = os.getcwd()
# 将当前工作目录修改为待修改文件夹的位置
os.chdir(r"C:\Users\龙龙.LAPTOP-54PEQUTO\Desktop\wpn")
# 名称变量
num = 1
# 遍历文件夹中所有文件
for fileName in fileList:
    # 匹配文件名正则表达式
    pat = ".+\.(txt)"
    # 进行匹配
    pattern = re.findall(pat, fileName)
    # 文件重新命名
    os.rename(fileName, (str(num + 9) + '.' + pattern[0]))
    # 改变编号，继续下一项
    num = num + 1
print("***************************************")
# 改回程序运行前的工作目录
os.chdir(currentpath)
# 刷新
sys.stdin.flush()
# 输出修改后文件夹中包含的文件名称
print("修改后：" + str(os.listdir(r"C:\Users\龙龙.LAPTOP-54PEQUTO\Desktop\wpn"))[:])
