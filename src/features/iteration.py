# coding=utf-8

from collections import Iterable

'''
list这种数据类型虽然有下标，但很多其他数据类型是没有下标的\
但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代
'''

# iterate a dict
print('\n# iterate a dict')
d = {'name': 'Lily', 'age': 25}
for key in d:
    print('dict d has a property %s and its value is %s' % (key, d.get(key)))

# detect wether an object is iterable
print('\n# detect wether an object is iterable')
print(isinstance('abc', Iterable))
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance(25, Iterable))
print(isinstance((1,), Iterable))

# iterate with index
print('\n# iterate with index')
'''
Python内置的enumerate函数可以把一个list变成索引-元素对，
这样就可以在for循环中同时迭代索引和元素本身
'''
alphabet = ['a', 'b', 'c']
print('using enumerate:')
for index, value in enumerate(alphabet):
    print('index: %d; value: %s' % (index, value))

'''
也可以只用 range + len 实现 index
'''
print('using range and len:')
for index in range(len(alphabet)):
    print('index: %d; value: %s' % (index, alphabet[index]))

# interate with multiple variables
print('\n# interate with multiple variables')
coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:
    print('x: %s, y: %s' % (x, y))
