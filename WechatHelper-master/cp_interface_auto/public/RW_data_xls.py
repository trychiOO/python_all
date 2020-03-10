# --*-- conding: utf8 -*-
import xlrd
#
#
# def read_excel():
#     # 打开文件
#     workbook = xlrd.open_workbook(r'C:\Users\龙龙.LAPTOP-54PEQUTO\Desktop\1.xlsx')
# #     print(d.sheet_names()))
#     # 获取所有sheet
#     print(workbook.sheet_names())  # [u'sheet1', u'sheet2']
#
#     # 根据sheet索引或者名称获取sheet内容
#     sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始
#
#     # sheet的名称，行数，列数
#     print(sheet1.name, sheet1.nrows, sheet1.ncols)
#
#     # 获取整行和整列的值（数组）
#     rows = sheet1.row_values(3)  # 获取第四行内容
#     cols = sheet1.col_values(2)  # 获取第三列内容
#     print(rows)
#     print(cols)
#
#     # 获取单元格内容
#     print(sheet1.cell(1, 0).value.encode('utf-8'))
#     print(sheet1.cell_value(1, 0).encode('utf-8'))
#     print(sheet1.row(1)[0].value.encode('utf-8'))
#
#     # 获取单元格内容的数据类型
#     print(sheet1.cell(1, 0).ctype)

#
# if __name__ == '__main__':
#     read_excel()
#
import xlrd
import xlwt

def get_xlsdata(file_nmae):
    d = xlrd.open_workbook(file_nmae)
    #打印出sheetName
    print(d.sheet_names())
    #根据sheet索引或者名称获取sheet内容
    # sheet_data = d.sheet_by_name('Sheet1')
    sheet_data = d.sheet_by_index(0)
    #sheet的名称，行数，列数
    print(sheet_data.name,sheet_data.nrows,sheet_data.ncols)
    # 获取整行和整列的值（数组）
    rows_data = sheet_data.row_values(2,-1)
    print(rows_data)
    cols_data = sheet_data.row_values(1,2,4)
    print(cols_data)
    #获取第四行内容


book = xlwt.Workbook('encoding = utf-8')

# 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
sheet = book.add_sheet('test01', cell_overwrite_ok=True)
# 其中的test是这张表的名字,cell_overwrite_ok，表示是否可以覆盖单元格，其实是Worksheet实例化的一个参数，默认值是False

# 向表test中添加数据
sheet.write(0, 0, '各省市')  # 其中的'0-行, 0-列'指定表中的单元，'各省市'是向该单元写入的内容
sheet.write(0, 1, '工资性收入')

# 也可以这样添加数据
txt1 = '北京市'
sheet.write(1, 0, txt1)
txt2 = 5047.4
sheet.write(1, 1, txt2)

# 添加第二个表
sheet2 = book.add_sheet("test02", cell_overwrite_ok=True)

Province = ['北京市', '天津市', '河北省', '山西省', '内蒙古自治区', '辽宁省',
            '吉林省', '黑龙江省', '上海市', '江苏省', '浙江省', '安徽省', '福建省',
            '江西省', '山东省', '河南省', '湖北省', '湖南省', '广东省', '广西壮族自治区',
            '海南省', '重庆市', '四川省', '贵州省', '云南省', '西藏自治区', '陕西省', '甘肃省',
            '青海省', '宁夏回族自治区', '新疆维吾尔自治区']

Income = ['5047.4', '3247.9', '1514.7', '1374.3', '590.7', '1499.5', '605.1', '654.9',
          '6686.0', '3104.8', '3575.1', '1184.1', '1855.5', '1441.3', '1671.5', '1022.7',
          '1199.2', '1449.6', '2906.2', '972.3', '555.7', '1309.9', '1219.5', '715.5', '441.8',
          '568.4', '848.3', '637.4', '653.3', '823.1', '254.1']

Project = ['各省市', '工资性收入', '家庭经营纯收入', '财产性收入', '转移性收入', '食品', '衣着',
           '居住', '家庭设备及服务', '交通和通讯', '文教、娱乐用品及服务', '医疗保健', '其他商品及服务']

# 填入第一列
for i in range(0, len(Province)):
    sheet2.write(i + 1, 0, Province[i])

# 填入第二列
for i in range(0, len(Income)):
    sheet2.write(i + 1, 1, Income[i])

# 填入第一行
for i in range(0, len(Project)):
    sheet2.write(0, i, Project[i])

# 最后，将以上操作保存到指定的Excel文件中
book.save("12.xls")

if __name__ == '__main__':
    get_xlsdata(r'C:\Users\龙龙.LAPTOP-54PEQUTO\Desktop\1.xlsx')

