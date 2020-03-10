
#_*_ coding:utf-8 _*_
#author:yr
with open (r"C:\Users\龙龙.LAPTOP-54PEQUTO\Desktop\任你说日志\识别\1m 5信噪比识别\wake.txt","r",encoding="utf-8") as f:
    lines= f.readlines()
    for i in lines:
        i = i.split("\t")[3].strip("\n")
        print(i)
#

