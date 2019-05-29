# coding=utf-8

# example
print('\n# example')


def simple_example():
    class Human(object):
        pass

    Tom = Human()
    print(Tom)
    print(Human)


simple_example()

# constructor
print('\n# constructor')


def constructor_example():
    class Human(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age

        '''
        和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self。
        调用时不用传递该参数。除此之外，类的方法和普通函数没有什么区别。
        所以仍然可以用默认参数、可变参数和关键字参数。
        '''
        def call_name(self):
            print('My name is %s' % self.name)

    Tom = Human('Tom Smith', 25)
    Tom.gender = 'M'
    print(Tom)
    print('name: %s' % Tom.name)
    print('age: %s' % Tom.age)
    print('gender: %s' % Tom.gender)
    Tom.call_name()


constructor_example()
