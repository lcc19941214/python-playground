# coding=utf-8


# define function
def my_abs(num):
    if num >= 0:
        return num
    else:
        return -num


print(my_abs(1))
print(my_abs(-1))

# pass


def my_pass():
    pass


print(my_pass())
print(my_pass)
print(my_pass.__str__())

# param check


def my_param_check(num):
    if not isinstance(num, (int, float)):
        raise TypeError('not an integer or a float')
    else:
        print('num is: ' + num.__str__())


my_param_check(10)
my_param_check(10.0)
try:
    my_param_check('10')
except Exception as error:
    print(error.__str__())

# return multiple params


def my_multi_returns(a, b):
    return (b, a)


print(my_multi_returns(1, 2))
first, second = my_multi_returns('first', 'second')
print(first)
print(second)
