# coding=utf-8

import functools

# partial function
print('\n# partial function')

'''
difference between partial function and curry function
@see https://segmentfault.com/q/1010000008626058
'''

'''
偏函数用于固定函数中的指定参数的值
'''

print(int('250'))
print(int('1234', 8))
print(int('10101010110', base=2))


def int_2(x, base=2):
    return int(x, base)


print(int_2('110'))

int_16 = functools.partial(int, base=16)
print(int_16('1f'))
