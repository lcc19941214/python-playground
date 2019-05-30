# coding=utf-8


class Animal(object):
    def __init__(self, species):
        self.species = species

    def run(self, speed=1):
        unit = 'meter' if speed == 1 else 'meters'
        print('%s is running at %s %s per second' %
              (self.species, speed, unit))


class Dog(Animal):
    pass


class Cat(Animal):
    def run(self):
        # call super
        super(Cat, self).run()
        print('Cat cannot run too fast!')


class BlurCat(Cat):
    pass


if __name__ == "__main__":
    # inherit
    print('\n# inherit')
    dog = Dog('Dog')
    dog.run(20)
    cat = Cat('Cat')
    cat.run()
    blue_cat = BlurCat('BlurCat')
    blue_cat.run()

    # is instance
    print('\n# is instance')
    print('isinstance(cat, Dog): %s' % isinstance(cat, Dog).__str__())
    print('isinstance(dog, Dog): %s' % isinstance(dog, Dog).__str__())
    print('isinstance(cat, Animal): %s' % isinstance(cat, Animal).__str__())
    print('isinstance(cat, Cat): %s' % isinstance(cat, Cat).__str__())
    print('isinstance(blue_cat, Cat): %s' %
          isinstance(blue_cat, Cat).__str__())
