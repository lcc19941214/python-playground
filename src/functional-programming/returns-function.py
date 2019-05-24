# coding=utf-8

# sample
print('\n# sample')
# sum
print('\n# sum')

L = range(1, 6)


def calc_sum(*args):
    rst = 0
    for x in args:
        rst += x
    return rst


print(calc_sum(*L))

# lazy sum
print('\n# lazy sum')


def lazy_sum(*args):
    def sum():
        rst = 0
        for x in args:
            rst += x
        return rst
    return sum


fn = lazy_sum(*L)
print(fn)
print(fn())


# closure
print('\n# closure')
'''
闭包
注意到返回的函数在其定义内部引用了局部变量args，所以，当一个
函数返回了一个函数后，其内部的局部变量还被新函数引用。
注意：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
'''


def count():
    # 类似于 JavaScrip，函数 f 持有的是 i 的引用，循环结束后，i 已经累加到了 3
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

# fixed
print('\n# fixed')


def count_2():
    fs = []
    for i in range(1, 4):
        def f(v=i):
            return v * v
        fs.append(f)
    return fs


f1, f2, f3 = count_2()
print(f1(), f2(), f3())


def count_3():
    fs = []
    for i in range(1, 4):
        def outter_f(v):
            def inner_f():
                return v * v
            return inner_f
        fs.append(outter_f(i))
    return fs


f1, f2, f3 = count_3()
print(f1(), f2(), f3())
