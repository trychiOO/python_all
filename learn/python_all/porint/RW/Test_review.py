# -*-coding:utf8 -*-
import xlrd

#读取文件
read_file = xlrd.open_workbook(r'D:\file\1.xlsx')

#读取文件的的sheetname

sheet_name1 =read_file.sheet_by_name('第二个')
# sheet_name1= read_file.sheet_by_index()

#读取行和列

# rows_data= sheet_name1.row_values(1,0)
# print(rows_data)
rows_data1= sheet_name1.row(1)
print(rows_data1)





#写入到xlsx

