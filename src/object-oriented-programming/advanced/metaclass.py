# coding=utf-8

# declare a class
print('\n# declare a class')


class Dog(object):
    def bark(self):
        print('wow wow wow')


print(type(Dog))
print(type(Dog()))

'''
要创建一个class对象，type()函数依次传入3个参数：

class的名称；
继承的父类集合，注意Python支持多重继承，如果只有一个父类，需要使用tuple的单元素写法；
class的方法名称与函数绑定，可以使用一个dict。
'''

# use type to create a class
print('\n# use type to create a class')


def meow(self):
    print('meow meow meow')


Cat = type('Cat', (object,), dict(meow=meow))

print(type(Cat))
print(type(Cat()))
Cat().meow()

# metaclass
print('\nmetaclass')

'''
当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
metaclass是Python面向对象里最难理解，也是最难使用的魔术代码
'''

# @see https://www.liaoxuefeng.com/wiki/1016959663602400/1017592449371072