#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    当需要创建大量实例的时候，可以定义类的__slots__属性，用它来声明实例属性名字列表
'''

# 先定义两个比较类
class Player1(object):
    def __init__(self, uid, name, status = 0, level = 1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level

class Player2(object):
    # 用来描述属性有哪些属性
    __slots__ = ['uid', 'name', 'status', 'level']
    def __init__(self, uid, name, status = 0, level = 1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level