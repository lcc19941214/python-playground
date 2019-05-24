# coding=utf-8

# sorted

'''
not like javascript, sorted in python will return a new list
'''
L = [123, 41, 46, 61, 43]
L2 = sorted(L)
print(L)
print(L2)

# reverse
L = [1, 2, 3, 4, 5, 6, 7]


def fn_reverse(a, b):
    if (a < b):
        return 1
    if (a > b):
        return -1
    return 0


L2 = sorted(L, fn_reverse)
print(L2)

# sort string
L = ['Lily', 'Amy', 'huLK', 'Zara', 'aLoha']


def cmp_string(a='', b=''):
    s1 = a.lower()
    s2 = b.lower()
    if (s1 < s2):
        return -1
    if (s1 > s2):
        return 1
    return 0


L2 = sorted(L)
L3 = sorted(L, cmp_string)
print(L2)
print(L3)
