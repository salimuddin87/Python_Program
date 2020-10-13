"""
Function and method arguments:
    Always use self for the first argument to instance methods.
    Always use cls for the first argument to class methods.

If the created method is an instance method then the reserved word self has to be used,
but if the method is a class method then the keyword cls must be used.
"""
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_fullname(cls, fullname):
        cls.first_name, cls.last_name = fullname.split(' ', 1)
        return cls(cls.first_name, cls.last_name)


if __name__ == '__main__':
    person_obj = Person('salim', 'kabeer')
    print(person_obj.first_name, person_obj.last_name)

    class_obj = Person.from_fullname('salim kabeer')
    print(class_obj.first_name, class_obj.last_name)
