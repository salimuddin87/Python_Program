def findMedian(sortedList):
    length = len(sortedList)
    if length / 2 == 0:
        mid = (sortedList[(length-1)/2] + sortedList[length/2]) / 2
    else:
        mid = sortedList[length/2]
    return mid

def notifications(expenditure, d):
    notifyCount = 0
    i = 0
    while (i+d) < len(expenditure):
        tempList = expenditure[i:i+d]
        tempList.sort()

        median = findMedian(tempList)

        if expenditure[i+d] >= (2 * median):
            notifyCount += 1
        i += 1
    return notifyCount


if __name__ == '__main__':

    d = 5
    expenditure = [2,3,4,2,3,6,8,4,5]
    print notifications(expenditure, d)
