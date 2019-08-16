
# Iterative method
def binarysearch(arr, start, end, num):
    #print(arr[start:end+1])
    if start > end:
        return -1
    mid = start + int((end - start)/2)
    if num == arr[mid]:
        return mid
    elif num < arr[mid]:
        return binarysearch(arr, start, mid-1, num)
    else:
        return binarysearch(arr, mid+1, end, num)