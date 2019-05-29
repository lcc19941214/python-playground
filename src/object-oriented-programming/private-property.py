# coding=utf-8

import datetime


class Human(object):
    def __init__(self, name, birth_year):
        self.__name = name
        self.birth_year = birth_year

    def get_age(self):
        year = datetime.date.today().year
        age = year - self.birth_year
        return age

    def say_name(self):
        print(self.__name)


Conan = Human('Conan', 1990)
print(Conan.get_age())

try:
    print('print __name: %s' % Conan.__name)
except Exception as error:
    print(error.__str__())

print('print _Human__name: %s' % Conan._Human__name)

Conan.say_name()
