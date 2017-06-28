#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 生成器函数(包含yield语句的函数)

class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def isPrimeNum(self, k):
        if k < 2:
            return True

        for i in xrange(2, k):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        # 把可迭代对象的这个方法实现成是一个生成器函数
        for i in xrange(self.start, self.end + 1):
            if self.isPrimeNum(i):
                yield i

for x in PrimeNumbers(1, 100):
    print x