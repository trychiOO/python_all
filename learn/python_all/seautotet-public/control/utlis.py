import xlrd
import xlsxwriter
from pathlib import Path


# 获取excel内容的工具类 增加生成excel测试报告功能
class Excel:
    # 初始化方法
    def __init__(self, type, file_name):
        # 读取excel
        if type == 'r':
            # 打开文件
            self.workbook = xlrd.open_workbook(file_name)
            self.sheet_names = self.workbook.sheet_names()
            # 装载所有数据的list
            self.list_data = []
            # 将测试数据内调用的方法，改编成自定义里面的变量
            self.dict_data = {}
        # 写入excel
        elif type == 'w':
            self.workbook = xlsxwriter.Workbook(file_name)
        # 获取到所有的sheet_names,sheet1,sheet2获取到所有，获取到的是一个list

    def read(self):
        # 循环编辑
        for sheet_name in self.sheet_names:
            # 通过每个sheetname获取到每个页的内容
            sheet = self.workbook.sheet_by_name(sheet_name)
            # 获取总行数
            rosw = sheet.nrows
            # 根据总行数进行读取
            for i in range(0, rosw):
                rowvalues = sheet.row_values(i)
                # 讲每一行的内容添加进去
                self.list_data.append(rowvalues)
            #     去除大标题第一行进行切割处理
        # 将得到的excel数据返回进行处理
        return self.list_data

    def write(self, data, sheet_name):
        # 设置报告格式
        sheet = self.workbook.add_worksheet(sheet_name)
        # 每行的宽度
        sheet.set_column('A:Q', 15)

        cell_format = self.workbook.add_format({'bold': True})
        sheet.set_row(0, 20, cell_format)
        # 红色
        red = self.workbook.add_format({'bg_color': 'red', 'color': 'white'})
        # 绿色
        green = self.workbook.add_format(
            {'bg_color': 'green', 'color': 'white'})
        for i in range(len(data)):
            for j in range(len(data[i])):
                # 进行用例结果的背景颜色更改 不同状态的用例 不同颜色
                if str(data[i][j]) == 'Fail':
                    sheet.write(i, j, str(data[i][j]), red)
                elif str(data[i][j]) == 'Pass':
                    sheet.write(i, j, str(data[i][j]), green)
                else:
                    sheet.write(i, j, str(data[i][j]))

    def close(self):
        self.workbook.close()


# 判断当前目录是否存在
def mkdir(p):
    path = Path('control/' + p)
    # 如果文件不存在 则创建
    if not path.is_dir():
        path.mkdir()




#
# if __name__ == '__main__':
#     import re
#
#     # 上个接口里面的返回内容
#     last_content = {'^Authorization': 'token', 'head_img': '', 'nick_name': '自动化数据上传nickname',
#                     'real_name': 'real_name自动上传', 'birthday': '2019-29-22', 'email': 'zhangmeng@1911thu.com',
#                     'sex': '1', 'position': '1', 'province': '山东', '^city': '菏泽', '^area': 'area地区',
#                     'company_name': '公司名称'}
#     # 当前接口里面携带了需要替换的数据内容
#     this_content = {"任务名称": "^real_name", "name": "^province"}
#     print(acquire(last_content, this_content))
# print(present)
# print(keys)
#
#     # 提取制定字符开头的内容
#     pattern = re.compile(r"'\^([\s\S]+?)'")
#     # 获取需要从上个接口匹配数据的key，然后通过key来读取内容
#     keys = re.findall(pattern, str(this_content))
#     # 获取到keys之后去除数据里面的特殊符号
#     content = str(this_content).replace('^', '')
#     # 用来存储匹配出来内容的list，用来进行原值替换
#     original = []
#     # 循环遍历key通过key来获取到value的所有内容
#     for key in keys:
#         # 通过上一步的key来获取指定的内容
#         regex = r"'%s': '([\s\S]+?)'" % key
#         # 匹配出来是个list 然后进行替换数据
#
#         match_obj = re.findall(regex, content)
#         for m in match_obj:
#             original.append(m)
#
# print(original)
#
# for o in original:
#     # todo 获取到上个接口的内容，进行替换数据
#     print(content.replace(o, '%s我是替换的数据' % o))


# pattern = re.compile(r"'\^([\s\S]+?)'")
# # 获取需要从上个接口匹配数据的key，然后通过key来读取内容
# keys = re.findall(pattern, str(this_content))
# print(keys)
#  todo 1.需要替换的数据，^开头后面跟上个接口需要提取的key值进行提取
# todo 2.去上个接口吧匹配的数据提取出来，进行替换到下个接口里面

# 创建必备的文件夹
def creation_files():
    # 创建文件
    files = ('report', 'junit', 'book', 'file')
    for file in files:
        mkdir(file)
    txt_path = str(Path('control/book') / ('txt_final.txt'))
    txt = open(txt_path, 'w')
    txt.seek(0)
    txt.truncate()
    txt.close()
