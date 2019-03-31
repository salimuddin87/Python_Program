"""
reduce(function, sequence) returns a single value constructed by calling the
binary function function on the first two items of the sequence, then on the
result and the next item, and so on

"""

def add(x, y): return x+y

res = reduce(add, range(1,11))

print res
