"""
The last program accepts integer values for --verbosity, but only two values are actually useful, True OR False.


"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbosity", 
                    action="store_true")
args = parser.parse_args()
if args.verbose:
    print "verbosity turned on"

"""
New keyword, action is given a value "store_true".
which assign the value True to args.verbose.
Not specifying it implies False
"""
