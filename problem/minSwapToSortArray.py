#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    print arr
    minSwap = 0
    index = range(1, len(arr)+1)
    for i in range(0, len(arr)):
        for j in range(i, len(index)):
            if arr[i] == index[j] and i != j:
                temp = index[i]
                index[i] = index[j]
                index[j] = temp
                minSwap += 1

    return minSwap

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input("\n Enter size of array : "))

    arr = map(int, raw_input("\nEnter array elements : ").rstrip().split())

    res = minimumSwaps(arr)

    #fptr.write(str(res) + '\n')
    #fptr.close()
    print "Min swaps : ", res
