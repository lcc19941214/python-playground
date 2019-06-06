# coding=utf-8


class Animal(object):
    def __init__(self, name):
        self.name = name


class Human(object):
    def __init__(self, name):
        self.name = name
        self.__age = 0

    def __str__(self):
        return '<class Human>: %s' % self.name

    __repr__ = __str__

    # 自定义迭代器
    def __iter__(self):
        while self.__age < 10:
            self.__age += 1
            pass
            yield 'This human is now %s year\'s old' % self.__age
        raise StopIteration()

    # def __getitem__(self):
        # 适用于 object[key] 以及 切片 调用的场景
        # pass

    def __getattr__(self, attr):
        # 有点类似 es6 中的 proxy 的 get
        return attr

    def __call__(self):
        print('My name is %s' % self.name)


animal = Animal('dog')
human = Human('Tom')

# __str__
print('\n# __str__')
print(animal)
print(human)

# __iter__ & __next__
print('\n# __iter__ & __next__')
try:
    for n in animal:
        print(n)
except Exception as error:
    print(error.__str__())

for n in human:
    print(n)

# __getattr__
print('\n# __getattr__')
try:
    print(animal.name)
    print(getattr(animal, 'are u ok', '404'))
    print(animal.age)
except Exception as error:
    print(error.__str__())
print(human.name)
print(human.age)
print(getattr(human, 'are u ok'))

# __call__
print('\n# __call__')
try:
    animal()
except Exception as error:
    print(error.__str__())
human()
