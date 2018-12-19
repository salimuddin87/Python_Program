#!/bin/python

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    #import pdb; pdb.set_trace()
    #cost.sort() 
    
    for i in range(len(cost)):
        for j in range(1, len(cost)):
            if (cost[i] + cost[j]) == money:
                print i+1, j+1
                return
            continue
    print "No Solution"
    return


if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        money = int(raw_input())

        n = int(raw_input())

        cost = map(int, raw_input().rstrip().split())

        whatFlavors(cost, money)
