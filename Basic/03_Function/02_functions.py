# 用def来定义函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print( my_abs(-4) ) # 4

# 用pass来占位空函数或者空表达式，防止报错
def foo():
    pass
if True:
    pass

# 函数返回多个参数，实际上是返回了一个tuple，并且可以用解构形式分别获得
def getVec():
    return 1, 2
vec = getVec()
print(vec) # (1, 2)
x, y = getVec()
print(x, y) # 1 2

# 必要的时候，可以加入类型判断进行抛错处理
def testError(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    else:
        return x
# testError('a') # TypeError: bad operand type

# 引入bulit-in*math包，并使用其中的函数
import math
print(math.pi) # 3.141592653589793
print(math.sqrt(4)) # 2.0