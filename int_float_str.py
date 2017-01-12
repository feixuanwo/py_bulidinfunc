#!:coding:utf-8

#int(x)
#int(x,base=10)
#把一个数、字符串转化成整形。如果为空，返回0；如果是数，返回x.__int__()；如果是浮点数，取整数部分；
#如果给出base，依据base返回对应值。
print int()
print int(0.9)
print int('0xff',base=16)
print int('0o377',base=8)
print int('0b11111111',base=2)


#float(x)
#把字符串或者一个数转化成浮点数。
print float(1)
print float('+1.23')
print float('   -12345\n')
print float('+1E6')
print float('-Infinity')
print float('1e-003')


#str(x)
#把数转化成字符串。
print str(5)
print str('   FishC')
