def print_msg(msg):

    def printer():
        print msg

    return printer

another = print_msg('Hello, salim')
another() # the msg is still remembered although we has finished executing print_msg
# The technique by which data 'Hello, salim' gets attached to the code is called closure

#########################################################
del print_msg
another()
print_msg('Hello, salim')
