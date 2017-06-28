#!/usr/bin/env python
#-*- coding:utf-8 -*-
from random import randint, sample

data1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3,6))}
data2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3,6))}
data3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3,6))}

# 取上面三个字典中的公共键
'''
    一：循环遍历判断
'''
result = []
for x in data1:
    if x in data2 and x in data3:
        result.append(x)

'''
    二：利用set交集的操作
'''
# 得到字典的keys的集合(dict的数目固定)
print data1.viewkeys() & data2.viewkeys() & data3.viewkeys()
# 使用map函数，得到所有字典的集合(dict的数目不固定)
map_dict = map(dict.viewkeys, [data1, data2, data3])
# 使用reduce函数，取出所有字典的keys的交集的集合
print reduce(lambda a, b: a & b, map_dict)