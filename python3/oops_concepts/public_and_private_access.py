"""
Naming		Type		Meaning
---------------------------------------------------------------------
1. name		Public 			These attributes can be freely used inside or outside of a class definition.

2. _name	Protected		Protected attributes should not be used outside of the class definition,
                            unless inside of a subclass definition.

3. __name	Private			This kind of attribute is inaccessible and invisible. It's neither possible
                            to read nor write to those attributes, except inside of the class definition itself.
"""


class A:
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"


if __name__ == '__main__':
    a = A()
    print(a.pub)
    print(a._prot)
    print(a._A__priv)  # private could be accessed
    print(a.__priv)  # But not this way

"""
Output:- 

I am public
I am protected
I am private
Traceback (most recent call last):
  File "privateAndPublic.py", line 26, in <module>
    print(a.__priv)
AttributeError: 'A' object has no attribute '__priv'
"""