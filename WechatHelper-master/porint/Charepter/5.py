# -*- coding:utf8 -*-
import xlrd
import xlwt


def get_data(*args):
    """
    打开文件
    三种方式获取 sheet 的数据
    :param file_name:
    :param sheet_name:
    :return:
    """
    data = xlrd.open_workbook("")
    # 通过索引
    # table = data.sheet_by_index()[0]
    table = data.sheets()[0]
    # 通过名称获取
    table = data.sheet_by_name("")
    # 获取郑整行，整列的数数值  返回 列表：
    table.row_values()
    table.col_values()
    # 获取行数和列数：
    table.nrows
    table.ncols
    # 获取单元格
    table.col_values(0, 0)
    table.row_values(0, 0, 0)


if __name__ == '__name__':


