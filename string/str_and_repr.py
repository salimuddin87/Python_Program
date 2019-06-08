import datetime

# Python has ways to convert any value to a string: pass it to the repr() or str() functions.

# The str() function is meant to return representations of values which are fairly human-readable, 
# while repr() is meant to generate representations which can be read by the interpreter (or will 
# force a SyntaxError if there is no equivalent syntax).

today = datetime.datetime.now()
s = "Hello, Salim"

print "str(s) : ", str(s) # Do not print quote 
print "str(2.0/11.0) : ", str(2.0/11.0) # Use __str__() method to display
print "str(today) : ", str(today) # Human readable output

print "*" * 50

print "repr(s) : ", repr(s) # print quote to show it's string
print "repr(2.0/11.0) : ", repr(2.0/11.0) # gives more precise value to debug
print "repr(today) : ", repr(today) # use __repr__() method to display
