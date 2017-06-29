#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    在访问二进制文件的时候，希望把文件映射到内存中，可以实现随机访问

    如果多个进程映射同一个文件，还能实现进程间通信
'''
'''
    使用mmap模块中的mmap()函数，接受一个文件描述符作为参数
'''
import os
import mmap

f = open('demo.bin', 'r+b')
# 获取文件描述符号
f_no = f.fileno()
# 文件映射
m = mmap.mmap(f_no, 0, access=mmap.ACCESS_WRITE)
print type(m)
print m[10:20] #切片操作
# 修改操作
m[4:8] = '\xff' * 4