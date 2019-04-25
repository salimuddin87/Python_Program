# First decorator
def star(func):

    def inner(*args, **kwargs):
        print "*" * 50
        func(*args, **kwargs)
        print "*" * 50
    return inner

# 2nd decorator
def percent(func):
    
    def inner(*args, **kwargs):
        print "%" * 50
        func(*args, **kwargs)
        print "%" * 50
    return inner

@star
@percent
def printer(msg):
    print msg

printer("Hello, Salim")

# we can also write as
# printer = star(percent(printer))
"""
Output :-

**************************************************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Hello, Salim
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
**************************************************

"""
