# coding=utf-8

# module
print('\n# module')

import hello

## call the module method
hello.say_hello()

## read a module variable
print('\n## read a module variable')
print('The author is %s' % hello.__author__)
print('We can access the variable [%s]: %s' % ('name', hello.name))

## try print variable bellow
# hello.__doc__
# hello.__name__
# hello.__file__

## reassign a variable
'''
Python并没有一种方法可以完全限制访问private函数或变量，
但是，编程时不应该引用private函数或变量

@see https://segmentfault.com/a/1190000002611411
约定：
_xxx  这表示这是一个保护成员（属性或者方法），它不能用from module import * 导入，其他方面和公有一样访问

__xxx  这表示这是一个私有成员，它无法直接像公有成员一样随便访问，可通过对象名._类名__xxx这样的方式访问

__xxx__  这表示这是一个特殊成员，所谓特殊，就是例如__init__()  __del__()  __call__()这些特殊方法
'''
print('\n## reassign a variable')
hello.__author__ = 'Cool Boy'
print('The author is %s now!' % hello.__author__) # this works!
hello.birth_year = 2012
print('The birth year also has been changed: %s' % hello.birth_year)

# alias
print('\n# alias')

try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

print(StringIO)