#!:coding:utf-8

#abs(x)
#返回一个数的绝对值.该参数可以是整数或浮点数.如果参数是一个复数,则返回其大小
print abs(1)
print abs(-1)

#all(iterable)
#如果迭代器里面的任何元素都非零,返回True;否则返回False.
print all([-1,'   ',1])
print all([-1,0,1])
print all(['  '])
print all([''])

#any(iterable)
#如果迭代器里面的任意元素非零,返回True;否则返回False.
print any([1,'   ',False])
print any(['   '])
print any([False])
print any([''])
