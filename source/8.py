#!/usr/bin/env python
#-*- coding:utf-8 -*-
# 倒入实现可迭代对象的两个关键类
from collections import Iterable, Iterator
import requests
# 继承上面的类－－实现迭代器对象
class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0
    def getWeather(self, city):
        r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s: %s, %s' % (city, data['low'], data['high'])
    # 实现迭代器对象的next方法
    def next(self):
        # 当索引调用到最大索引的时候 再次调用next方法会抛出错误
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)

# 实现可迭代对象
class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities = cities
    
    # 实现可迭代接口
    def __iter__(self):
        return WeatherIterator(self.cities)

# test
weather = WeatherIterable(['北京'.decode('utf8'), '上海'.decode('utf8')])
for w in weather:
    print w.encode('utf8')