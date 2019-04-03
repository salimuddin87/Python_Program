import datetime

class Human(object):
    name = None
    gender = None
    birthdate = None

    def __getattr__(self, name):
        if name == 'age':
            return datetime.datetime.now() - self.birthdate
        else:
            return None

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

h = Human()
h.birthdate = datetime.datetime(1987, 3, 14)
h.age = 32

print h.age
