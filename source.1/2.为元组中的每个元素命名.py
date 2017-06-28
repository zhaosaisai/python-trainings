#!/usr/bin/env python
#-*- coding:utf-8 -*-
from collections import namedtuple

# 一个元组元素
my_info = ('Pavoooo', 24, 'weidian', 'full-stack', 'pavoooo@163.com')

'''
    第一种：使用类似于枚举类型的方式
'''
NAME, AGE, COMPANY, JOB, EMAIL = xrange(len(my_info))
# 获取姓名
print my_info[NAME]
# 获取邮箱 
print my_info[EMAIL]

'''
    第二种：使用标准库collections.namedtuple 代替tuple
'''
my_info = namedtuple('my_info', ['name', 'age', 'company', 'job', 'email'])
info = my_info('Pavoooo', 24, 'weidian', 'full-stack', 'pavoooo@163.com')
# 访问姓名
print info.name
# 访问邮箱
print info.email

