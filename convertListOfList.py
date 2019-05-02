list1 = [1,2,3,['a',6], [[4,5]]]

def returnList(list1):
    result = []
    for item in list1:
        if type(item) is list:
            result.extend(item)
        else:
            result.append(item)
    return result

def returnSingleList(list1):
    result = []
    for item in list1:
        if type(item) is list:
            result.extend(returnSingleList(item))
        else:
            result.append(item)
    return result

if __name__ == '__main__':

    print returnList(list1)
    print returnSingleList(list1)
