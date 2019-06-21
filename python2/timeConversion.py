#!/bin/python

#from __future__ import print_function

import os
import sys
import re

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    # 07:05:45PM
    timeList = re.split('(\d+)', s)
    time = ""
    if 'PM' in timeList or 'pm' in timeList:
        if timeList[1] != '12':
            timeList[1] = str(int(timeList[1]) + 12)

    if 'AM' in timeList or 'am' in timeList:
        if timeList[1] == '12':
            timeList[1] = '00'
    
    for item in timeList[:-1]:
        time = time + item

    return time

if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = timeConversion(s)

    #f.write(result + '\n')

    print result

    #f.close()
