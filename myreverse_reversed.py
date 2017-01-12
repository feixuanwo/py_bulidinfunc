#!:coding:utf-8

#reversed与reverse不同。前者是内置函数，后者是列表、字典的方法。前者返回一个新列表。
i = [x for x in range(-5,6)]
for x in reversed(i):
    print x,

print
print i
print i.reverse()
print i
