# Given an positive integer number N
# Find two prime number whose sum is N

from math import sqrt

class Solution:
    # @param A : integer
    # @return a list of integers
    def isPrime(self, num):
        if num <= 1:
            return False
        for i in range(2, int(sqrt(num)+1)):
            if num % i == 0:
                return False
        return True
        
    def primesum(self, A):
        res = []
        for i in range(2, int(A/2)):
            if self.isPrime(i):
                if self.isPrime(A-i):
                    res.append(i)
                    res.append(A-i)
                    return res
        return res

if __name__ == '__main__':
    A = Solution()
    print(A.primesum(12))