# coding=utf-8

from inherit_polymorphism import Animal, Cat, Dog
import types

# type
print('\n# type')


class Human(object):
    pass


def func():
    pass


dog = Dog('Dog')
cat = Cat('Cat')


print(type(0))
print(type(1.0))
print(type('hello'))
print(type(None))
print(type(True))
print(type({}))
print(type([]))
print(type((1, 2)))
print(type(abs))
print(type(str))
print(type(func))
print(type(Human))
print(type(dog))

# compare type()
print('\n## compare type()')

print(type(1) == type(2))
print(type('hello') == type(False))
print(type(0) == types.IntType)
print(type(None) == types.NoneType)
print(type(float) == types.TypeType)

# isinstance
print('\n# isinstance')

print(isinstance('a', str))
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(cat, Dog))
print(isinstance(1, (int, float)))  # 多个type的其中一种，可以用 tuple
print(isinstance(1, (bool, float)))  # 多个type的其中一种，可以用 tuple

# is & ==
'''
about == and is
@see https://juejin.im/entry/5a3b62446fb9a0451f311b5c

is比较的是两个对象的id值是否相等，也就是比较两个对象是否为同一个实例对象，是否指向同一个内存地址。
==比较的是两个对象的内容是否相等，默认会调用对象的__eq__()方法
'''
print('\n# is & ==')
L1 = [1, 2, 3]
L2 = [1, 2]
L3 = L1[:]
print('L1 is L2 => %s' % (L1 is L2))
print('L1 is not L2 => %s' % (L1 is not L2))
print('L1 is L3 => %s' % (L1 is L3))
print('L2 is L3 => %s' % (L2 is L3))
print('L1 is L1 => %s' % (L1 is L1))
print('---')
print('L1 == L2 => %s' % (L1 == L2))
print('L1 != L2 => %s' % (L1 != L2))
print('L1 == L3 => %s' % (L1 == L3))
print('L2 == L3 => %s' % (L2 == L3))
print('L1 == L1 => %s' % (L1 == L1))

# dir
print('\n# dir')
print(dir(1))
print(dir({'name': 'Tom'}))
print(dir(True))
