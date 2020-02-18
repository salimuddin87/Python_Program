def searchValueIndex(arr, start, num):

    for i in range(start, len(arr)):
        if arr[i] == num:
            return i
    return -1

def minSwapToSortArray(arr):
    minSwap = 0
    n = len(arr)
    index = [i for i in range(1, n+1)]

    for i in range(0, n):
        print(index)
        if index[i] != arr[i]:
            t = searchValueIndex(index, i, arr[i])
            if t != -1:
                index[i], index[t] = index[t], index[i]
                minSwap += 1
    return minSwap

if __name__ == '__main__':
    arr = [3,2,6,1,5,4]
    print(minSwapToSortArray(arr))