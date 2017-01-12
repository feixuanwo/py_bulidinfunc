#!:coding:utf-8

#enumerate()是python的内置函数
#enumerate在字典上是枚举、列举的意思
#对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
#enumerate多用于在for循环中得到计数
list1 = ["这", "是", "一个", "测试"]
for i in range (len(list1)):
    print i ,list1[i]

list1 = ["这", "是", "一个", "测试"]
for index, item in enumerate(list1):
    print index, item


#enumerate还可以接收第二个参数，用于指定索引起始值，如：
list1 = ["这", "是", "一个", "测试"]
for index, item in enumerate(list1, 1):
    print index, item

#元组
for i,j in enumerate(('a','b','c')):
    print(i,j)
#列表
for i,j in enumerate([1,2,3]):
    print(i,j)
#字符串
for i,j in enumerate('abc'):
    print(i,j)
#字典
for i,j in enumerate({'a':1,'b':2}):
    print(i,j)

#如果要统计文件的行数，可以这样写：
#count = len(open(filepath, 'r').readlines())
#这种方法简单，但是可能比较慢，当文件比较大时甚至不能工作。
#可以利用enumerate()：
#count = -1 
#for index, line in enumerate(open(filepath,'r'))： 
#    count += 1
