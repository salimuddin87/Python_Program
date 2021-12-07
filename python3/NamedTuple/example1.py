"""
>>> from collections import namedtuple

>>> # Create a namedtuple type, Point
>>> Point = namedtuple("Point", "x y")
>>> issubclass(Point, tuple)
True

>>> # Instantiate the new type
>>> point = Point(2, 4)
>>> point
Point(x=2, y=4)

>>> # Dot notation to access coordinates
>>> point.x
2
>>> point.y
4

>>> # Indexing to access coordinates
>>> point[0]
2
>>> point[1]
4

>>> # Named tuples are immutable
>>> point.x = 100
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: can't set attribute

#####################################################
>>> Person = namedtuple("Person", "name children")
>>> john = Person("John Doe", ["Timmy", "Jimmy"])
>>> john
Person(name='John Doe', children=['Timmy', 'Jimmy'])
>>> id(john.children)
139695902374144

>>> john.children.append("Tina")
>>> john
Person(name='John Doe', children=['Timmy', 'Jimmy', 'Tina'])
>>> id(john.children)
139695902374144

>>> hash(john)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'

# To illustrate how to provide field_names, here are different ways to create points:
>>> # A list of strings for the field names
>>> Point = namedtuple("Point", ["x", "y"])
>>> Point
<class '__main__.Point'>
>>> Point(2, 4)
Point(x=2, y=4)

>>> # A string with comma-separated field names
>>> Point = namedtuple("Point", "x, y")
>>> Point
<class '__main__.Point'>
>>> Point(4, 8)
Point(x=4, y=8)

>>> # A generator expression for the field names
>>> Point = namedtuple("Point", (field for field in "xy"))
>>> Point
<class '__main__.Point'>
>>> Point(8, 16)
Point(x=8, y=16)
"""