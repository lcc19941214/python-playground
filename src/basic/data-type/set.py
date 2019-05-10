# coding=utf-8

# dict
print('# dict')
numbers = set([1, 2, 3, 4])
print(numbers)

uniqNumbers = set([1, 1, 2, 3, 2, 3, 4])
print(uniqNumbers)

# manipulation
print('# manipulation')
# add
print('# add')
numbers.add('hello')
numbers.add('5')
numbers.add(5)
print(numbers)

# discard remove number
print('# discard remove number')
numbers.discard('hello')
numbers.discard(5)
print(numbers)

# remove
print('# remove')
numbers.remove(1)
numbers.remove(2)
print(numbers)

# operation
print('# operation')
print(set([1, 2, 3]) | set([4, 5, 6]))
print(set([1, 2, 3]) & set([3, 4, 5]))
