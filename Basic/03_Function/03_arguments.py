# 默认参数
def f1(name, age, city = 'China', work = 'it'):
    print('Name: %s, Age: %d, City: %s, Work: %s' % (name, age, city, work))
f1('Michael', 30) # Name: Michael, Age: 30, City: China, Work: IT
'''
默认参数有坑：如果默认值是可变对象list/tuple/dict等，需要用None来替换
'''
def f2(arg = []):
    arg.append('end')
    print(arg)
f2() # ['end']
f2() # ['end', 'end']
def f3(arg = None):
    if arg is None:
        arg = []
    arg.append('end')
    print(arg)
f3() # ['end']
f3() # ['end']
'''
如果参数是默认参数，则可以不按顺序传入，只需要在传入时指定key
'''
f1('Michael', 30, work = 'teacher') # Name: Michael, Age: 30, City: China, Work: teacher

# 可变参数*arg
'''
* *arg实质上是一个tuple
* 实参也可以传入range/list/tuple，需要在前面加上*来展开
'''
def f4(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    print(sum)
f4(1, 2, 3) # 6
f4(*[1, 2, 3]) # 6
f4(*(1, 2, 3)) # 6
f4(*range(4)) # 6

# 关键词参数**kw
'''
* **kw实质上是一个dict
* 实参页可以传入dict，需要在前面加上**来展开
'''
def f5(name, age, **kw):
    print('Name: %s, Age: %d, Keyword: %s ' % (name, age, kw))
f5('Michael', 30, city = 'Xian', work = 'IT') # Name: Michael, Age: 30, Keyword: {'city': 'Xian', 'work': 'IT'}
f5('Michael', 30, **{ 'city': 'Xian', 'work': 'IT' }) # Name: Michael, Age: 30, Keyword: {'city': 'Xian', 'work': 'IT'}

# 命名关键词参数
'''
* 有时候想使用关键词参数的**实参的便利性，但又想限制传入的key，这时要用命名关键词参数
* 如果命名关键词参数前没有可变参数，则需要补一位*参数来声明其后的参数
* 如果有可变参数，则后面的参数默认视为命名关键词参数
* 命名关键词参数也可以含有默认参数
'''
def f6(name, *, age, sex):
    print('Name: %s, Other: %s' % (name, (age, sex)))
f6('Michael', **{'age': 30, 'sex': 'male'}) # Name: Michael, Other: (30, 'male')
def f7(name, *args, age, work = 'IT'):
    print('Name: %s, Friends: %s, Age: %s, Work: %s' % (name, args, age, work))
f7('Michael', *['Lucy', 'Peter'], **{'age':30}) # Name: Michael, Friends: ('Lucy', 'Peter'), Age: 30, Work: IT

# 参数组合
'''
参数排列的顺序一定是：位置参数(默认参数) > 可变参数*arg > 关键词参数**kw > 命名关键词参数(默认参数)
'''
def intro(name, age, *friends, city = 'China', idNumber, sex, **other):
    print('################################## \n' \
        'Hello, my name is %s, I\'m %d years old. \n' \
        'I come from %s. \n' \
        'I have many friends named %s. \n' \
        'If you want to know, I can tell you my id number is %d, and I am a %s. \n' \
        'There is my other infomation: %s. \n' \
        'Bye! \n' \
        '##################################' \
        % (name, age, city, friends, idNumber, 'boy' if sex == 'male' else 'girl', other))
intro('Michael', 30, *['Lucy', 'Peter'], **{'idNumber': 9527, 'sex': 'male', 'parent': ['Liang', 'Feng']})
'''
################################## 
Hello, my name is Michael, I'm 30 years old. 
I come from China. 
I have many friends named ('Lucy', 'Peter'). 
If you want to know, I can tell you my id number is 9527, and I am a boy. 
There is my other infomation: {'parent': ['Liang', 'Feng']}. 
Bye! 
##################################
'''