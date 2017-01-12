#!:coding:utf-8

#chr(integer)
#把整数转化成对应的字母.
print chr(97)
print chr(65)

#ord(str)
#把对应的字符转成整数.
print ord('A')
print ord('a')

#bool(x)
#把一个值转化为布尔值,如果该值为假或者省略返回False,否则返回True.
tmp = [False,None,0,0.0,'',(),[],{},1,' ']
for i in tmp:
    print(bool(i))
