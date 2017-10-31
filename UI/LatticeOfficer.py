#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 读取excel数据
import xlrd

#data = xlrd.open_workbook('address.xls') # 打开xls文件
class LatticeOfficer():
    def __init__(self, area=''):
        self.area = area

    def getOfficerList(self):
        try:
            data = xlrd.open_workbook('database/officer.xlsx') # 打开xls文件
        except FileNotFoundError:
            print("找不到文件")
        else:
            table = data.sheets()[0] # 打开第一张表
            nrows = table.nrows # 获取表的行数
            # for i in range(nrows): # 循环逐行打印
            #     if i == 0: # 跳过第一行
            #         continue
            #     print(table.row_values(i)[:13]) # 取前十三列
            officerNames = []
            for i in range(nrows):
                if( table.row_values(i)[0] == self.area):
                    officerName = table.row_values(i)[1]
                    officerNames.append(officerName)
            return officerNames

    def getDetail(self, oname):
        try:
            data = xlrd.open_workbook('database/officer.xlsx') # 打开xls文件
        except FileNotFoundError:
            print("找不到文件")
        else:
            table = data.sheets()[0] # 打开第一张表
            nrows = table.nrows # 获取表的行数
            # for i in range(nrows): # 循环逐行打印
            #     if i == 0: # 跳过第一行
            #         continue
            #     print(table.row_values(i)[:13]) # 取前十三列
            officerDetail = []
            for i in range(nrows):
                if( table.row_values(i)[1] == oname):
                    oname = table.row_values(i)[1]
                    # otel1 = table.row_values(i)[2]
                    # otel2 = table.row_values(i)[3]
                    if (table.row_values(i)[2] != ''):
                        otel1 = str(int(table.row_values(i)[2]))
                    else:
                        otel1 = ''
                    if (table.row_values(i)[3] != ''):
                        otel2 = str(int(table.row_values(i)[3]))
                    else:
                        otel2 = ''
                    if (table.row_values(i)[4] != ''):
                        otel3 = str(int(table.row_values(i)[4]))
                    else:
                        otel3 = ''
            officerDetail = [
                oname, otel1, otel2, otel3
            ]

            return officerDetail