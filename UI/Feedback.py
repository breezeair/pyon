#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 读取excel数据
import xlrd

#data = xlrd.open_workbook('address.xls') # 打开xls文件
class Feedback():
    def __init__(self):
         self.number = 'number'
         self.name = 'name'

    def getAddress(self, number):
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
            address = ''
            for i in range(nrows):
                if( table.row_values(i)[1] == number):
                    address = table.row_values(i)[4]
            #print("address:" + address)
            return address

    def getTelNum(self, name):
        try:
            data = xlrd.open_workbook('database/officer.xlsx') # 打开xls文件
        except FileNotFoundError:
            print("找不到文件")
        else:
            table = data.sheets()[0] # 打开第一张表
            nrows = table.nrows # 获取表的行数
            telNum = ''
            for i in range(nrows):
                if( table.row_values(i)[1] == name):
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