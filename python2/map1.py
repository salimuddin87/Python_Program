"""
map(function, sequence) calls function(item) for each of the sequence's items
and returns a list of the return values. For example, to compute some cubes:

"""

def cube(x): return x*x*x

res = map(cube, range(1, 11))

print res
