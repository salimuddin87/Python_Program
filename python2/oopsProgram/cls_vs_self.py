class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @classmethod
    def from_fullname(cls, fullname):
        cls.firstname, cls.lastname = fullname.split(' ', 1)

"""
Function and method arguments:

Always use self for the first argument to instance methods.

Always use cls for the first argument to class methods.
"""