import sys


class MinimalABSdiffInArray():
    def __init__(self):
        self.n = int(raw_input("Enter the size of an array \n"))
        self.arr = map(int, raw_input("Enter array elements \n").rstrip().split())

    def findMinimal(self):
        n = self.n
        arr = self.arr
        arr.sort()
        minAbsdiff = sys.maxint
        for i in range(0,n-1):
            absdiff = abs(arr[i] - arr[i+1])
            if absdiff < minAbsdiff:
                    minAbsdiff = absdiff

        return minAbsdiff

if __name__ == '__main__':
    # n = int(raw_input("Enter the size of an array"))

    # arr = map(int, raw_input("Enter array elements").rstrip().split())

    obj1 = MinimalABSdiffInArray()

    result = obj1.findMinimal()

    print "Result is : %s" % result
