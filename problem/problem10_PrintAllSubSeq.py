arr = [10,1,6,34,2,5,78,8,3,99,9]

def findList(arr, item):
    res = []
    prevItem = item - 1
    nextItem = item + 1
    while prevItem in arr and prevItem not in res:
        res.append(prevItem)
        prevItem -= 1
    while nextItem in arr and nextItem not in res:
        res.append(nextItem)
        nextItem += 1
    return res

def printAllSubseq(arr):
    resDict = {}
    key = 0
    for item in arr:
        key += 1
        resDict[key] = [item]
        arr.remove(item)
        list1 = findList(arr, item)
        resDict[key].extend(list1)
        for item in list1:
            arr.remove(item)
    return resDict

def printLargeSub(arr):
    arr.sort()
    for i in range(0, len(arr)):
        if i == 0:
            print arr[i],
            continue
        nextItem = arr[i-1] + 1
        if nextItem == arr[i]:
            print arr[i],
        else:
            print "\n", arr[i],

if __name__ == '__main__':
    
    outDict = printAllSubseq(arr)
    for key in outDict.keys():
        print outDict[key]
