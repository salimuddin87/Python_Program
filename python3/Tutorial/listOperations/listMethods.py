

if __name__ == '__main__':
    a = [0, 1, 2, 3]
    a.append(4)  # a = [0, 1, 2, 3, 4]

    b = [5, 6]
    a.extend(b)  # a = [0, 1, 2, 3, 4, 5, 6]

    a.insert(3, 10)  # a = [0, 1, 2, 10, 3, 4, 5, 6]

    a.append(10)  # a = [0, 1, 2, 10, 3, 4, 5, 6, 10]

    a.remove(10)  # Removes first item which is 10. That's why a = [0, 1, 2, 3, 4, 5, 6, 10]

    item = a.pop()  # item = 10 and a = [0, 1, 2, 3, 4, 5, 6]

    item1 = a.pop(4)  # item1 = 4 and 4 is not in list, check with a.index(4)

    item2 = a.index(3)  # item2 = 3 i.e. third item from list

    a.extend([1, 4, 2, 5, 1, 1])  # a = [0, 1, 2, 3, 5, 6, 1, 4, 2, 5, 1, 1]

    item3 = a.count(1)  # item3 = 4

    a.sort()  # a = [0, 1, 1, 1, 1, 2, 2, 3, 4, 5, 5, 6]

    a.reverse()  # a = [6, 5, 5, 4, 3, 2, 2, 1, 1, 1, 1, 0]
