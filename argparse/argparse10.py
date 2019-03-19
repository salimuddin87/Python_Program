"""
$ python prog.py 4
16
$ python prog.py 4 -v
usage: prog.py [-h] [-v VERBOSITY] square
prog.py: error: argument -v/--verbosity: expected one argument
$ python prog.py 4 -v 1
4^2 == 16
$ python prog.py 4 -v 2
the square of 4 equals 16
$ python prog.py 4 -v 3
16
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('square', type=int,
                   help='display a square of given number')
parser.add_argument('-v', '--verbose', type=int,
                   help='increase output verbosity')
args = parser.parse_args()
answer = args.square ** 2

if args.verbose == 2:
    print "the square of {} equals {}".format(args.square, answer)
elif args.verbose == 1:
    print "{}^2 == {}".format(args.square, answer)
else:
    print answer
