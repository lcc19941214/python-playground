# coding=utf-8

# a sample
print('\n# a sample')
L = [x * x for x in range(1, 10)]
print(L)

g = (x * x for x in range(1, 10))
print(g.next())
print(g.next())
print(g.next())

# use generator in iteration
print('\n# use generator in iteration')
g = (x * x for x in range(1, 10))

for n in g:
    print(n)

# use yield to declare a generator
print('\n# use yield to declare a generator')


def gen(max):
    x = 1
    while x < max:
        yield x
        x += 1


g = gen(3)
try:
    print(g.next())
    print(g.next())
    print(g.next())
except Exception as error:
    pass
