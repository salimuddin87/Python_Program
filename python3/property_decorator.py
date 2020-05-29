
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # 2 self.email = first + '.' + last + '@email.com'
    
    # 2 changes
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp_1 = Employee('salim', 'kabeer')

emp_1.first = 'Guddu' # 1 changes

print(emp_1.first)
# 2 print(emp_1.email())
print(emp_1.email)
print(emp_1.fullname)

print('#' * 20)

emp_1.fullname = 'salimuddin ansari'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname