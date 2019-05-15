# coding=utf-8

# internal functions
print('# internal functions')
rst = abs(-100)
print(rst)

rst = cmp(100, 20)
print(rst)

# type convert
print('# type convert')
print(int('100'))
print(int(100.5))
print(float(200))
print(bool(0))
print(isinstance(str(1000), str))
print(isinstance(1000, str))
print(unicode(100))
