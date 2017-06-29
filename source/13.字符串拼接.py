#!/usr/bin/env python
#-*- coding:utf-8 -*-

name = 'pavoooo'
company = 'weidian'

job = name + company

str_list = ['pavoooo', 'in', 'the', 'weidian']
print ''.join(str_list)

# join方法所传递的list中，必须所有的值都是str
# 所以我们可以像下面这样使用
print ''.join((str(i) for i in str_list))