"""
$ python prog.py
usage: prog.py [-h] [-v] square
prog.py: error: the following arguments are required: square
$ python prog.py 4
16
$ python prog.py 4 --verbose
the square of 4 equals 16
$ python prog.py --verbose 4
the square of 4 equals 16
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, 
                    help="display square of a given number")
parser.add_argument('-v', '--verbose', action='store_true',
                   help='increase output verbosity')
args = parser.parse_args()
answer = args.square**2

if args.verbose:
    print "The square of {} equals {}".format(args.square, answer)
else:
    print answer
