#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    可以使用标准库中的xml.etree.ElementTree。其中的parse函数可以进行xml解析
'''
from xml.etree.ElementTree import parse

# 打开xml文件
f = open('../demo.xml', 'r')
#解析xml文档
et = parse(f)
# 获取根节点
root = et.getroot()
# 跟节点的标签名
print root.tag
# 根节点的属性
print root.attrib
# 跟节点的内容
print root.text

# 遍历节点
for child in root:
    print child.get('name') # 获取一个属性 

# 也可以使用元素查找方法
print root.find('body')
print root.findall()

# 包含所有元素节点的迭代器
print root.iter()

'''
    更详细的可以参考python文档
'''