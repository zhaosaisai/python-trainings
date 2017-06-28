#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
    关键是实现反向迭代协议的__reversed__方法，它返回一个反向迭代器
'''

l = [1,2,3,4,5]

'''
    使用reversed函数得到列表的反向迭代器
'''
for x in reversed(l):
    print x

class FloatRange:
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step
    
    # 实现正向迭代器
    def __iter__(self):
        t = self.start
        while t < self.end:
            yield t
            t += self.step
    
    # 实现反向迭代器
    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step

# 正向迭代器测试
for x in FloatRange(1.0, 4.0, 0.5):
    print x

# 反向迭代器测试
for x in reversed(FloatRange(1.0, 4.0, 0.5)):
    print x