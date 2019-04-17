# 映射 map()
'''
* built-in@map(func, iterable)
* 返回Iterator
'''
from collections import Iterator
l = [1, 2, 3]
def square(x):
    return x * x
m = map(square, l)
print( m ) # <map object at 0x10f487e10>
print( isinstance(m, Iterator) ) # True
print( list(m) ) # [1, 4, 9]

# 收敛 reduce()
'''
* functools@reduce(func, Iterable)
'''
from functools import reduce
def sum(x, y):
    return x + y
res = reduce(sum, l)
print(res) # 6

''' 练习：使用map和reduce实现float(floatStr) '''
def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    pointIndex = s.index('.')
    intStr = s[:pointIndex]
    floatStr = s[pointIndex + 1:]
    decimals = 10 ** len(floatStr)
    def char2number(i):
        return DIGITS[i]
    def str2int(x, y):
        return x * 10 + y
    return reduce( str2int, map(char2number, intStr) ) + reduce( str2int, map(char2number, floatStr) ) / decimals

print('1234.56789') # 1234.56789