# coding=utf-8

import sys
from os import path
sys.path.append(path.dirname(path.dirname(
    path.dirname(path.abspath(__file__)))))
from utils.section import section

# list
section('# list')
fruits = ['apple', 'pear', 'peach']
print(fruits)

# length
section('# length')
print(len(fruits))

# index
section('# index')
print('index of ' + fruits.index('pear').__str__())
print('first item ' + fruits[0])
print('second item ' + fruits[1])
print('last item ' + fruits[-1])
print('last but one item ' + fruits[-2])
try:
    print(fruits[3])
except Exception as e:
    print('Error: ' + e.__str__())

# manipulation
section('# manipulation')
# assign value
section('# assign value')
fruits[0] = 'APPLE'
print(fruits)

# append
section('# append')
fruits.append('strawberry')
fruits.append('watermelon')
print(fruits)

# insert
section('# insert')
fruits.insert(0, 'grape')
fruits.insert(len(fruits), 'banala')
print(fruits)

# pop
section('# pop')
fruits.pop()
fruits.pop(0)
print(fruits)

# remove remove first one
section('# remove remove first one')
fruits.append('banala')
fruits.append('banala')
print(fruits)
fruits.remove('banala')
print(fruits)

sublist = ['tony', 'steve', 'banner']
fruits.append(sublist)
fruits.append(sublist)
print(fruits)
fruits.remove(sublist)
print(fruits)

# count
section('# count')
print(fruits.count('banala'))
print(fruits.count('sublist'))
print(fruits.count(sublist))

# clear
section('# clear')
while len(fruits):
    fruits.pop()
print(fruits)

# concat & repeat
section('# concat & repeat')
print([1, 2, 3] + [4, 5, 6])
print([1, 2, 3] * 3)
