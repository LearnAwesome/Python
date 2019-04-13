# 条件判断
'''
* 基本形式 if-elif-else
* 只要进入到某一个条件中，则不会进入到其他有交集的条件中
'''
age = 20
if age >= 18:
    print('adult')
elif age >= 6 and age < 18:
    print('teenager')
else:
    print('kid')

# 条件简写
''' 下列数据判断运算结果为False '''
cond_false = False    # 假
cond_none = None      # 空
cond_zero = 0         # 零
cond_emptyStr = ''    # 空字符串
cond_emptyList = []   # 空列表
cond_emptyTuple = ()  # 空元组
cond = cond_false or cond_none or cond_zero or cond_emptyStr or cond_emptyList or cond_emptyTuple
if cond:
	print('right')
else:
	print('wrong') # 'wrong'

# 注意使用控制台input()获取的一切数据均为字符串
inp = input('Press: ')
inp = int(inp) # 注意使用int()来将字符串转换为数字
if inp > 10:
	print('beyond 10')
else:
	print('not beyond 10')