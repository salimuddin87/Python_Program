"""
$ python prog.py 4
Traceback (most recent call last):
  File "prog.py", line 5, in <module>
    print args.square**2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
"""

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number")
args = parser.parse_args()
print args.square**2

"""
That didn’t go so well. That’s because argparse treats the options we give 
it as strings, unless we tell it otherwise. So, let’s tell argparse to 
treat that input as an integer
"""
