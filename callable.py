#!:coding:utf-8

#callable（object）
#检查对象object是否可调用。如果返回True，object仍然可能调用失败；但如果返回False，调用对象ojbect绝对不会成功。

print callable([1,'2',3.0])
def FishC():
    pass
print callable(FishC)

class AA:
    pass

print '类是否可调用:'
print callable(AA)
print '实例是否可调用:'
aa = AA()
print callable(aa)

class BB:
    def __call__(self):
        pass

print '类是否可调用:'
print callable(BB)
bb = BB()
print '实例是否可调用:'
print callable(bb)
