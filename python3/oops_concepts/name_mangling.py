"""
“Private” instance variables that cannot be accessed except from inside an
object don’t exist in Python. However, there is a convention that is followed
by most Python code: a name prefixed with an underscore (e.g. _spam) should
be treated as a non-public part of the API (whether it is a function, a method
or a data member).

Mangling:- Any identifier of the form __spam (at least two leading underscores,
at most one trailing underscore) is textually replaced with _classname__spam,
where classname is the current class name with leading underscore(s) stripped.

Name mangling is helpful for letting subclasses override methods without
breaking intraclass method calls. For example:

"""
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method


class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

"""
The above example would work even if MappingSubclass were to introduce a __update
 identifier since it is replaced with _Mapping__update in the Mapping class and 
 _MappingSubclass__update in the MappingSubclass class respectively.

Note that the mangling rules are designed mostly to avoid accidents; it still is 
possible to access or modify a variable that is considered private. This can even
be useful in special circumstances, such as in the debugger.

"""
class Test:
    def __init__(self):
        self.foo = 10
        self._bar = 20  # Hint to use it as a private variable
        self.__baz = 30  # Name mangling is used

if __name__ == '__main__':
    t = Test()
    # ['_Test__baz', '__doc__', '__init__', '__module__', '_bar', 'foo']
    print(dir(t))

    print("t.foo : ", t.foo)
    print("t._bar : ", t._bar)
    print("t._Test__baz : ", t._Test__baz)