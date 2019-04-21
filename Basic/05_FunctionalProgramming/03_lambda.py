# 拉姆达表达式(匿名函数) lambda
'''
* 属于python内置的关键字，用于快速构建一个有返回值的匿名函数
* 多用于map, reduce, filter, sorted等需要传入一个处理函数的方法
'''

def prod(x, y):
    return x * y # 等价于prod = lambda x, y: x * y