# -*- coding: utf-8 -*-

print 100
print '100'
print 'hello'
print '你好'
print u'你好'.encode('utf8')
print 'line 1\nline 2'
print r'line 1\n line 2'

# method `u` means to describe an unicode symbol
# method `r` means not to excape the code

# ASCII
print ord('A')
print chr(65)

# length of string
print len('abc')    # 3
print len(u'abc')   # 3
print len(u'中文')  # 2
print len('\xe4\xb8\xad\xe6\x96\x87') # 6

# encode & decode
print 'abc'.encode('utf-8') # 'abc
print 'abc'.decode('utf-8')
print u'中文'.encode('utf-8') # '\xe4\xb8\xad\xe6\x96\x87'
