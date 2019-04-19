class Test:
    def __init__(self):
        self.foo = 10
        self._bar = 20 (Hint to use it as a private variable)
        self.__baz = 30 (Name mangling is used)

t = Test()
dir(t)
