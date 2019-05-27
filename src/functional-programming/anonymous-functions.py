# coding=utf-8

'''
匿名函数只能有一个表达式，不用写return，返回值就是该表达式的结果
'''
L = range(1, 11)
L2 = map(lambda x: x*2, L)
print(L2)

func = lambda x: x**2
print(func)
print(func(5))