# coding=utf-8

# filter
print('\n# filter')


def is_odd(num):
    return num % 2 == 1


L = range(1, 10)
print(filter(is_odd, L))

# get all prime number from 2 to 100


def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

L = range(1, 100)
print(filter(is_prime, L))
