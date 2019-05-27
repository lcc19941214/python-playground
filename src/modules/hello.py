# coding=utf-8

'''
a hello module
任何模块代码的第一个字符串都被视为模块的文档注释
'''

# 写入模块的作者名
__author__ = 'Cool Conan'

import sys


def say_hello():
    # sys.argv includes filename at least
    argv = sys.argv
    if len(argv) == 1:
        print('Hello world - [%s]' % argv[0])
    elif len(argv) == 2:
        print('Hello, %s' % argv[1])
    else:
        print 'Too many arguments'

name = 'Conan'
birth_year = 1900

# a private variable
_gender = 'Male'

'''
当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
而如果在其他地方导入该hello模块时，if判断将失败。
'''
if __name__ == "__main__":
    print('called with interpreter')
    say_hello()
else:
    # once import this line will be called
    # multiple import will only execute once
    print('called as a module')
