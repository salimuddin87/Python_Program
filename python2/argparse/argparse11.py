"""
$ python prog.py 4 -v 3
usage: prog.py [-h] [-v {0,1,2}] square
prog.py: error: argument -v/--verbosity: invalid choice: 3 (choose from 0, 1, 2)
$ python prog.py 4 -h
usage: prog.py [-h] [-v {0,1,2}] square

positional arguments:
  square                display a square of a given number

optional arguments:
  -h, --help            show this help message and exit
  -v {0,1,2}, --verbosity {0,1,2}
                        increase output verbosity
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('square', type=int,
                   help='display a square of a given number')
parser.add_argument('-v', '--verbose', type=int, choices=[0,1,2],
                   help='increase output verbosity')

args = parser.parse_args()
answer = args.square ** 2

if args.verbose == 2:
    print 'The square of {} equals {}'.format(args.square, answer)
elif args.verbose == 1:
    print '{}^2 == {}'.format(args.square, answer)
else:
    print answer
