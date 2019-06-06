# coding=utf-8
from enum import Enum, unique

# normal usage
print('\n# normal usage')

Week = Enum('Week', ('Monday', 'Tuesday', 'Wednesday',
                     'Thursday', 'Friday', 'Saturday', 'Sunday'))

print(Week)
'''
value属性则是自动赋给成员的int常量，默认从1开始计数。
'''
for name, member in Week.__members__.items():
    print("%s => %s, %s" % (name, member, member.value))

# customize
print('\n# customize')


@unique
class FiveElements(Enum):
    Metal = 0
    Wood = 1
    Water = 2
    Fire = 3
    Earth = 4


metal = FiveElements.Metal
print(metal)
fire = FiveElements.Fire
print('%s => %s' % (fire, fire.value))
