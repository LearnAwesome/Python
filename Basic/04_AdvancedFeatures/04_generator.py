# 生成器 generator
''' 使用类似列表生成式的方式，将[]更换为()，来快速创建generator '''
g1 = (n * n for n in range(1, 4))
print(g1) # <generator object <genexpr> at 0x1011aaa98>

''' 使用yield语句来创建generator函数 '''
def fib(max):
    n, a, b = 0, 0, 1
    while n <= max:
        yield b
        a, b = b, a + b
        n += 1
    return 'Done'

''' 使用next来执行调用generator '''
f1 = fib(4)
print( next(f1) ) # 1
print( next(f1) ) # 1
print( next(f1) ) # 2
print( next(f1) ) # 3
print( next(f1) ) # 5
# print( next(f1) ) # StopIteration: Done

''' 使用迭代来执行generator '''
f2 = fib(4)
for n in f2:
    print(n) # 1 1 2 3 5

''' 迭代执行generator时无法执行到return语句，改写成while循环 '''
f3 = fib(4)
while True:
    try:
        n = next(f3)
        print(n) # 1 1 2 3 5
    except StopIteration as e: # 捕获StopIteration错误
        print(e.value) # 'Done'
        break

''' 杨辉三角形实现 '''
def triangles():
    L = [1]
    while L:
        yield L
        L.insert(0, 0)
        L.append(0)
        L = [ L[i] + L[i + 1] for i in range( len(L) - 1 ) ]

n, t = 6, triangles()
while n > -1:
    print(next(t))
    n -= 1
'''
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1]
'''