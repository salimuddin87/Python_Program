"""
The method in the subclass is said to override the method in the super-class.
"""


class Parent:

    def __init__(self):
        self.value = "Inside Parent Class"

    def show(self):
        print(self.value)


class Child(Parent):

    def __init__(self):
        self.value = "Inside Child Class"

    def show(self):
        print(self.value)


if __name__ == '__main__':
    p = Parent()
    c = Child()

    p.show()
    c.show()
