#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 迭代iteration
'''
* python中的迭代用for in，适用于一切可以迭代的对象，基本包括str/range/list/tuple/dict/set等
* 可以用bulit-in@enumerate()来创造一个类似Java/Javascript的可枚举对象
'''

''' 迭代list '''
l = { 'a': 0, 'b': 1 }
for key in l: # 普通key迭代
    print(key) # 'a' -> 'b'
for value in l.values(): # value迭代
    print(value) # 0 -> 1
for key, value in l.items(): # key-value迭代
    print(key, value) # 'a' 0 -> 'b' 1

'''通过built-in@enumerate()来创造可枚举对象 '''
for i, value in enumerate(['a', 'b']):
    print(i, value) # 0 'a' -> 1 'b'
for i, key in enumerate(l):
    print(i, key) # 0 'a' -> 1 'b'

''' 枚举二维iteration '''
for a, b in ([1, 2], [3, 4]):
    print(a, b) # 1 2 -> 3 4

''' 通过collections*Iterable模块和bulit-in@isinstance()来判断是否为可迭代对象 '''
from collections import Iterable
print(isinstance('ABC', Iterable)) # True
print(isinstance([], Iterable)) # True
print(isinstance((), Iterable)) # True
print(isinstance({}, Iterable)) # True
print(isinstance(range(0), Iterable)) # True