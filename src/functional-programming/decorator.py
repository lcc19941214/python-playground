# coding=utf-8

import datetime
import time
import functools

'''
在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
'''

# simple
print('\nsimple')


def get_time():
    return datetime.datetime.now()


def simple():
    def log(func):
        def wrapper(*args, **kw):
            print('call %s():') % func.__name__
            return func(*args, **kw)
        return wrapper

    @log
    def now():
        print(get_time())

    now()
    # note the name is not 'now'
    print(now.__name__)


simple()

# complicated
print('\n# complicated')


def complicated():
    def logger(text):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():') % (text, func.__name__)
                return func(*args, **kw)
            return wrapper
        return decorator

    @logger('timer')
    def now():
        print(get_time())

    now()
    print(now.__name__)


complicated()

# playground
print('\n# playground')


def playground():
    # time logger
    print('\n## time logger')

    def timeLogger(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            start = time.time()
            rst = func(*args, **kw)
            end = time.time()
            time_spent = (end - start) * 1000
            print('[%s]: %s ms') % (func.__name__, time_spent)
            return rst
        return wrapper

    @timeLogger
    def f():
        i = 0
        while i < 1000000:
            i = i + 1
        return

    f()

    # advanced logger
    print('\n## advanced logger')
    '''
    编写一个装饰器，支持直接使用，也支持传入参数
    '''

    def advancedLogger(f):
        def getWrapper(func, text='call'):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('[%s] %s:') % (text, func.__name__)
                return func(*args, **kw)
            return wrapper

        if isinstance(f, str):
            def fn(func): return getWrapper(func, f)
        elif callable(f):
            # use callable for python 2.x or 3.2+
            # for python 3.x but before 3.2, check the `__call__` property
            # @see https://stackoverflow.com/questions/624926/how-do-i-detect-whether-a-python-variable-is-a-function
            fn = getWrapper(f)
        return fn

    @advancedLogger
    def func_a(str):
        print('hello %s' % str)

    @advancedLogger('Debug')
    def func_b(str):
        print('hi %s' % str)

    func_a('world')
    func_b('world')


playground()
