# coding=utf-8

# condition
age = 18
if age > 18:
    print('you are an adult')
else:
    print('you are not an adult')

time = 15
if time > 6 and time <= 12:
    print('good morning')
elif time > 12 and time <= 18:
    print('good afternoon')
elif time > 18:
    print('good night')
else:
    print('good night')

# shorthand
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
x = 'hello'
if x:
    print 'hello'
x = []
if not x:
    print 'world'

# num = raw_input('please enter a number: ')
# if int(num) > 50:
#   print('num is greater than 50')
# else:
#   print('num is less than 50')
