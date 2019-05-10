# coding=utf-8

# statement
print('# statement')
a = 1
b = 2
c = 3
d = e = f = 4
g, h, i = 5, 6, 7
print(a, b, c, d, e, f, g, h, i)

# delete
print(a)
del a
try:
  print(a)
except Exception as error:
  print('error: ' + error.__str__())
