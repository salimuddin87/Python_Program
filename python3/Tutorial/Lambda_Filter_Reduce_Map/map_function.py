"""
iter = map(function, sequence)
Map returns an iterator
"""


C = [39.2, 36.5, 37.3, 38, 37.8]
print(C)
print(type(C))

F = list(map(lambda x: (float(9)/5)*x + 32, C))
print(F)
print(type(F))

C = map(lambda x: (float(5)/9)*(x-32), F)
print(list(C))
print(type(C))

# map can be applied to more than one list
a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]
R = map(lambda x, y, z: x + y + z, a, b, c)
print(list(R))
print(type(R))

# If one list has fewer elements than the others, map will stop when the shortest list has been consumed
a = [1, 2, 3]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]
R = list(map(lambda x, y, z: x + y + z, a, b, c))
print(R)
