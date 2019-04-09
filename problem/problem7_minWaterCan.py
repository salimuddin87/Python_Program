"""
Assume, there are 5 water can with capacity Total=[3,5,3,5,3]
and they contain Used=[3,2,1,3,1]. The first can is full but 2nd 
can have 3 unit of space and so on.

Return the min number of can required to carry "Used" water.
The min number of can needed is 2 (i.e. [0,5,0,5,0]) in this case.

"""
def minCanNeeded(T, U):
    minCan = 0
    T.sort()
    T = T[: : -1]
    U_total = sum(U)
    for i in range(0, len(T)):
        if U_total == 0:
            break
        if U_total < T[i]:
            minCan += 1
            break
        U_total -= T[i]
        minCan += 1
    return minCan


if __name__ == '__main__':
    T = [3,5,3,5,3]
    # U = [3,2,1,3,1]
    U = [3,2,1,3,3]

    res = minCanNeeded(T, U)
    print "Min can required : ", res
