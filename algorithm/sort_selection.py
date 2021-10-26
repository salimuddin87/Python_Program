"""
Selection sort is an in-place sorting algorithm. Selection sort works well for small files.
"""


# O(n^2) in worst case and O(n^2) in best case
def selection_sort(num_list):
    print(num_list)
    # Find the minimum value and swap it with the current position.
    for i in range(0, len(num_list)):
        print("i = ", i)
        min_index = i
        for j in range(i+1, len(num_list)):
            if num_list[min_index] > num_list[j]:
                min_index = j
        # Swap the elements
        print("min_index = ", min_index)
        if min_index != i:
            num_list[min_index], num_list[i] = num_list[i], num_list[min_index]
        print(num_list)


if __name__ == '__main__':
    # selection_sort([4, 9, 2, 1, 6])
    selection_sort([1, 2, 4, 6, 9])
