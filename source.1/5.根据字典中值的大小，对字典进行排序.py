#!/usr/bin/env python
#-*- coding:utf-8 -*-
from random import randint

# 使用内置函数sorted
'''
    一：使用内置函数zip将字典转化成元组
'''
score = {x: randint(60, 100) for x in 'abcdefg'}

print sorted(zip(score.itervalues(), score.iterkeys()))

'''
     二：使用sorted函数结合key参数
'''
print sorted(score.items(), key=lambda x: x[1])