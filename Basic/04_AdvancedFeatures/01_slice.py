# 切片slice
'''
* 切片功能可以很方便的截取str/range/list/tuple中的一段，作为拷贝
* list[起始位置:结束位置:跳过数量]
* 包含起始项，不含结束项
* 支持负向操作
* 如果起始位置是0，可以省略
'''
l1 = [0, 1, 2]
print(l1[0:3]) # [0, 1, 2]
print(l1[:2]) # [0, 1]
l2 = l1[:] # 拷贝l1
l2[0] = 'a'
print(l1) # [0, 1, 2]

print(l1[-1:]) # [2]
print('ABC'[:2]) # 'AB'
print('ABC'[::2]) # 'AC' 每隔两个切片一次