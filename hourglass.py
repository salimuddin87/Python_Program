#!/usr/local/bin/python

def hourglass(arr):
    """ 
    0 -4 -6 0 -7 -6
    -1 -2 -6 -8 -3 -1
    -8 -4 -2 -8 -8 -6
    -3 -1 -2 -5 -7 -4
    -3 -5 -3 -6 -6 -6
    -3 -6 0 -8 -6 -7
    """
    max = 0
    print arr
    print "*" * 20
    for i in range(4):
        for j in range(4):
            sum = (arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
            if sum > max:
                max = sum
    return max

print hourglass.__doc__
arr = []
for a in xrange(6):
    print a
    arr.append(map(int, raw_input().rstrip().split()))

result = hourglass(arr)
print result
