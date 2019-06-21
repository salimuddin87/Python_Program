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

times3 = make_multiplier_of(3)

times5 = make_multiplier_of(5)

print times3(5)
print times5(5)
print times5(times3(5))
