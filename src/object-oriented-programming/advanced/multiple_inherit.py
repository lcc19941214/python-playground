# coding=utf-8


class Animal(object):
    @property
    def category(self):
        return 'Animal'


class Mammal(Animal):
    def breeding(self):
        print('Mammals are viviparous animals')


class Bird(Animal):
    def breeding(self):
        print('Birds are egg-laying animals')


class Runnable(object):
    def run(self, speed=0):
        if not isinstance(speed, int):
            raise ValueError('speed is not an integer')
        print('[Run]: %s m/s' % speed)


class Flyable(object):
    def fly(self, height=0):
        if not isinstance(height, int):
            raise ValueError('height is not an integer')
        print('[Fly]: at %s meter(s) high' % height)


class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


class Parrot(Bird, Flyable):
    pass


class Ostrich(Bird, Runnable):
    pass

dog = Dog()
bat = Bat()
parrot = Parrot()
ostrich = Ostrich()

print('\n# dog')
print('Category of dog: %s' % dog.category)
dog.breeding()
dog.run(10)

print('\n# bat')
bat.breeding()
bat.fly(5)

print('\n# parrot')
parrot.breeding()
parrot.fly(10)

print('\n# ostrich')
ostrich.breeding()
ostrich.run(2)
