#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 读取excel数据
import xlrd

#data = xlrd.open_workbook('address.xls') # 打开xls文件
class Mainten():
    def __init__(self, number=''):
        self.number = number

    def getNameandAddress(self):
        try:
            data = xlrd.open_workbook('database/terminal.xlsx') # 打开xls文件
        except FileNotFoundError:
            print("找不到文件")
        else:
            table = data.sheets()[0] # 打开第一张表
            nrows = table.nrows # 获取表的行数
            # for i in range(nrows): # 循环逐行打印
            #     if i == 0: # 跳过第一行
            #         continue
            #     print(table.row_values(i)[:13]) # 取前十三列
            nameAndAddress = []
            for i in range(nrows):
                if( table.row_values(i)[1] == self.number):
                    name = table.row_values(i)[8]
                    address = table.row_values(i)[4]
                    nameAndAddress = [name, address]
            return nameAndAddress

    def getTelNum(self, oname):
        try:
            data = xlrd.open_workbook('database/officer.xlsx') # 打开xls文件
        except FileNotFoundError:
            print("找不到文件")
        else:
            table = data.sheets()[0] # 打开第一张表
            nrows = table.nrows # 获取表的行数
            telNum = ''
            for i in range(nrows):
                if( table.row_values(i)[1] == oname):
                    if (table.row_values(i)[3] != ''):
                        telNum = str(int(table.row_values(i)[3]))
                    else:
                        telNum = ''

            return telNum

# m = Mainten('3201051932101')
# print(m.getNameandAddress())
# s = m.getNameandAddress()
# g = s[0]
# print(m.getTelNum(g))