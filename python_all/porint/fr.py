#-*- coding: utf-8 -*-
def TextDR(sourcepath,destpath):
    sum = 0
    sum_pre = 0
    addrs = set()
    with open(sourcepath, 'r',encoding='utf8') as scan_file:
        for line in scan_file.readlines():
            sum_pre += 1
            addrs.add(line)
    scan_file.close()
    with open(destpath, 'w',encoding='utf8') as infile:
        while len(addrs) > 0:
            sum += 1
            infile.write(addrs.pop())
    infile.close()
    #print(addrs)
    print("去重之前文本条数: "+str(sum_pre))
    print("去重之后文本条数: "+str(sum))
    return sum_pre,sum
#example
sourcepath = r'C:\Users\龙龙.LAPTOP-54PEQUTO\Desktop\新建文件夹\30wenben.txt'
destpath = r'C:\Users\龙龙.LAPTOP-54PEQUTO\Desktop\新建文件夹\txt.txt'
TextDR(sourcepath,destpath)