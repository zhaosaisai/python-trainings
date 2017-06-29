#!/usr/bin/env python
#-*- coding:utf-8 -*-
import re
import string
'''
    一：使用strip，lstrip，rstrip去除字符串两端的空白字符
'''
s1 = '      adc        '
print s1.strip()
print s1.lstrip()
print s1.rstrip()

s2 = '----abc++++'
print s2.strip('-+')

'''
    二：删除单个固定位置的方法，可以使用切片加拼接的方式
'''
s3 = 'abc:123'
print s3[:3]+s3[4:]

'''
    三：字符串的replace方法，或正则表达式的re.sub()删除任意位置的字符
'''
s4 = '\tabc\t123\txyz'
print s4.replace('\t', '')

s5 = '\tabc\t123\txyz\ropq'
re.sub('[\t\r]', '', s5)

'''
    四：使用字符串的translate方法
'''
s6 = 'abc12306def'
# 生成转换规则
rules = string.maketrans('abcxyz', 'xyzabc')
s6.translate(rules)
s7 = 'abc\tdefs\rad'
# 第二个参数是需要删除的字符
s7.translate(None, '\t\r')

# 注意，unicode的translate方法接受的参数是一个字典