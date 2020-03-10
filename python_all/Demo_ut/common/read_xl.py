#-*- coding:utf8 -*-
import xlrd
import os
import configparser

proj_path = str(os.path.dirname(__file__).split('common')[0])
ex_path = proj_path +'testFile/case/teacherCase.xlsx'
#
ex_data = xlrd.open_workbook(ex_path)

#读取sheet_name 工作表

sheet_name = ex_data.sheet_by_name('login')
ex_sheet_data = sheet_name.cell_value(1,1) #获取某一行 某一列的值

#获取 某行的有效值。
nows = sheet_name.ncols
print(nows)





