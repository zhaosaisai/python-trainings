#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
'''
    一：使用os模块的stat、fstat、lstat获取文件状态
'''
print os.stat('../demo.txt')
print os.lstat('../demo.txt') # 不跟随符号链接文件
f = open('../demo.txt', 'r')
print f.fileno()
print os.fstat(f.fileno()) #参数是一个文件描述符号

s = os.stat('../demo.txt')

mode = s.st_mode # 文件的标志位

import stat # 用于解析文件的模块 
stat.S_ISDIR(mode) #判段是不是文件夹
stat.S_ISREG(mode) # 判断是不是一个普通文件

print mode & stat.S_IRUSR # 是否具有读权限
print mode & stat.S_IXUSR # 是否具有执行权限

print s.st_mtime # 修改时间
print s.st_atime # 访问时间

import time
time.localtime(s.st_ctime) # 获取节点状态变更时间转换成标准文件格式

print  s.st_size # 获取文件的大小


'''
    使用os.path模块下面的快捷函数
'''
print os.path.isdir('../demo.txt') # 判断是不是文件夹
print os.path.islink('..demo.txt') # 判断是不是符号链接
print os.path.isfile('../demo.txt') # 判断是不是普通文件
print os.path.getatime('../demo.txt') # 获取文件的访问时间
print os.path.getsize('../demo.txt') # 获取文件的大小