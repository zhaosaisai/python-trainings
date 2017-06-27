#!/usr/bin/env python
#-*- coding:utf-8 -*-
import re
from collections import Counter
# 读取文件
txt_str = open('sentence.txt').read()
# 分隔字符串
txt_list = re.split('\W+', txt_str)
# 出现次数最高的前十的单词
print Counter(txt_list).most_common(10)
