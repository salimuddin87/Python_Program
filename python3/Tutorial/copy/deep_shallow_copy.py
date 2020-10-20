"""
The difference between shallow and deep copying is only relevant for compound objects
(objects that contain other objects, like lists or class instances):

A shallow copy constructs a new compound object and then (to the extent possible)
    inserts references into it to the objects found in the original.

A deep copy constructs a new compound object and then, recursively, inserts copies
    into it of the objects found in the original.
"""
import copy


if __name__ == '__main__':
    a = [1, 3, 2, [1, 2], 5]
    b = a  # by default shallow copy i.e. [1, 3, 2, [1, 2], 5]
    b[3].append(3)
    print(b)  # pointing to same object i.e. [1, 3, 2, [1, 2, 3], 5]
    print(a)  # [1, 3, 2, [1, 2, 3], 5]

    c = copy.deepcopy(a)
    print(c)  # [1, 3, 2, [1, 2, 3], 5]

    c.append(6)
    print(c)  # [1, 3, 2, [1, 2, 3], 5, 6]
    print(a)  # [1, 3, 2, [1, 2, 3], 5]

    c[3].append(4)
    print(c)  # [1, 3, 2, [1, 2, 3, 4], 5, 6]
    print(a)  # [1, 3, 2, [1, 2, 3], 5]

    d = copy.copy(a)
    print(d)  # [1, 3, 2, [1, 2, 3], 5]

    d.append(6)
    print(d)  # [1, 3, 2, [1, 2, 3], 5, 6]
    print(a)  # [1, 3, 2, [1, 2, 3], 5]

    d[3].append(4)
    print(d)  # [1, 3, 2, [1, 2, 3, 4], 5, 6]
    print(a)  # [1, 3, 2, [1, 2, 3, 4], 5]
