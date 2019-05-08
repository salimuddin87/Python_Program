arr = [10,1,6,34,2,5,78,8,3,99,9]

def printLargeSub(arr):
    arr.sort()
    for i in range(0, len(arr)):
        if i == 0:
            print arr[i],
            continue
        nextItem = arr[i-1] + 1
        if nextItem == arr[i]:
            print arr[i],
        else:
            print "\n", arr[i],

if __name__ == '__main__':
    
    printLargeSub(arr)
