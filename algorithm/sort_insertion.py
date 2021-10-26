"""
Insertion sort is a simple and efficient comparison sort. In this algorithm, each iteration removes an element
from the input data and inserts it into the correct position in the list being sorted.
"""


# O(n^2) in worst cases and O(n) in best case
def insertion_sort(num_list):
    print(num_list)
    for i in range(1, len(num_list)):
        key = num_list[i]
        j = i - 1
        print("i = {}, key = {} and j = {}".format(i, key, j))
        while j >= 0 and num_list[j] > key:
            num_list[j + 1] = num_list[j]
            j = j - 1
        num_list[j + 1] = key
        print(num_list)


if __name__ == '__main__':
    insertion_sort([5, 3, 8, 6, 7])
