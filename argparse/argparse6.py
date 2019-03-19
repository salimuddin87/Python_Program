"""
$ python prog.py --verbosity 1

$ python prog.py

$ python prog.py --help
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity:
    print "verbosity turned on!"

