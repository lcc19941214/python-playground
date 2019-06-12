# coding=utf-8

# slice
L = ['Loki', 'Steve', 'Natasha', 'Stark', 'Hulk', 'Eagle Eye', 'Thor']

print(L[0:3])
print(L[:4])
print(L[5:])
print(L[:-1])
print(L[-3:])

# slice with steps
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = num[::2]
even = num[1::2]
print('odd number includes %s' % odd)
print('even number includes %s' % even)


# copy
L = [1,2,3,4,5]
L_copy = L[:]
print(L_copy)
print(L_copy is L)
print(L_copy == L)

'''
about == and is
@see https://juejin.im/entry/5a3b62446fb9a0451f311b5c

is比较的是两个对象的id值是否相等，也就是比较两个对象是否为同一个实例对象，是否指向同一个内存地址。
==比较的是两个对象的内容是否相等，默认会调用对象的__eq__()方法
'''