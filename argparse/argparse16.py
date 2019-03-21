"""
$ python prog.py 4 2
16
$ python prog.py 4 2 -v
4^2 == 16
$ python prog.py 4 2 -vv
Running 'prog.py'
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
    print 'Running program \'{}\''.format(__file__)
if args.verbose >= 1:
    print '{} to the power {} == '.format(args.x, args.y)
print answer
