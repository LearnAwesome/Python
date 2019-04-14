# 迭代器 Iterator
'''
* 凡是可以用for in来迭代的都称为，可迭代类型Iterable
* 凡是可以用next()来调用的都称为，迭代器Iterator，属于惰性计算序列
* 集合数据类型range / list / tuple / str等属于Iterable，生成器generator对象属于Iterator。所以Iterator属于Iterable
* Iterable可以用built-in@iter()来转化成Iterator
'''

from collections import Iterator, Iterable
print( isinstance('ABC', Iterable) ) # True
print( isinstance('ABC', Iterator) ) # False
print( isinstance(iter('ABC'), Iterator) ) # True

iter_s = iter('ABC')
# print( next(iter_s) ) # 'A'
# print( next(iter_s) ) # 'B'
# print( next(iter_s) ) # 'C'
# print( next(iter_s) ) # 'StopIteration'
while True:
    try:
        print( next(iter_s) ) # 'A' 'B' 'C'
    except StopIteration:
        print( 'StopIteration' ) # 'StopIteration'
        break