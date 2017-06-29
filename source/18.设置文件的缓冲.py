#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    文件缓冲就是将文件的内容写入到硬件设备的时候，使用系统调用，这类I/O操作时间很长
    为了减少I/O操作的次数，文件通常使用缓冲区

    分为全缓冲，行缓冲，无缓冲
'''
'''
    python中文件的缓冲区的大小是4096，只有写入的内容达到4096时，才会真正的向文件中写入
    (缓冲区的大小时和平台以及块设备相关的)
'''
'''
    python设置缓冲区的大小
        全缓冲：open函数的buffering设置为大于1的正整数，这个整数就是缓冲区的大小
        行缓冲：buffering的值设置为1
        无缓冲：buffering的值设置为0
'''
f = open('../demo.txt', 'w+')
f.write('abc') # 文件不会写入的
f.close()

f = open('../demo2.txt', 'w', buffering=2048)
f.write('+' * 1024)
f.close()

'''
    测试mac环境下缓冲不起作用，只有在控制台中起作用
'''