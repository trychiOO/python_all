# -*- coding:utf-8 -*-
#! python2
import shutil
a=0
readDir = r"C:\Users\龙龙.LAPTOP-54PEQUTO\Desktop\123\2\3米5信噪比识别\2.txt"  #old
writeDir = r"C:\Users\龙龙.LAPTOP-54PEQUTO\Desktop\123\2\3米5信噪比识别\new.txt" #new
lines_seen = set()
outfile = open(writeDir, "w",encoding='utf8')
f = open(readDir, "r",encoding='utf8')
for line in f:
  if line not in lines_seen:
    a+=1
    outfile.write(line)
    lines_seen.add(line)
    print(a)
    print('\n')
outfile.close()
print("success")