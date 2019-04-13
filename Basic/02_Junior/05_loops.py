# for in循环
classmates = ['Michael', 'Lucy', 'Peter']
for name in classmates:
	print(name)

# while循环
n = 10
while n > 0:
    n = n - 2
    print(n)

# 跳出循环break
n = 10
while n > 0:
    n -= 2
    if n < 6:
        break
    print(n)

# 跳过当前循环continue
n = 10
while n > 0:
    n -= 1
    if n % 2 == 0:
        continue
    print(n)

''' 
可以配合
    * global@range() 获得连续范围
    * global@list() / global@tuple() 通过范围获得列表 / 元组
来快速生成可循环的对象
'''
for n in range(5):
    print(n)