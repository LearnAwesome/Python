# 过滤 filter()
'''
* built-in@filter(func, iterable)
* 过滤条件为func返回为True
* 返回Iterator
'''

r = filter(lambda x: x % 2 == 0, range(1, 11))
print(r)

print('hahahahah')