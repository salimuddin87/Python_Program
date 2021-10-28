"""
Quick sort is in-place sorting and divide and conquer algorithm.
best case: O(nlogn)
worst case: O(n^2) if we pick greatest/smallest element as pivot
There are different way to pick quick sort pivot element:
    1. Pick first/last element as pivot
    2. Pick random element as pivot
    3. Pick median as pivot
"""

import math


def partition(num_list, first, last):
    pivot = math.floor((first + last) / 2)
    pivot_value = num_list[pivot]
    print("pivot item :", pivot_value)
    i = first
    j = last

    while i < j:
        if num_list[i] < pivot_value:
            i += 1
        if num_list[j] > pivot_value:
            j -= 1
        # swap i and j position item
        if i != pivot and j != pivot:
            num_list[i], num_list[j] = num_list[j], num_list[i]
            i += 1
            j -= 1
        if i == pivot:
            i += 1
        if j == pivot:
            j -= 1

    # i == j after coming out of loop, swap with pivot value
    num_list[i], num_list[pivot] = num_list[pivot], num_list[i]
    print("List after partition for pivot {} is : {}".format(num_list[j], num_list))
    return i


def quick_sort(num_list, first, last):
    if first < last:
        q = partition(num_list, first, last)
        quick_sort(num_list, first, q-1)
        quick_sort(num_list, q+1, last)
    return num_list


if __name__ == '__main__':
    print(quick_sort([4,9,2,1,6], 0, 4))
