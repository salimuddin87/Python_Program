class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        if A[0] == 0 and len(A) == 1:
            A[0] = 1
            return A

        # Remove front zero from the list
        for item in A:
            if item == 0:
                A = A[1:]
            else:
                break

        # Increment the array by one
        i = len(A) - 1
        A[i] = A[i] + 1
        while A[i] == 10:
            if i == 0:
                A[i] = 0
                A = [1] + A
                return A
            A[i] = 0
            i = i - 1
            A[i] = A[i] + 1
        return A

if __name__ == '__main__':
    obj = Solution()
    test1 = [1,2,3,4,5]
    test2 = [9,9,9,9,9]
    test3 = [4,5,3,9,1,3]
    test4 = [3,4,1,2,9,9,9]

    print "[0] plus one is : ", obj.plusOne([0])

    print "{} plus one is : ".format(test1),
    print obj.plusOne(test1)

    print "{} plus one is : ".format(test2),
    print obj.plusOne(test2)

    print "{} plus one is : ".format(test3),
    print obj.plusOne(test3)

    print "{} plus one is : ".format(test4),
    print obj.plusOne(test4)
