class Test:
    def __init__(self):
        self.foo = 10
        self._bar = 20 # Hint to use it as a private variable
        self.__baz = 30 # Name mangling is used

t = Test()
# ['_Test__baz', '__doc__', '__init__', '__module__', '_bar', 'foo']
print dir(t)

print "t.foo : ", t.foo
print "t._bar : ", t._bar
# print "t._baz : ", t.__baz
print "t._Test__baz : ", t._Test__baz
