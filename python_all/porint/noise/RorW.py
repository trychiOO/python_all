# -*- coding:utf8 -*-

readDir = r"C:\Users\龙龙.LAPTOP-54PEQUTO\Desktop\test\1.txt"
writeDir = r"C:\Users\龙龙.LAPTOP-54PEQUTO\Desktop\test\11.txt"
outfile = open(writeDir, "w", encoding='utf8')
data = []
# for line in  open(readDir,'r',encoding='utf8'):
#     outfile.write(line)
#
#     data.append(line)
#    # print(data)
#
# outfile.close()

with open(readDir, 'r', encoding='utf8') as f:
    line = f.readlines()
    data.append(line)
def paixu(a):
    count = len(a) - 1
    for i in range(count, 0, -1):
        for j in range(i):
            if a[j][0] > a[j + 1][0]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a



l =[]
l =paixu(data)


for j in l:
    outfile.write(str(j))




