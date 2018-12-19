#!/bin/python

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    count = 0
    a1 = list(a)
    b1 = list(b)
    print a1,b1
    #import pdb; pdb.set_trace()
    for i in range(len(a)):
        temp = a[i]
        if temp not in b1:
            count += 1
        if temp in b1:
            a1.remove(temp)
            b1.remove(temp)
    for j in range(len(b)):
        temp = b[j]
        if temp not in a1:
            count +=1
        if temp in a1:
            a1.remove(temp)
            #b1.remove(temp)
    print "Anagram"
    print a1,b1
    return count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = raw_input()

    b = raw_input()

    res = makeAnagram(a, b)

    #fptr.write(str(res) + '\n')

    #fptr.close()
