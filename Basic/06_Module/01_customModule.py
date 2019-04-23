#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块 module
'''
* 任何一个同级目录下的.py文件都可以看作是一个model
* 一般使用import [filename]的形式来引入
* 再用[filename].属性或方法的形式来使用
* module中的第一个字符串可作为模块注释，可以通过[filename].__doc__来获取
'''
''' 引入方式1: 引入模块 '''
# import myModule
# print(myModule.var_num) # 123
# myModule.say('Michael') # Hi, Michael. It is a module!
# print(myModule.__doc__) # It's a doc, can be found with __doc__
''' 引入方式2: 引入模块中的属性或方法(两种方法)
* from [filename] import [export1, export2, ...]
* from [filename] import *
'''
# from myModule import var_num, say
# print(var_num) # 123
# say('Michael') # Hi, Michael. It is a module!
# from myModule import *
# print(var_num) # 123
# say('Michael') # Hi, Michael. It is a module!

# 包 package
'''
* 任何一个同级目录下，只要含有__init__.py文件，都当作package处理
* 父package下也可以包含子package，子package中同样需要含有__init__.py文件
* 包内模块间互相可以引用，使用import [packageName].[moduleName]来引入
'''
''' 引入方式1: 单独引入包内模块(两种方法)
* import [packageName].[moduleName]
* from [packageName] import [moduleName1, moduleName2, ...]
'''
# import myPackage.a
# myPackage.a.sayHello('Michael') # Hello, Michael!
# from myPackage import a, b
# a.sayHello('Michael') # Hello, Michael!
# b.sayBye('Michael') # Bye, Michael!
''' 引入方式2: 引入包内所有模块(需要在包内__init__.py文件写入: __all__ = [moduleName1, moduleName2, ...]) '''
# from myPackage import *
# a.sayHello('Michael') # Hello, Michael!
# b.sayBye('Michael') # Bye, Michael!

''' 小技巧：在模块中写测试，但是并不想打印出来。此时需要用if __name__ == __main__ 来判断是否为直接调用 '''
import myPackage.a
myPackage.a.sayHello('Michael')
# '''
# Hello, test!
# test sayHello(): None
# Hello, Michael!
# '''
