"""
Input:
    N = 5, D = [[1,2,10], [2,3,20], [2,5,25]]

Return: [10, 55, 45, 25, 25]

First devotee donated :      [10, 10, 0, 0, 0]
Second devotee donated :     [0, 20, 20, 0, 0]
Third devotee donated :      [0, 25, 25, 25, 25]

Total earn by beggars :      [10, 55, 45, 25, 25]

"""

def beggarsEarning(N, D):

    resList = [0] * N
    for itemList in D:
        first = itemList[0] - 1
        last = itemList[1]
        for i in range(first, last):
            resList[i] = resList[i] + itemList[2]

    return resList

if __name__ == '__main__':
    N = int(raw_input("Enter number of beggars : "))
    DN = int(raw_input("Enter number of devotees : "))
    #D = [[1,2,10], [2,3,20], [2,5,25]]
    D = []
    for i in range(0, DN):
        D.append([])
        first = int(raw_input("Enter first index value : "))
        D[i].append(first)
        last = int(raw_input("Enter last index value : "))
        D[i].append(last)
        money = int(raw_input("Enter the amount given : "))
        D[i].append(money)

    resList = beggarsEarning(N, D)
    print resList
