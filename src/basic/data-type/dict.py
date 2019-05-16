# coding=utf-8

# dict
print('\n# dict')
names = {
    'Hulk': 40,
    'Tony': 35,
    "Rogers": 70,
    'Thor': 1000
}
print(names)

# key
print('\n# key')
# both string and number can be the key
d = {}
d['1'] = 1
d[1] = 1
print(d)

# detection
print('\n# detection')
print(names.has_key('Hulk'))
print(names.has_key('Natasha'))
print('Loki' in names)
print(1 in d)

# manipulation
print('\n# manipulation')
# retrieve value
print('\n# retrieve value')
print(names['Hulk'])
print(names.get('Hulk'))
print(names.get('Loki', 3000))

# assign value
print('\n# assign value')
names['Thor'] = 2000
names['Loki'] = 1500
print(names)

# remove key
print('\n# remove key')
names.pop('Loki')
print(names)
try:
    names.pop('Natasha')
except Exception as error:
    print('error: ' + error.__str__())

# dict
print('\n# dict')
t1 = ('key', 'value')
t2 = ('hello', 'world')
t = (t1, t2)
arr = [t1, t2]
d1 = dict(t)
d2 = dict(arr)
d3 = dict([[1, 1], [2, 2]])
print(d1)
print(d2)
print(d3)
