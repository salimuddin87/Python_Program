"""
The difference between shallow and deep copying is only relevant for compound objects
(objects that contain other objects, like lists or class instances):

A shallow copy constructs a new compound object and then (to the extent possible)
	inserts references into it to the objects found in the original.

A deep copy constructs a new compound object and then, recursively, inserts copies
	into it of the objects found in the original.
"""

>>> a = [1,3,2,[1,2],5]
>>> b = a (by default shallow copy)
>>> b
[1, 3, 2, [1, 2], 5]
>>> b[3].append(3)
>>> b  (pointing to same object)
[1, 3, 2, [1, 2, 3], 5]
>>> a
[1, 3, 2, [1, 2, 3], 5]

>>> import copy
>>> c = copy.deepcopy(a)
>>> c
[1, 3, 2, [1, 2, 3], 5]
>>> c.append(6)
>>> c
[1, 3, 2, [1, 2, 3], 5, 6]
>>> a
[1, 3, 2, [1, 2, 3], 5]
>>> c[3].append(4)
>>> c
[1, 3, 2, [1, 2, 3, 4], 5, 6]
>>> a
[1, 3, 2, [1, 2, 3], 5]
>>>
>>>
>>>
>>> d = copy.copy(a)
>>> d
[1, 3, 2, [1, 2, 3], 5]
>>> d.append(6)
>>> d
[1, 3, 2, [1, 2, 3], 5, 6]
>>> a
[1, 3, 2, [1, 2, 3], 5]
>>> d[3].append(4)
>>> d
[1, 3, 2, [1, 2, 3, 4], 5, 6]
>>> a
[1, 3, 2, [1, 2, 3, 4], 5]

