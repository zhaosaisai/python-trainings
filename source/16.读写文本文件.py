#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    python2和python3中字符串的语义发生了变化
        py2         py3
        str   --->  bytes
        unicode  ---> str
    py2:写入文件前对unicode进行编码，读入文件后对二进制字符串进行解码
    py3:open函数指定t的文本格式，encoding指定编码格式        
'''
s = u'你好'
# print s.encode('utf8')
# print s.encode('gbk')
# print s.encode('utf8').decode('gbk') # 会乱码

# py2中的文本读写
f = open('py2.txt', 'w')
s = u'你好'
f.write(s.encode('utf8'))
f.close()
p = open('py2.txt', 'r').read()
print p
# py3中的文本读写
# s3 = b'abcdefg' # bytes
# s3 = 'abcdefg' # unicode