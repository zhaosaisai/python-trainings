#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    使用第三方的库：xlrd和xlwt，这两个库分别用于excel文件的读和写
'''
import xlrd
import xlwt

book = xlrd.open_workbook('demo.xlsx')

# 获取这个excel中的所有的表
sheets = book.sheets()

# 获取一个表对象
sheet = book.sheet_by_index(0)
# 访问行数
print sheet.nrows
# 访问列数
print sheet.ncols
# 获取一个单元格的内容－－传入行，列的坐标即可
cell = sheet.cell(0, 0)
# 获取单元格内容类型
print cell.ctype
# 获取value 
print cell.value
# 获取一行－－传入行号
print sheet.row(1) # 返回一个列表，列表每个值都是一个cell对象
# 直接获取某一行的值
print sheet.row_values(1)
print sheet.row_values(1, 1) # 从第二列开始读取

'''
    写excel
'''
# 创建一个excel写对象
wbook = xlwt.Workbook()
# 添加一个表的名字
wsheet = wbook.add_sheet('sheet1')
# 添加单元格--行，列，值
wsheet.write(0, 0, 'pavoooo')
# 保存
wbook.save('pavoooo.xlsx')




