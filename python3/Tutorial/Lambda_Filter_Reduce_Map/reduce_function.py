"""
reduce() had been dropped from the core of Python when migrating to Python 3.
The function
        reduce(func, seq)

continually applies the function func() to the sequence seq. It returns a single value.
"""


from functools import reduce


print(reduce(lambda x, y: x + y, range(0, 6)))
