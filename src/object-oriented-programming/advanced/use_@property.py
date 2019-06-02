# coding=utf-8

# 参数检查、限制属性访问
'''
Python内置的@property装饰器可以把把一个方法变成属性调用
把一个getter方法变成属性，只需要加上@property就可以了
'''

print('\n# Example: Student')


class Student(object):
    @property
    def score(self):
        # it's wired if set with __score and use getattr to get __score
        # return getattr(self, '_score', 0)
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an interger')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')
        self.__score = value


std_1 = Student()
std_1.score = 60
print(std_1.score)
try:
    std_1.score = 999
except Exception as error:
    print(error.__str__())

print('\n# Example: Screen')


class Screen(object):
    def validate(self, value):
        if not isinstance(value, int):
            raise ValueError('value is not an interger')

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        self.validate(value)
        self.__width = value

    @height.setter
    def height(self, value):
        self.validate(value)
        self.__height = value

    @property
    def resolution(self):
        return "%s x %s" % (self.width, self.height)


s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
s.width = 2096
print(s.resolution)