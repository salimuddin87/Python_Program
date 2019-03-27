"""
The try-except statement has an optional else clause, which, when present, 
must follow all except clauses. It is useful for code that must be executed 
if the try clause does not raise an exception.

"""

import sys

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print "cannot open", arg
    else: 
        # must be executed if try does not raise an exception
        print arg, 'has', len(f.readlines()), 'lines'
        f.close()
