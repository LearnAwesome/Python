# 字典dict
'''
* 全称dictionary，在其他语言中称为map或object，使用key-value的方式储存
* 通过key计算位置的算法称为哈希算法（Hash）
* 与list/tuple相比，dict的优点是速度快，缺点是占空间多
* 其中key必须是不可变对象(字符串 / 数字)
'''
d = {
    'Michael': 30,
    'Lucy': 24,
    'Peter': 54
}
print(d['Michael']) # 30 获取
print('Lucy' in d) # True 查看是否存在key
print(d.get('Peter')) # 54 通过dict@get()来查看是否存在key
print(d.get('Marry', -1)) # -1 可以指定不存在时的返回值
d['Peter'] = 20 # 通过赋值的方式改变value
print(d['Peter']) # 20
d.pop('Michael') # 通过dict@pop()来删除键值对
print(d) # {'Lucy': 24, 'Peter': 20}

# 集合set
'''
* 与dict的特点基本相同，不同点是只储存key，而不储存value
* 集合中不存在重复元素
* 通过global@set()来创建，需要传入range/list/tuple来作为source
'''
s = set([1, 2, 3, 3, 2])
print(s) # {1, 2, 3}
s = set(range(4))
print(s) # {0, 1, 2, 3}
s = set(list(range(2)))
print(s) # {0, 1}
s = set(tuple(range(2)))
print(s) # {0, 1}
# set@add() 添加元素，如果被添加的元素重复，则无效
s.add(2)
print(s) # {0, 1, 2}
s.add(0)
print(s) # {0, 1, 2}
# set@remove() 删除元素，如果被删除元素不存在，报错
s.remove(2)
print(s) # {0, 1}
# 集合可以做数学上的交集，并集
s1 = set([0, 1, 2])
print(s & s1) # {0, 1} 交集
print(s | s1) # {0, 1, 2} 并集