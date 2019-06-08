class Employee:
    pass

john = Employee()

john.name = 'John Doe'
john.dept = 'computer labs'
john.salary = 1000

# length of obj is :  3
# {'salary': 1000, 'dept': 'computer labs', 'name': 'John Doe'}

print "length of obj is : ", len(john.__dict__)
print john.__dict__
