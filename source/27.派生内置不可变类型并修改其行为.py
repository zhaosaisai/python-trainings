#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    一个简单的需求：
        自定义一种新的类型的元组，对于传入的可迭代对象，只保留其中int类型并且值大于0的元素

    思路：
        定义一个类，继承内置的tuple，并实现__new__,修改实例化行为
'''
class IntTuple(tuple):
    def __new__(cls, iterable):
        # 这个方法会先于__init__方法调用。同时第一个参数就是这个类
        g = (x for x in iterable if isinstance(x, int) and x > 0)
        return super(IntTuple, cls).__new__(cls, g)
    def __init__(self, iterable):
        super(IntTuple, self).__init__(iterable)

t = IntTuple([1,2,0, -1, 'a'])
print t