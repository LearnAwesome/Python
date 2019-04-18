# 过滤 filter()
'''
* built-in@filter(func, iterable)
* 过滤条件为func返回为True
* 返回Iterator
'''

r = filter(lambda x: x % 2 == 0, range(1, 11))
print(list(r)) # [2, 4, 6, 8, 10]

''' 埃氏筛法 '''
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for i in primes():
    print(i) # 2 3 5 7 11 13 17 19 23 29 31
    if i > 30:
        break

''' 输出回数序列 '''
def _is_palindrome(n):
    # return str(n) == str(n)[::-1] # 简易方法O(n)
    # 复杂方法 O(n/2)
    str_num = str(n)
    loop_len = len(str_num) / 2
    i = 0
    while i < loop_len:
        if (str_num[i] != str_num[-i - 1]):
            return False
        i += 1
    return True


def palindromes(n):
    return list( filter( _is_palindrome, range(1, n) ) )

print(palindromes(10000)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]