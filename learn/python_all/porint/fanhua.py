# -*- coding:utf-8 -*-
import  csv
#读取文件   xiaohua.csv
filename = r'E:\xiaohua.csv'
for z in range(3):
    print()
print(z)
with open(filename) as f:
    reader = csv.reader(f)
    higths = []
    for j in reader:
        header_row = next(reader)
        higths.append(header_row)

        #for i in range(6):
    # print(higths)
    # #lzxcvb

    l = str(higths[z][0][0])+str(higths[1][0][0])
    print(l)
    print(higths[0][0][0])

















    #print(len(header_row))
    #print(type(header_row))
    # higths = []
    # for i in reader:
    #     higths.append(i)
    # print(higths)



#获取地址

#读取每一列

#每一列的长度

#for循环

#选择需要的列数

#进行循环

