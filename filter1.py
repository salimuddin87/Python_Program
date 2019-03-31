"""
filter(function, sequence) returns a sequence consisting of those items from 
the sequence for which function(item) is true. If sequence is a str, unicode
or tuple, the result will be of the same type; otherwise, it is always a list.

"""
def f(x):
    return x % 3 == 0 or x % 5 == 0

res = filter(f, range(2, 25))

print res
