"""
Given a positive integer which fits in a 32 bit signed integer, 
find if it can be expressed as A^P where P > 1 and A > 0. A and 
P both should be integers.
"""

import math
class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        root = math.sqrt(A)
        if A==1:
            return 1
        if root == int(root) and root>1:
            return 1
        else:
            limit = math.floor(root)+1
            j = 2
            while(j<limit):
                for i in range(1,limit):
                    sm = j**i
                    if sm==A:
                        return 1
                j+=1
            
        return 0