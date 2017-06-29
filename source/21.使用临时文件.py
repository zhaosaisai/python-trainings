#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    临时文件不用命名，而且在关闭后会被自动删除
'''
'''
    使用标准库tempfile操作临时文件
    TemporaryFile, NamedTemporaryFile都是创建一个临时文件
    NamedTemporaryFile:创建一个命名的临时文件
'''
from tempfile import TemporaryFile, NamedTemporaryFile

# 创建一个临时文件
f = TemporaryFile()
# 向临时文件写入内容
f.write('abcdef' * 10000)
# 将文件指针指向最前面
f.seek(0)
# 读取临时文件中的内容
f.read(100)

# 创建一个命名的临时文件
ntf = NamedTemporaryFile() # 文件关闭后删除
print ntf.name # 临时文件在系统中的路径

ntf = NamedTemporaryFile(delete=False) # 文件关闭后不会自动删除
