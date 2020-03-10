# -*- coding:utf8 -*-
import xlrd
from datetime import date, datetime

# 读取文件

# 打开文件  xlrd.opem_workbook('file.path.name')
readfile = xlrd.open_workbook(r"D:\file\1.xlsx")
# print(readfile.sheet_names())

# 读取 sheetname

sheet2_name = readfile.sheet_names()[1]
# print(sheet2_name)
#

sheet = readfile.sheet_by_name('第二个')
#读取整行和整列的内容
row_datas = sheet.row_values(1,2) #行在前 ，列在后
print(row_datas)
#col_datas = sheet.col_values(2,1)  #列在前 行在后




