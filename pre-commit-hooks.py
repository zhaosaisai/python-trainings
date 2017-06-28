#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    这个文件是git的pre-commit的脚本文件:在文件commit之前对source中的文件重命名
'''
import os
import yaml

SOURCE_DIR = os.getcwd()+'/source'
TITLE_CONFIG = yaml.load(open('./title.yml'))['titles']

for file in os.listdir(SOURCE_DIR):
    file_list = file.split('.')
    file_name = file_list[0]
    file_ext = file_list[1]
    try:
        correct_file_name = TITLE_CONFIG[int(file_name) - 1]
        os.rename('%s/%s' % (SOURCE_DIR, file), '%s/%s.%s' % (SOURCE_DIR, correct_file_name, file_ext))
    except:
        continue

print 'auto change filename successfully'

# 命名结束之后中git命令
try:
    os.system('git add .')
except:
    exit('执行自动化git命令失败')