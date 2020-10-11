# convert a list of list to a single list
def return_list(arr):
    result = []
    for item in arr:
        if type(item) is list:
            result.extend(item)
        else:
            result.append(item)
    return result


def return_single_list(arr):
    result = []
    for item in arr:
        if type(item) is list:
            result.extend(return_single_list(item))
        else:
            result.append(item)
    return result


if __name__ == '__main__':
    list1 = [1, 2, 3, ['a', 6], [[4, 5]]]
    print("Return list: ", return_list(list1))
    print("Return single list: ", return_single_list(list1))
