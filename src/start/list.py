# coding=utf-8

# list
fruits = ['apple', 'pear', 'peach']
print fruits

# length
print len(fruits)

# index
print 'first item ' + fruits[0]
print 'second item ' + fruits[1]
print 'last item ' + fruits[-1]
print 'last but one item ' + fruits[-2]
try:
    print fruits[3]
except Exception as e:
    print 'Error: ' + e.__str__()

# manipulation
# append
fruits.append('strawberry')
fruits.append('watermelon')
print(fruits)

# insert
fruits.insert(0, 'grape')
fruits.insert(len(fruits), 'banala')
print(fruits)

# pop
fruits.pop()
fruits.pop(0)
print(fruits)

# remove remove first one
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
print(fruits.count('banala'))
print(fruits.count('sublist'))
print(fruits.count(sublist))

# clear
while len(fruits):
    fruits.pop()
print fruits
