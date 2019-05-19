
"""
Counting sort is a sorting technique based on keys between a specific range.
It works by counting the number of objects having distinct key values (kind
of hashing). Then doing some arithmetic to calculate the position of each 
object in the output sequence.
"""

def countingSort(arr):
    
    l = min(arr)
    r = max(arr)
    Index = []
    Count = []
    # create index and count list
    for i in range(l, r+1):
        Index.append(i)
        Count.append(arr.count(i))
    print "index : ", Index
    print "count : ", Count

    # find count sum
    for i in range(1, len(Count)):
        Count[i] += Count[i-1]
    print "count_sum : ", Count

    # sort the array based on index
    sorted_arr = [0] * len(arr)
    for item in arr:
        j = Index.index(item)
        item_index = Count[j] - 1
        sorted_arr[item_index] = item
        Count[j] -= 1

    print "Sorted_arr : ", sorted_arr


#arr = [11,8,5,4,6,8,9]
arr = [20,30,40]
print arr
countingSort(arr)
