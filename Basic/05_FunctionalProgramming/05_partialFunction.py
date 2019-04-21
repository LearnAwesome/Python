# 偏函数 Partial Function
'''
* 也叫局部函数，固定某些函数的参数，来局部实现函数功能
* 使用functools@partial简单实现
'''

''' 通过固定int的base参数，来实现int2偏函数 '''
''' 手动实现 '''
def int2_manual(n, base = 2):
    # if not isinstance(n, str):
    #     n = str(n)
    return int(n, base)
print( int2_manual('100') ) # 4
''' 通过functools@partial实现 '''
from functools import partial
int2_partial = partial(int, base = 2)
print( int2_partial('100') ) # 4

''' 偏函数参数规则
* 定义时，还可以传入一些可变参数*args以及关键词参数**kws，functools.partial(func, *args, **kws)
* 执行时，将传入的可变参数放到已存在的可变参数之后
* 执行时，将传入的关键词参数放到已存在的关键词参数之后(如果存在，则替换)
'''
def _add(*args, **kws):
    print(*args)
    print('-' * 10)
    for key, value in kws.items():
        print('%s : %s' % (key, value))

_partial = partial(_add, 3, k1 = 'a', k2 = 'b')
_partial(1, 2, k1 = 'replaced', k3 = 'c')
'''
3 1 2 # 将传入的可变参数放到已存在的可变参数之后
----------
k1 : replaced # 将传入的关键词参数放到已存在的关键词参数之后(如果存在，则替换)
k2 : b
k3 : c
'''