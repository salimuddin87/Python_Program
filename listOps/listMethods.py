>>> print "List Methods"
List Methods
>>> a = [0,1,2,3]
>>> a.append(4)
>>> a
[0, 1, 2, 3, 4]
>>> b = [5,6]
>>> a.extend(b)
>>> a
[0, 1, 2, 3, 4, 5, 6]
>>> a.insert(3,10)
>>> a
[0, 1, 2, 10, 3, 4, 5, 6]
>>> a.append(10)
>>> a
[0, 1, 2, 10, 3, 4, 5, 6, 10]
>>> a.remove(10) # Removes first item which is 10
>>> a
[0, 1, 2, 3, 4, 5, 6, 10]
>>> a.pop()
10
>>> a
[0, 1, 2, 3, 4, 5, 6]
>>> a.pop(4)
4
>>> a.index(4) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 4 is not in list
>>> a.index(3)
3
>>> a.extend([1,4,2,5,1,1])
>>> a
[0, 1, 2, 3, 5, 6, 1, 4, 2, 5, 1, 1]
>>> a.count(1)
4
>>> a.sort()
>>> a
[0, 1, 1, 1, 1, 2, 2, 3, 4, 5, 5, 6]
>>> a.reverse()
>>> a
[6, 5, 5, 4, 3, 2, 2, 1, 1, 1, 1, 0]
