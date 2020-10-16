"""
python does not supports method overloading by default. But there are different ways to achieve method
overloading in Python.
"""


class Student:

    def add(self, datatype, *args):
        if datatype == 'int':
            answer = 0

        if datatype == 'str':
            answer = ''

        for x in args:
            answer += x

        print("Answer = ", answer)

    def hello_function(self, name=None):
        if name is not None:
            print("Hello " + name)
        else:
            print("Hello")


def product(a, b):
    print("First product", a * b)


def product(a, b, c=1):
    print("Second product", a * b * c)


if __name__ == '__main__':
    std = Student()
    std.hello_function()
    std.hello_function("Nick")

    # Operator overloading
    print(5 + 5)
    print("py" + "thon")

    product(4, 5)  # Always 2nd function will be called

    std.add('int', 5, 6)
    std.add('str', 'Hi', 'Salim')
