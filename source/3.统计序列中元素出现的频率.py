#!/usr/bin/env python
#-*- coding:utf-8 -*-
from random import randint
from collections import Counter

# 创建一个随机序列
data = [randint(0,20) for _ in xrange(30)]


# 找出上个序列中元素出现最多的

'''
    一：创建一个dict
'''
d_value = dict.fromkeys(data, 0)
for x in data:
    d_value[x] += 1

print d_value

'''
    二：使用 collections.Counter对象
'''
d_value = Counter(data)
print d_value.most_common(3)