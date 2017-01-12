
#map(func, *iterables) --> map object
#Make an iterator that computes the function using arguments from
#each of the iterables.  Stops when the shortest iterable is exhausted.
def f(x):
    return x*x

print list(map(f,[1,2,3,4,5,6]))
print list(map(str,[1,2,3,4,5,6]))


#reduce(...)
#reduce(function, sequence[, initial]) -> value
#Apply a function of two arguments cumulatively to the items of a sequence,
#from left to right, so as to reduce the sequence to a single value.
#For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
#((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
#of the sequence in the calculation, and serves as a default when the
#sequence is empty.


from functools import reduce
def ad(x,y):
    return x + y

print reduce(ad, [1, 3, 5, 7, 9])
