"""
A=[1, 3, -1]

f(1, 1) = f(2, 2) = f(3, 3) = 0
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

So, we return 5.
"""
# @param A : list of integers
# @return an integer
def maxArr(self, A):
    max1 = -sys.maxsize-1
    max2 = -sys.maxsize-1
    min1 = sys.maxsize
    min2 = sys.maxsize
    for i in range(len(A)):
        max1 = max(max1, A[i]+i)
        min1 = min(min1, A[i]+i)
        max2 = max(max2, A[i]-i)
        min2 = min(min2, A[i]-i)
        
    return max(max1-min1, max2-min2)