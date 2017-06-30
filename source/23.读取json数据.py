#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    使用标准模块中的json模块。其中loads和dumps可以完成json的操作
'''
import json

l = [1,2,3,'abc',{'name': 'pavoooo', 'age': 24}]
#转换成json字符串
print json.dumps(l)
d = {
    'b': None,
    'a': 5,
    'c': 'abc'
}
print json.dumps(d)

# 也可以指定分隔符号
print json.dumps(l, separators=[',', ':'])
# 也可以对输出的键进行排序
print json.dumps(d, sort_keys=True)

# 将json字符串 转换成json对象
print json.loads(json.dumps(l))

'''
    还可以使用json.load和json.dump进行文件的操作

    (注意文件的打开方式)
'''
with open('package.json', 'wb') as f:
    # 将一个json对象dump到一个文件中
    json.dump(l, f)