"""
Bubble sort is the simplest sorting algorithm. It works by iterating
the input element from the first element to last.
"""


# Takes O(n^2) even in best case.
def bubble_sort(num_list):
    print(num_list)
    for i in range(len(num_list), 1, -1):
        print("i = ", i)
        for j in range(0, i - 1):
            print("j = ", j, end="; ")
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

        print("\n num_list = ", num_list)


# Takes O(n) in best case and O(n^2) in worst case
def bubble_sort_best(num_list):
    print(num_list)
    swapped = True
    for i in range(len(num_list), 1, -1):
        print("i = ", i)
        if swapped:
            swapped = False
            for j in range(0, i - 1):
                print("j = ", j, end="; ")
                if num_list[j] > num_list[j + 1]:
                    swapped = True
                    num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

        print("\n num_list = ", num_list)


if __name__ == '__main__':
    bubble_sort([4, 9, 2, 6, 1])
    print("*" * 30)
    bubble_sort_best([4, 9, 12, 16, 100])
