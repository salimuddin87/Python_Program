"""
A metaclass is a class whose instances are classes.

There are numerous use cases for metaclasses:
	1. logging and profiling
	2. interface checking
	3. registering classes at creation time
	4. automatically adding new methods
	5. automatic property creation
	6. proxies
	7. automatic resource locking/synchronization.
"""

class LittleMeta(type):
    def __new__(cls, clsname, superclasses, attributedict):
        print("clsname: ", clsname)
        print("superclasses: ", superclasses)
        print("attributedict: ", attributedict)
        return type.__new__(cls, clsname, superclasses, attributedict)

class S:
    pass
class A(S, metaclass=LittleMeta):
    pass
a = A()
