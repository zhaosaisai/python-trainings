#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    可以使用csv模块，其中的reader和writer可以完成csv文件的读写
'''
from urllib import urlretrieve
import csv

# 下载一份csv文件
# urlretrieve('http://table.finance.yahoo.com/table.csv?s=000001.sz', 'pingan.csv')

# 读取csv文件
rf = open('./pingan.csv', 'rb') # 一定要以二进制的形式打开

reader = csv.reader(rf) #返回的是一个迭代器

# reader.next() 读取一行的内容－返回的结果是一个list

# 也可以这样读
for row in reader:
    print row

# 写入csv文件
wf = open('./pingan.csv', 'wb')
writer = csv.writer(wf)

writer.writerow(['............']) # 参数是一个列表

wf.flush() # 保存更新文件    

