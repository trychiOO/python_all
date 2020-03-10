#coding:utf-8
import xlrd
"""读取文件"""
import  time
# 打开文件
read_f = xlrd.open_workbook("D:\PycharmProjects\WechatHelper-master\selenium_demo\D2\query.xlsx")
# print(read_f.sheet_names())

sheet = read_f.sheet_by_name
sheet = read_f.sheet_by_name('Sheet1')
col_datas = sheet.col_values(0,1)
print(col_datas)
print(type(col_datas))


print(str(time.time())[11:])

