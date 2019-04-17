# def is_palindrome(n):
#     n = str(n)
#     i = 0
#     while i < int(len(n) / 2):
#         if n[i] != n[-1 - i]:
#             return False
#         i += 1
#     return True

# print(list(filter(is_palindrome, range(1, 100000))))

# def _odd_iter():
#     n = 1
#     while True:
#         n += 2
#         yield n

# def _not_divisible(n):
#     return lambda x: x % n > 0

# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible(n), it)

# for i in primes():
#     if i < 1000:
#         print(i)
#     else:
#         break