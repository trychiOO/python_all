# -*-coding:utf8 -*-
import xlrd
import os
import  configparser as cparser
def cell_value(fp, sheet_name, row, col):
    """
    获取单元格的值
    :param fp:
    :param sheet_name:
    :param row:
    :param col:
    :return:
    """
    test_data = xlrd.open_workbook(fp)
    sheet_name = test_data.sheet_by_name(sheet_name)
    return sheet_name.cell_value(row-1, col-1)

def row_value(fp, sheet_name, case_name):
    """
    获取整行的值
    :param fp:
    :param sheet_name:
    :param case_name:
    :return:
    """
    test_data = xlrd.open_workbook(fp, 'br')
    sheet_name = test_data.sheet_by_name('%s' % sheet_name)
    cases = sheet_name.col_values(0)
    for case_i in range(len(cases)):
        if cases[case_i] == case_name:
            return sheet_name.row_values(case_i)


def col_value(fp, sheet_name, col):
    """
    获取整列的值
    :param fp:
    :param sheet_name:
    :param col:
    :return:
    """
    test_data = xlrd.open_workbook(fp)
    sheet_name = test_data.sheet_by_name('%s' % sheet_name)
    return sheet_name.col_values(col - 1)

proj_path = str(os.path.dirname(__file__).split('common')[0])
proj_path = proj_path.replace('\\', '/')
excel_path = proj_path + 'testFile/case/teacherCase.xlsx'
cf = cparser.ConfigParser()



if __name__ == '__main__':
    req_len = 0
    param_key = row_value(excel_path, 'login', 'case_name')
    param_value = row_value(excel_path, 'login', 'case_name')
    # print(param_value )
    # 获取request参数长度
    for i in range(len(param_key)):
        if param_key[i] == 'Response':
            req_len = i
            # print(req_len)
            break
    params = dict()
    for key_i in range(1, req_len):
        if param_key[key_i] == 'city':
            params['account'] = (param_value[key_i])

        else:
            params[param_key[key_i]] = param_value[key_i]




