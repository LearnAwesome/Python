# 排序 sorted()
''' built-in@sorted(Iterable, key, reverse = False) '''

print( sorted( (1, 2, 3, 2, 1) ) ) # [1, 1, 2, 2, 3]
print( sorted( (1, 2, 3, 2, 1), reverse = True ) ) # [3, 2, 2, 1, 1]

''' 使用key func来定义排序规则 '''
print( sorted( [1, -1, -3, 2, 0, 3], key = abs ) ) # [0, 1, -1, 2, -3, 3]
print( sorted( [1, -1, -3, 2, 0, 3], reverse = True ) ) # [3, 2, 1, 0, -1, -3]
print( sorted( [1, -1, -3, 2, 0, 3], key = lambda x: -x ) ) # [3, 2, 1, 0, -1, -3] # 巧妙的使用负数来实现反向排序
print( sorted( ['D', 'c', 'B', 'a'] ) ) # ['B', 'D', 'a', 'c'] # 默认使用ASCII编码大小来排序
print( sorted( ['D', 'c', 'B', 'a'], key = str.lower ) ) # ['a', 'B', 'c', 'D']

classmates = [
    { 'name': 'Michael', 'score': 99 },
    { 'name': 'Peter', 'score': 80 },
    { 'name': 'Marry', 'score': 91 }
]

print( sorted(classmates, key = lambda student: student['score']) ) # [{'name': 'Peter', 'score': 80}, {'name': 'Marry', 'score': 91}, {'name': 'Michael', 'score': 99}]