#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    实例：给.sh和.py结尾的文件加上可执行权限
'''
import os, stat

# 遍历目录
[name for name in os.listdir('.') if name.endsWith(('.py', '.sh'))]
# 转换权限
for file in name:
    os.chmod(file, os.stat(file).st_mode | stat.S_IXUSR)