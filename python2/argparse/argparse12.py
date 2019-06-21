"""
$ python prog.py 4
16
$ python prog.py 4 -v
4^2 == 16
$ python prog.py 4 -vv
the square of 4 equals 16
$ python prog.py 4 --verbosity --verbosity
the square of 4 equals 16
$ python prog.py 4 -v 1
usage: prog.py [-h] [-v] square
prog.py: error: unrecognized arguments: 1
$ python prog.py 4 -h
usage: prog.py [-h] [-v] square

positional arguments:
  square           display a square of a given number

optional arguments:
  -h, --help       show this help message and exit
  -v, --verbosity  increase output verbosity
$ python prog.py 4 -vvv
16
"""

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                   help="display the square of a given number")
parser.add_argument('-v', '--verbose', action='count',
                   help='increase output verbosity')

args = parser.parse_args()
answer = args.square ** 2

if args.verbose == 2:
    print "the square of {} equals {}".format(args.square, answer)
elif args.verbose == 1:
    print "{}^2 == {}".format(args.square, answer)
else:
    print answer
