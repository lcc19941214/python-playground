# coding=utf-8

# dict
print('\n# dict')
numbers = set([1, 2, 3, 4])
print(numbers)

uniqNumbers = set([1, 1, 2, 3, 2, 3, 4])
print(uniqNumbers)

# manipulation
print('\n# manipulation')
# add
print('\n# add')
numbers.add('hello')
numbers.add('5')
numbers.add(5)
print(numbers)

# discard remove number
print('\n# discard remove number')
numbers.discard('hello')
numbers.discard(5)
print(numbers)

# remove
print('\n# remove')
numbers.remove(1)
numbers.remove(2)
print(numbers)

# operation
print('\n# operation')
print(set([1, 2, 3]) | set([4, 5, 6]))
print(set([1, 2, 3]) & set([3, 4, 5]))
