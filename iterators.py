
# The use of iterators pervades and unifies Python. Behind the scenes, 
# the for statement calls iter() on the container object. The function 
# returns an iterator object that defines the method next() which accesses 
# elements in the container one at a time. When there are no more elements, 
# next() raises a StopIteration exception which tells the for loop to terminate. 
# This example shows how it all works:

>>> s = 'abc'
>>> it = iter(s)
>>> it
<iterator object at 0x00A1DB50>
>>> it.next()
'a'
>>> it.next()
'b'
>>> it.next()
'c'
>>> it.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    it.next()
StopIteration

Adding __iter__() method in class
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print char
...
m
a
p
s

