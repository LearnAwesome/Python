# 列表生成式 list comprehensions
'''
* 用[处理器 循环体 过滤器]的表达式来快速生成list
'''
print( [i * i for i in range(1, 11)] ) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print( [i * i for i in range(1, 11) if i % 2 == 0] ) # [4, 16, 36, 64, 100]

''' 可以用多个循环体，之间是嵌套关系 '''
print( [a + b for a in 'abc' for b in 'xyz'] ) # ['ax', 'ay', 'az', 'bx', 'by', 'bz', 'cx', 'cy', 'cz']
print( [a + b for a in 'abc' if a == 'a' for b in 'xyz'] ) # ['ax', 'ay', 'az']

''' 用os@listdir()来组合列表生成式，快速获得目录 '''
import os
print([d[:1] for d in os.listdir('./io')]) # ['a', 'b']