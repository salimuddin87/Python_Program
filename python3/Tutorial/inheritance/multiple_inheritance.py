class Parent1:

    def show(self):
        print("Inside Parent1")


class Parent2:

    def show(self):
        print("Inside Parent2")


class Parent3:

    def show(self):
        print("Inside Parent3")


class Child1(Parent1, Parent2, Parent3):

    def display(self):
        print("Inside Child1")


class Child2(Parent3, Parent2, Parent1):

    def display(self):
        print("Inside Child2")

if __name__ == '__main__':
    c1 = Child1()
    c1.show()
    c1.display()

    print("\n")
    c2 = Child2()
    c2.show()
    c2.display()
