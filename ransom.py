import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
     
    for i in range(len(note)):
        if note[i] not in magazine[i:]:
            print "No"
            return
    print "Yes"
    return


if __name__ == '__main__':
    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = raw_input().rstrip().split()

    note = raw_input().rstrip().split()
    """
    m = 6; n=4
    magazine = "give me one grand today night"
    note = "give one grand today"
    """
    checkMagazine(magazine, note)
