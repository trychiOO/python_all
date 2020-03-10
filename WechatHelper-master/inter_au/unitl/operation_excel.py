# coding : utf-8
import xlrd
from xlutils.copy import copy
import os


class OperationExcel:

    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../case/interface.xls'
            self.sheet_id = 0
        self.data = self.get_data()

    #   ��ȡsheets������
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables
    def get_lines(self):
        tables = self.data
        return tables.nrows

    #��ȡĳһ����Ԫ�������
    def get_cell_value(self,row,col):
        tables = self.data
        cell = tables.cell_value(row,col)
        return cell
    #д������
    def write_value(self,row,col,value):
        '''
        д�뵽excel����
        row,col,value
        '''
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

    #���ݶ�Ӧcase_id�ҵ���Ӧ�е�����
    def get_rows_data(self,case_id):
        row_num = self.get_row_num(case_id)
        self.get_row_values(row_num)

    #���ݶ�Ӧ��case_id�ҵ���Ӧ���к�
    def get_row_num(self,case_id):
        num = 0
        coldata = self.get_col_values()
        for data in coldata:
            if case_id in data:
                return num
            num+=1
        return num

    #�����кţ��ҵ����е�����
    def get_row_values(self,row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    # �����кţ��ҵ����е�����
    def get_col_values(self,col=None):
        if col != None:
            col_data = self.data.col_values(col)
        else:
            col_data = self.data.col_values(0)
        return col_data


if __name__ == '__main__':
    opexcel = OperationExcel()
    print(opexcel.get_lines())
    print(opexcel.get_cell_value(0,0))