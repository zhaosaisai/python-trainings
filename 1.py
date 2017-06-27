#!/usr/bin/env python
#-*- coding:utf-8 -*-
from random import randint

'''
   一： 列表解析
'''

# 生成一个随机数 
list_data = [randint(-10, 10) for _ in xrange(10)]

'''
    列表解析一：使用filter函数
'''
print filter(lambda x: x >= 0, list_data)

'''
    列表解析二：使用列表解析与法（相比filter速度更快）
'''
print [i for i in list_data if i >= 0]

'''
    二：筛选字典
'''
# 创建一个随机字典
dict_data = {s:randint(60, 100) for s in xrange(1,21)}

'''
    字典解析
'''
# 过滤出分数大于80的同学
print {k: v for k, v in dict_data.iteritems() if v > 80}

'''
    三：集合解析
'''
set_data = set(list_data)

# 找出集合中的偶数
print {i for i in set_data if i % 2 == 0}