#-*- coding: utf8 -*-
import  os
from xlrd import open_workbook
import getPath

#获取当前目录
basePath = getPath.get_basepath()
basePath1 = os.path.abspath('.')

print(basePath1)

#xlsPath = os.path.join(basepath,'test_file','case',xls_name)
xlsPath = os.path.join(basePath,'test_file','case','login.xls')
print(xlsPath)



