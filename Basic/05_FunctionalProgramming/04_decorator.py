# 装饰器 decorator
'''
* 用于介入函数运行，改善函数运行环境，本质上也是一个函数
* 定义时，传入原函数，返回高阶函数
* 使用时，用@装饰器名字写在定义的函数前一行
'''

''' 不需要传入额外参数的装饰器(只默认传入原函数), 包裹一层 '''
''' !!!谨慎: 手动定义的装饰器函数需要进行__name__指向修正 '''
def log_noarg1(func):
    def wrapper(*arg, **kw):
        print('begin call:')
        return func(*arg, **kw)
    return wrapper
@log_noarg1
def getName1(person):
    return person['name']
fn1 = getName1
print( fn1({'name': 'Michael', 'age': 30}) ) # 相当于log_noarg1( wrapper( {'name': 'Michael', 'age': 30} ) )
print(fn1.__name__) # wrapper 指向装饰器函数内部的包裹函数wrapper
''' __name__指向修正 '''
import functools
def log_noarg2(func):
    # @functools.wraps(func) # 方式1: 通过@functools.wraps来修正
    def wrapper(*arg, **kw):
        print('begin call:')
        return func(*arg, **kw)
    wrapper.__name__ = func.__name__ # 方式2: 通过赋值方式简单修正
    return wrapper
@log_noarg2
def getName2(person):
    return person['name']
fn2 = getName2
print( fn2({'name': 'Michael', 'age': 30}) )
print(fn2.__name__) # getName2 指向装饰器函数内部的包裹函数wrapper

''' 需要传入额外参数的装饰器，包裹两层 '''
def log_args1(about):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*arg, **kw):
            print(about, 'begin call:')
            return func(*arg, **kw)
        return wrapper
    return decorator
@log_args1('Python')
def getName3(person):
    return person['name']
fn3 = getName3
print( fn3({'name': 'Michael', 'age': 30}) ) # log_args1('Python')( wrapper( {'name': 'Michael', 'age': 30} ) )
print(fn3.__name__) # getName3 指向装饰器函数内部的包裹函数wrapper

''' 练习: 传入额外参数，并且在原函数执行前后都进行操作的装饰器 '''
def log(about):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*arg, **kw):
            print(about, 'begin call')
            print('%s()' % func.__name__, 'is calling')
            res = func(*arg, **kw)
            print(about, 'end call')
            return res
        return wrapper
    return decorator
@log('Python')
def getName(person):
    return person['name']
fn = getName
print( fn({'name': 'Michael', 'age': 30}) )
print(fn.__name__) # getName3 指向装饰器函数内部的包裹函数wrapper