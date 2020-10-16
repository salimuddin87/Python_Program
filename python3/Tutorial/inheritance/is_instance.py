class A:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi, I am " + self.name)


class B(A):
    pass


class C(B):
    pass


if __name__ == '__main__':
    x = A("Marvin")
    y = B("James")
    z = C("salim")

    print("x = {} and type(x) = {}".format(x, type(x)))
    print("y = {} and type(y) = {}".format(y, type(y)))
    y.say_hi()

    print(isinstance(x, A), isinstance(y, A))
    print(isinstance(x, B), isinstance(y, B))

    print(type(y) == A, type(y) == B)
    print(isinstance(z, A))