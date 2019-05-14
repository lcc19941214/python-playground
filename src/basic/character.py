# coding=utf-8

# Normal Input
print(100)
print(3.1415926897)
print('100')
print('hello')
print('你好')
print(u'你好'.encode('utf8'))
print('line 1\nline 2')
print(r'line 1\n line 2')

# method `u` means to describe an unicode symbol
# method `r` means not to excape the code

# ASCII
print(ord('A'))
print(chr(65))

# length of string
print(len('abc'))  # 3
print(len(u'abc'))  # 3
print(len(u'中文'))  # 2
print(len('\xe4\xb8\xad\xe6\x96\x87'))  # 6

# encode & decode
print('abc'.encode('utf-8'))  # 'abc
print('abc'.decode('utf-8'))
print(u'中文'.encode('utf-8'))  # '\xe4\xb8\xad\xe6\x96\x87'

# format with placeholder
# %s string this will always work
# %d digit 是否在数字前面padStart：%xnd x代表需要pad的字符，可以省略，默认补充空格；n代表字符总长度
# %f float 小数点后位数： %.nf n 代表需要显示的长度，默认6个
# %x 16 radix
print('hello %s' % 'world')
print('%s is now %d year\'s old' % ('Lily', 25))
print('PI is start with %f(with default to 6 digit)' % (3.141592653897))
print('PI is start with %.10f(with up to 10 digit)' % (3.141592653897))
print('The constant E is start with %d' % (2.71828))
print('Success Rate: %s%%' % 7.5)
print('My favorite movie is %03d' % 7)  # 007
