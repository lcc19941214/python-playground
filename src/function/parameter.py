# coding=utf-8


# 传入参数
print('\n# 传入参数')


def modify_param_1(num):
    # 修改基本数据类型
    num += 1
    return num


n = 1
print(modify_param_1(n))
print(n)


def modify_param_2(li):
    # 修改可变对象
    li.append(1)
    return li


li = [1]
print(modify_param_2(li))
print(li)

# 默认参数
print('\n# 默认参数')
# @see https://foofish.net/python-tricks.html
# 函数对象生成之后，它的属性：名字和默认参数列表都将初始化完成


def default_param(name='Amy'):
    # 默认值为不可变对象
    print(name)


default_param('Bob')
default_param()


def default_param_li(l=[]):
    # 默认值为可变对象
    # 多次函数调用，共享的是同一个默认参数对象，只是每调用一次就往该列表中增加了一个元素
    l.append('item')
    print(l)


print(default_param_li.__name__)
print(default_param_li.__defaults__)

default_param_li()
default_param_li()


def default_param_li_no_cache(l=None):
    # 默认值为None
    if l is None:
        l = []
    l.append('item')
    print(l)


default_param_li_no_cache()
default_param_li_no_cache()

# 具名默认参数
print('\n# 具名默认参数')


def default_param_with_name(name, age, city='Beijing', gender='F'):
    print('name: ', name, 'age: ', age, 'city: ', city, 'gender: ', gender)


default_param_with_name('Amy', 25)
default_param_with_name('Bob', 30, city="Shanghai")
default_param_with_name('Cindy', 10, gender='M')

# 可变参数
print('\n# 可变参数')


def mutable_param(*numbers):
    # * 关键字类似于 js 里的参数展开 ... ，会转变成一个 tuple
    # 但是 python 支持 参数组合，*可变参数 后面还可以传入其他参数
    print(numbers)


mutable_param(1, 2, 3, 4)
num_list = [1, 2, 3, 4, 5]
mutable_param(num_list)
mutable_param(*num_list)  # use * to spread the list or tuple

# 关键字参数
print('\n# 关键字参数')


def key_word_param(a, b, c, **kw):
    # 键字参数允许你传入0个或任意个含参数名的参数
    print(a, b, c, kw)


key_word_param('a', 'b', 'c')
key_word_param('a', 'b', 'c', x='x', y='y', z='z')
kw = {'alpha': 'a', 'beta': 'b'}
key_word_param(1, 2, 3, **kw)

# 参数组合
print('\n# 参数组合')


def func(a, b, c, *args, **kw):
    print('a', a)
    print('b', b)
    print('c', c)
    print('args', args)
    print('kw', kw)
    print('------')


func(1, 2, 3)
func(1, 2, 3, 'args1', 'args2')
func(1, 2, 3, *('args1', 'args2'), x='x', y='y')


# conclusion
'''
默认参数一定要用不可变对象，如果是可变对象，运行会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
'''
