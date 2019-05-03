
"""
List Comprehensions

"""
squares = []
for x in range(10):
    squares.append(x**2)
print squares

squares1 = [x**2 for x in range(10)]
print squares1

squares2 = map(lambda x: x**2, range(10))
print squares2

# ------------------------------------------------------
list1 = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print list1

list2 =[]
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            list2.append((x,y)) # must be parenthesized
print list2

#------------------------------------------------------
vec = [-4, -2, 0, 2, 4]

print [x*2 for x in vec]

print [x for x in vec if x >=0]

print [abs(x) for x in vec]

print [(x, x**2) for x in range(10)]

#------------------------------------------------------

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]

trsp = [[row[i] for row in matrix] for i in range(4)]
print "Transpose : ", trsp


transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print "Transpose : ",transposed
