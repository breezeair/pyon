#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 读取excel数据
# 小罗的需求，取第二行以下的数据，然后取每行前13列的数据
import xlrd

#data = xlrd.open_workbook('address.xls') # 打开xls文件
try:
    data = xlrd.open_workbook('database/officer.xlsx') # 打开xls文件
except FileNotFoundError:
    print("找不到文件")
else:
    table = data.sheets()[0] # 打开第一张表
    nrows = table.nrows # 获取表的行数
    for i in range(nrows): # 循环逐行打印
        if i == 0: # 跳过第一行
            continue
        print(table.row_values(i)[:13]) # 取前十三列
