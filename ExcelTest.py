#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 读取excel数据
# 小罗的需求，取第二行以下的数据，然后取每行前13列的数据
import xlrd, xlwt
from datetime import datetime
from xlutils.copy import copy

#data = xlrd.open_workbook('address.xls') # 打开xls文件
try:
    data = xlrd.open_workbook('database/incominginfo.xlsx') # 打开xls文件
except FileNotFoundError:
    print("找不到文件")
else:
    table = data.sheets()[0] # 打开第一张表
    nrows = table.nrows # 获取表的行数
    # for i in range(nrows): # 循环逐行打印
    #     if i == 0: # 跳过第一行
    #         continue
    #     print(table.row_values(i)[:13]) # 取前十三列
    # table.write(nrows+1, 1, "gggg")
    # table.save('database/incominginfo33.xlsx')

    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',num_format_str='#,##0.00')
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
    
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')
    
    ws.write(0, 0, 1234.56, style0)
    ws.write(1, 0, datetime.now(), style1)
    ws.write(2, 0, 1)
    ws.write(2, 1, 1)
    ws.write(2, 2, xlwt.Formula("A3+B3"))
    
    wb.save('example.xlsx')

