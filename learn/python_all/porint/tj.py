# -*- coding:utf-8 -*-
import  csv
#读取文件   xiaohua.csv
filename = r'E:\xiaohua.csv'
s= 0
with open(filename) as f:
    reader = csv.reader(f)
    reader_row = next(reader)
    higths = []
    for row in reader:
        higths.append(row)
    #print(higths)

    Z = higths[0]
    K = higths[1]
    M = higths[2]
    print(Z)
    print(K)
    for z in Z:
        #print(z)
        for k in K:
            for m in M :
                l = str(z) + str(k)+str(m)
                s+= 1
                print(l)



print(s)


