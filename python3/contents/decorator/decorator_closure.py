"""
The criteria to create closure in python are
    1. We must have nested function
    2. Nested function must refer to a value defined in the enclosing(outer) function
    3. Enclosing/Outer function must return nested function.

closure provides some form of data hiding.
when few methods to be implemented in a class,
closure can provide an alternative.

"""

def make_multiplier_of(n):
    def multiplier(x):
        return x * n

    return multiplier


def print_msg(msg):

    def printer():
        print(msg)

    return printer


if __name__ == '__main__':
    print("Multiplier example for closure!")
    times3 = make_multiplier_of(3)
    times5 = make_multiplier_of(5)

    print("3 times 5: ",times3(5))
    print("5 times 5: ",times5(5))
    print("5 times 3 times 5: ",times5(times3(5)))

    print("\n Print msg example for closure!")
    another = print_msg('Hello, salim')
    print("call to another function")
    another()
    # the msg is still remembered although we has finished executing print_msg
    # The technique by which data 'Hello, salim' gets attached to the code is called closure
    del print_msg  # After deleting function
    print("call to another function")
    another()  # Still, we can see that another() contain msg

    print("After deleting print_msg!")
    print_msg('Hello, salim')
