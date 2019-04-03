class Employee:
    pass

john = Employee()

john.name = 'John Doe'
john.dept = 'computer labs'
john.salary = 1000

print "length of obj is : ", len(john.__dict__)
print john.__dict__
