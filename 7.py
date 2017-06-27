#!/usr/bin/env python
#-*- coding:utf-8 -*-
from collections import OrderedDict

# 创建一个字典
d = OrderedDict()
d['Jim'] = (1, 35)
d['Leo'] = (2, 39)
d['Bob'] = (3, 46)

for k in d:
    print k # Jim  Leo  Bob