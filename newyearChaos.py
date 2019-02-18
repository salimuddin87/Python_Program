#!/bin/python

import math
import os
import random
import re
import sys

def minimumBribes(q):
    print "Queue : {}".format(q)

    minBribe = 0
    lenq = len(q)
    moves = 0
    for i in range(0, lenq):
        moves = q[i] - (i+1)
        if moves > 2:
            print "Too chaotic"
            return

    for i in range(0, lenq):
        swapped = False
        for j in range(1, lenq-i):
            if q[j-1] > q[j]:
                temp = q[j]
                q[j] = q[j-1]
                q[j-1] = temp
                minBribe += 1
                swapped = True
        if swapped == False:
            break

    print minBribe
    return


if __name__ == '__main__':
    t = int(raw_input('How many times: '))
    
    for i in range(t):
        n = int(raw_input('How many persons: '))

        q = map(int, raw_input('Enter position queue list: '))
        
        minimumBribes(q)
