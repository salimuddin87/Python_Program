# Integer set
my_set = {1,2,3,4}
print my_set

# Mixed datatypes
my_set = {1.0, 'Hello', (1,2,3), 5}
print my_set

# set from a list
list1 = [1,2,3,1,4]
print set(list1)

# initialize a set
tempSet = set()

# add and update in a set
my_set = {1, 3}
my_set.add(2)
print "my_set : ", my_set

my_set.update([2,3,4])
print "my_set : ", my_set

my_set.update([4,5], {6,7,8})
print "my_set : ", my_set

# The only difference between the two is that, while using discard() 
# if the item does not exist in the set, it remains unchanged. But 
# remove() will raise an error in such condition.
my_set.discard(4)
my_set.remove(6)
print "my_set : ", my_set

# pop and clear from a set
my_set1 = set("HelloWorld")
print "pop from a set : ", my_set1.pop() # pop a random elements
print "my_set1.clear() : ", my_set1.clear()

print "###################### Set Operation ###########################"
A = {1,2,3,4,5,8}
B = {4,5,6,7,8,2}

print "Union of A | B : ", A | B
print "A.union(B) : ", A.union(B)

print "Intersection of A & B : ", A & B
print "A.intersection(B) : ", A.intersection(B)

print "set difference of A - B : ", A - B
print "A.difference(B) : ", A.difference(B)

print "Symmetric Difference A ^ B : ", A ^ B
print "A.symmetric_difference(B) : ", A.symmetric_difference(B)

