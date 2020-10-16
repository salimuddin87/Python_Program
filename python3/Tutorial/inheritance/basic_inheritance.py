"""
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
"""


class Person:

    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def print_name(self):
        print(self.first_name + " " + self.last_name)


class Student(Person):

    def __init__(self, fname, lname, year):
        # To keep the inheritance of the parent's __init__()
        # Person.__init__(self, fname, lname)
        """
        Python also has a super() function that will make the child class inherit all the methods and
        properties from its parent. By using the super() function, you do not have to use the name of
        the parent element, it will automatically inherit the methods and properties from its parent.
        """
        super().__init__(fname, lname)
        self.graduation_year = year

    def welcome(self):
        print("Welcome ", self.first_name, self.last_name, " to the class of ", self.graduation_year)


if __name__ == '__main__':
    x = Person("John", "Doe")
    x.print_name()

    # y = Student("Mike", "Olsen")
    y = Student("Mike", "Olsen", "2020")
    y.print_name()

    z = Student("salim", "kabeer", "2015")
    z.print_name()
    z.welcome()
