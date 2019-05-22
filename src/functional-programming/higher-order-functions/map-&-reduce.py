# coding=utf-8

# map
print('\n# map')

L = [1, 2, 3, 4, 5, 6]
L2 = map(str, L)
print(L2)

L = [1, 2, 3, 4, 5, 6]


def square(num):
    return num * num


L2 = map(square, L)
print(L2)

# polyfill a map
print('\n# polyfill a map')


def equalization(val):
    return val


def map_polyfill(func=equalization, li=[]):
    return [func(x) for x in li]


print(map_polyfill(str, [1, 2, 3, 4]))

# reduce
print('\n# reduce')


def add(x, y):
    return x + y


L = [1, 2, 3, 4]
value = reduce(add, L)
print(value)

value = sum(L)
print(value)


# polyfill a reduce
print('\n# polyfill a reduce')


def map_reduce(func=equalization, li=[]):
    initialValue = li[0]
    for v in li[1:]:
        initialValue = func(initialValue, v)
    return initialValue


print(map_reduce(add, [1, 2, 3, 4, 5]))
print(map_reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))
