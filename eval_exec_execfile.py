#!:coding:utf-8

#eval(str [,globals [,locals ]])
#函数将字符串str当成有效Python表达式来求值，并返回计算结果。
print eval('1+2+3')
x = 1
print eval('x+2+3')


#exec(object[, globals[, locals]])
#将字符串str当成有效Python代码来执行。
exec('print("I Love FishC.com !!!")')
exec('x = 520')
print x

#execfile(filename [,globals [,locals ]])
#函数可以用来执行一个文件。
