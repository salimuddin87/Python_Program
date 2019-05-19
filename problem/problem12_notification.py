#!/bin/python

import math
import os
import random
import re
import sys

libPath = os.path.abspath(os.path.dirname(__file__)) + '../algorithm'
sys.path.append(libPath)

# Complete the activityNotifications function below.
from collections import deque

def countingSort(arr):
    
    l = min(arr)
    r = max(arr)
    Index = []
    Count = []
    # create index and count list
    for i in range(l, r+1):
        Index.append(i)
        Count.append(arr.count(i))
    print "index : ", Index
    print "count : ", Count

    # find count sum
    for i in range(1, len(Count)):
        Count[i] += Count[i-1]
    print "count_sum : ", Count

    # sort the array based on index
    sorted_arr = [0] * len(arr)
    for item in arr:
        j = Index.index(item)
        item_index = Count[j] - 1
        sorted_arr[item_index] = item
        Count[j] -= 1

    return sorted_arr

def findMedian(list2):
    #import pdb; pdb.set_trace()
    list1 = countingSort(list2)
    length = len(list1)
    if length / 2 == 0:
        mid = (list1[(length-1)/2] + list1[length/2]) / 2
    else:
        mid = list1[length/2]
    return mid

# queue implementation
def activityNotifications(exp, d):
    #import pdb; pdb.set_trace()
    queue = deque(exp[0:d])
    i = d
    notifyCount = 0
    while i < len(exp):

        median = findMedian(list(queue))
        if exp[i] >= (2*median):
            notifyCount += 1
        queue.append(exp[i])
        queue.popleft()
        i += 1
    return notifyCount

# array implementation
def notifications(expenditure, d):
    notifyCount = 0
    i = 0
    while (i+d) < len(expenditure):
        tempList = expenditure[i:i+d]
        #tempList.sort()

        median = findMedian(tempList)

        if expenditure[i+d] >= (2 * median):
            notifyCount += 1
        i += 1
    return notifyCount


if __name__ == '__main__':

    d = 3
    expenditure = [10,20,30,40,50]
    #expenditure = [2,3,4,2,3,6,8,4,5]
    #print notifications(expenditure, d)
    print activityNotifications(expenditure, d)

