#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    使用正则表达式
'''
import re

print re.split('[,;|\t]+', 'ab,;fd,es\tjg,ds|ds')