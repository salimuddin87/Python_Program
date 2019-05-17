def merge(arr, l, m, r):
    count = 0
    n1 = m - l # size of left array [l to m-1]
    n2 = r - m + 1 # size of right array [m to r]

    # Create two temporary array
    L = [0] * n1
    R = [0] * n2

    # fill the array elements on temp array
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + j]

    i = 0 # initial left array index
    j = 0 # initial right array index
    k = l # start of the sub-array index

    # start merging of left and right array to arr
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            count += (len(L) - i)
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    return count

# Complete the countInversions function below.
def enhancedMergeSort(arr, l, r):
    inv_count = 0
    if l < r:
        m = (l + r + 1)/2

        inv_count += enhancedMergeSort(arr, l, m-1)
        inv_count += enhancedMergeSort(arr, m, r)

        inv_count += merge(arr, l, m, r)
    return inv_count

if __name__ == '__main__':
    import pdb
    #pdb.set_trace()
    arr = [2,1,3,1,2]
    print enhancedMergeSort(arr, 0, 4)
    print arr
