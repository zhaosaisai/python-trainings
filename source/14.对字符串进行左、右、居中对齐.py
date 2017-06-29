#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    使用字符串的str.ljust(),str.rjust(),str.center()
'''
s = 'abc'
print s.ljust(20)
print s.ljust(20, '=')
print s.rjust(20)
print s.center(20)

'''
    使用format方法
'''
print format(s, '<20')
print format(s, '>20')
print format(s, '^20')