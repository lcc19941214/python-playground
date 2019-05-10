# coding=utf-8

# dict
print('# dict')
names = {
    'Hulk': 40,
    'Tony': 35,
    "Rogers": 70,
    'Thor': 1000
}
print(names)

# key
print('# key')
# both string and number can be the key
d = {}
d['1'] = 1
d[1] = 1
print(d)

# detection
print('# detection')
print(names.has_key('Hulk'))
print(names.has_key('Natasha'))
print('Loki' in names)
print(1 in d)

# manipulation
print('# manipulation')
# retrieve value
print('# retrieve value')
print(names['Hulk'])
print(names.get('Hulk'))
print(names.get('Loki', 3000))

# assign value
print('# assign value')
names['Thor'] = 2000
names['Loki'] = 1500
print(names)

# remove key
print('# remove key')
names.pop('Loki')
print(names)
try:
    names.pop('Natasha')
except Exception as error:
    print('error: ' + error.__str__())
