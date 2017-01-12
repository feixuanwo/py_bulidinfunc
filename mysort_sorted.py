#!:coding:utf-8

#sorted(iterable, key=None, reverse=False) --> new sorted list
#返回将迭代器中的元素排序的新列表。

#sorted与sort不同。前者是内置函数，后者是列表、字典的方法；前者返回一个新列表。

i = [x for x in range(-5,6)]
print sorted(i)
print sorted(i,reverse=True)
print i
print i.sort(reverse=True)
print i
