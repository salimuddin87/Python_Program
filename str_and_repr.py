import datetime


today = datetime.datetime.now()
s = "Hello, Salim"

print "str(s) : ", str(s) # Do not print quote 
print "str(2.0/11.0) : ", str(2.0/11.0) # Use __str__() method to display
print "str(today) : ", str(today) # Human readable output

print "*" * 50

print "repr(s) : ", repr(s) # print quote to show it's string
print "repr(2.0/11.0) : ", repr(2.0/11.0) # gives more precise value to debug
print "repr(today) : ", repr(today) # use __repr__() method to display
