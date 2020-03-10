#-*- coding:utf8 -*-
import jieba
l = ['11','a',6,9]
m = ['10','b',3,8]


a = [l,m]

readDir= r"C:\Users\龙龙.LAPTOP-54PEQUTO\Desktop\test\11.txt"
writeDir= r"C:\Users\龙龙.LAPTOP-54PEQUTO\Desktop\test\11.txt"
outfile =  open(readDir,'w',encoding='utf8')
f = open(readDir,'r',encoding='utf8')
# a =list(f)



data = []
for line in open(readDir,"r"):
    data.append(line)






def paixu(a):

    count = len(a)-1

    for i in range(count, 0, -1):
        for j in range(i):
            if a[j][3] > a[j+1][3]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
k = paixu(a)
print(str(k))
lines = set()
for line in k:
    print(line)

outfile.write(str(lines))
outfile.close()
