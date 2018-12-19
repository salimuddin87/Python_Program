#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    min = 0
    for i in range(len(q)):
        print "%d iteration" % (i+1)
        if (i+1) != q[i]:
            print "element moved"
            j = q.index(i+1)
            print "j index %d" % (j+1)
            if j < i: 
                print "element bribed"
                if (i - j) > 2:
                    print "Too chaotic"
                    return 0
                min = min + (i - j)
        print min
    return q

if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        result = minimumBribes(q)
        if result != 0:
            print result

