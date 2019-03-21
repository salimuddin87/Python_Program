"""
$ python prog.py
usage: prog.py [-h] [-v] x y
prog.py: error: the following arguments are required: x, y
$ python prog.py -h
usage: prog.py [-h] [-v] x y

positional arguments:
  x                the base
  y                the exponent

optional arguments:
  -h, --help       show this help message and exit
  -v, --verbosity
$ python prog.py 4 2 -v
4^2 == 16

"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('x', type=int, help='The base')
parser.add_argument('y', type=int, help='The exponent')
parser.add_argument('-v', '--verbose', action='count', default=0)

args = parser.parse_args()
answer = args.x ** args.y

if args.verbose >= 2:
    print '{} to the power {} equals {}'.format(args.x, args.y, answer)
elif args.verbose >= 1:
    print '{} ^ {} == {}'.format(args.x, args.y, answer)
else:
    print answer

