# 递归
''' 用递归的方式实现阶乘 '''
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

'''
* 因为每次执行函数则会生成一个栈帧，每次return的时候又减少一个栈帧
* 所以递归很容易导致栈溢出
* 使用尾递归来避免栈溢出，使得栈帧永远为一个
* 尾递归特点: return的时候必须只是递归函数的执行，不能是表达式
'''
def tail_fact(n):
    return tail_fact_iter(n, 1)

def tail_fact_iter(n, prod):
    if n == 1:
        return prod
    return tail_fact_iter(n - 1, n * prod)

print(tail_fact(3))

''' 用递归实现汉诺塔 '''
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)

move(4, 'A', 'B', 'C')
'''
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
'''