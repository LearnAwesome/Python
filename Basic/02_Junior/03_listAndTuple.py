# 列表list
'''
* 元素可变，长度可变，有序
* 索引值index正向0base，负向-1base
'''
classmates = ['Michael', 'Lucy', 'Peter']
print(classmates)                     # ['Michael', 'Lucy', 'Peter']
print(classmates[1]) # 'Lucy' 正向下标获取列表中的元素
# built-in@len() 获取长度
print( len(classmates) ) # 3
# list@append() 添加元素(在最后一位后)
classmates.append('Jeny') # 返回值None
print(classmates)                     # ['Michael', 'Lucy', 'Peter', 'Jeny']
# list@insert() 添加元素(指定位置)
classmates.insert(1, 'Marry') # 返回值None
print(classmates)                     # ['Michael', 'Marry', 'Lucy', 'Peter', 'Jeny']
# list@pop() 删除元素(可以指定位置，默认删除最后一位)
classmates.pop()
print(classmates)                     # ['Michael', 'Marry', 'Lucy', 'Peter']
classmates.pop(1)
print(classmates)                     # ['Michael', 'Lucy', 'Peter']
# 赋值改变列表元素
classmates[1] = 'Ray'
print(classmates)                     # ['Michael', 'Ray', 'Peter']

# 元组tuple
'''
* 内容指向不可变，长度不可变，有序
* 没有修改的方法
* 当心！只有一个元素的元组声明时需要加逗号来避免圆括号的运算歧义(1,)
'''
workers = ('Michael', 'Lucy', 'Peter')
print(workers) # ('Michael', 'Lucy', 'Peter')
# built-in@len() 获取长度
print( len(workers) ) # 3
wrongOneElementTuple = ('Michael')
print(wrongOneElementTuple) # 'Michael' 解释器认为()是运算符号
correctOneElementTuple = ('Michael',)
print(correctOneElementTuple) # ('Michael',)