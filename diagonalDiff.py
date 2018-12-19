#!/bin/python

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    #import pdb; pdb.set_trace()
    #Calculate left diagonal
    ld = 0
    for i in range(len(arr)):
        ld += arr[i][i]

    #calculate right diagonal
    rd = 0
    j = len(arr[0]) - 1
    for i in range(len(arr)):
        rd += arr[i][j]
        j -= 1

    return abs(ld - rd)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(arr)

    print result

    #fptr.write(str(result) + '\n')

    #fptr.close()
