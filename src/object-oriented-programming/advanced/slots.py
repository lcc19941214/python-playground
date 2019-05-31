# coding=utf-8

'''
正常情况下，实例化后，可以给该实例绑定任何属性和方法
'''


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score


std_a = Student('Tom', 'A')
print(std_a.get_score())
std_a.set_score('S')
print(std_a.get_score())

'''
如果我们想要限制实例的属性，
Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性.
__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的.
除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
'''


class Human(object):
    def __init__(self, name):
        self.name = name

    __slots__ = ('age', 'gender', 'name')


tom = Human('Tom')
print(tom.name)
tom.age = 25
try:
    tom.height = 178
except Exception as error:
    print(error.__str__())


class Boy(Human):
    __slots__ = ('weight')
    pass


bob = Boy('Bob')
try:
    bob.height = 178
    print(bob.height)
except Exception as error:
    print(error.__str__())
