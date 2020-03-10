# -*- coding: utf:8 -*-
from common.cryptoMethod import Encryption
from common.readExcel import *
import configparser as cparser
from common.mysqlCfg import DB
from common.txt import *
import os

proj_path = str(os.path.dirname(__file__).split('common')[0])
proj_path = proj_path.replace('\\', '/')
excel_path = proj_path + 'testFile/case/teacherCase.xlsx'
# print(excel_path)
cfg_path = proj_path + 'config.ini'
print(cfg_path)
cf = cparser.ConfigParser()
cf.read(cfg_path)


def get_req_params(sheet, case):
    """
    获取请求参数
    :param sheet: sheet name
    :param case: 用例名
    :return:
    """






























'''
    
    req_len = 0
    param_key = row_value(excel_path, sheet, 'case_name')
    param_value = row_value(excel_path, sheet, case)
    # 获取request参数长度
    for i in range(len(param_key)):
        if param_key[i] == 'Response':
            req_len = i
            # print(i)
            break



def get_resp_params(sheet, case, resp_key):
    """
    获取响应参数
    :param resp_key: 响应名
    :param sheet: sheet name
    :param case: 用例名
    :return:
    """


'''
