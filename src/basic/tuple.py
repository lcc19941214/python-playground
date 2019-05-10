# coding=utf-8

# tuple
t1 = (1)
t2 = (1,)
t3 = ('a', 'b', 'c')
t4 = (1, 'b', True, [1, 2, 3])
print(t1)
print(t2)
print(t3)
print(t4)

# index
print('index of:' + t3.index('c').__str__())
print(t2[0])
print(t3[1])
print(t4[2])

# manipulation
# manipulation is not allowed for immutable element in tuple
try:
    t2[0] = 2
except Exception as error:
    print('error: ' + error.__str__())

print(t4)
t4[3][0] = 'mutable'
print(t4)
