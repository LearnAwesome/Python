# 闭包 closure
'''
* 闭包函数A内至少含有一个函数定义B，并且B函数内部需要使用到B函数外A函数内的一个变量(被抓变量)
* 如果返回函数B，则具有惰性属性，真正的结果需要执行函数B的时候才能得到
'''
def lazy_sum(*args):
    def _sum():
        n = 0
        for v in args:
            n += v
        return n
    return _sum

fn1 = lazy_sum(*(1, 2, 3))
print(fn1) # <function lazy_sum.<locals>._sum at 0x109380e18>
print(fn1()) # 6

''' !!!谨慎：被抓变量如果是循环变量或后续可能发生变化的变量，需要注意内部函数的写法 '''

''' 循环变量的陷阱 '''
def outerFn_loop_var1():
    fns = []
    for i in range(1, 3):
        def innerFn():
            return i * i # 被抓循环变量i
        fns.append(innerFn)
    return fns
fns1 = outerFn_loop_var1()
print(fns1[0](), fns1[1]()) # 4 4 # 没有得到期望值1 4，出现理解偏差。原因: 惰性，当执行内部函数innerFn时，循环已经结束，此时 i = 2
''' 循环变量陷阱, 修复写法: 包裹法 '''
def outerFn_loop_var2():
    fns = []
    for i in range(1, 3):
        def wrapper(i): # 再包裹一层
            def innerFn():
                return i * i
            return innerFn
        fns.append(wrapper(i)) # 将期望的被抓循环变量i传进去
    return fns
fns2 = outerFn_loop_var2()
print(fns2[0](), fns2[1]()) # 1, 4

''' 后续可能发生变化的变量陷阱 '''
ref1 = [1, 2]
def outerFn_ref_var1():
    def innerFn():
        return sum(ref1)
    return innerFn
doSum1 = outerFn_ref_var1()
print(doSum1()) # 3
doSum2 = outerFn_ref_var1()
ref1.append(1) # 后续发生变化
print(doSum2()) # 4 # 结果不一致，不易控制。原因: 两个被抓变量的指向相同
''' 后续可能发生变化的变量陷阱, 简单修复写法: 浅拷贝 '''
ref2 = [1, 2]
def outerFn_ref_var2():
    ref = ref2[:] # 浅拷贝
    def innerFn():
        return sum(ref) # 修改被抓变量
    return innerFn
doSum3 = outerFn_ref_var2()
print(doSum3()) # 3
doSum4 = outerFn_ref_var2()
ref2.append(1) # 后续发生变化
print(doSum4()) # 3
