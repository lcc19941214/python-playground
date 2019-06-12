# coding=utf-8

import os

# introduction
# how to create an list including [1,2,3,4,5,...,n]?
print('\n# how to create an list including [1,2,3,4,5,...,n]?')
L = range(1, 10)
print(L)

# how to create an list including [1x1, 2x2, 3x3, ... nxn]?
print('\n# how to create an list including [1x1, 2x2, 3x3, ... nxn]?')
L = []
for num in range(1, 10):
    L.append(num * num)
print(L)

# with list comprehension
print('\n# with list comprehension')
L = [x * x for x in range(1, 10)]
print(L)

L = ['%s:%s' % (index, value) for index, value in enumerate(['a', 'b', 'c'])]
print(L)

L = ['Loki', 'Steve', 'Natasha', 'Stark', 'Hulk', 'Eagle Eye', 'Thor']
L = [s.lower() for s in L]
print(L)

# list comprehension with condition statement
print('\n# list comprehension with condition statement')
L = [x * x for x in range(1, 10) if x % 2 == 0]
print(L)

'''
python没有三元表达式，可以使用 expression if condition else expression 这种写法代替实现
'''
L = ['Hello', 'World', 18, 'Apple', None]
L = [s.lower() if isinstance(s, str) else s.__str__() for s in L]
print(L)

# list comprehension with nested statement
print('\n# list comprehension with nested statement')
L = [m + n for m in 'ABC' for n in '123']
print(L)

# list dirs and files
print('\n# list dirs and files')
L = [d for d in os.listdir('.')]
print(L)