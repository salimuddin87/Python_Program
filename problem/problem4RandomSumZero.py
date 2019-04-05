"""
Generate N random numbers in between 
-100 to 100, whose sum is zero

"""
import random

def generateNnumbers(N):
    list1 = []
    for i in range(0, N):
        item = random.randint(-999, 999)
        list1.append(item)
    return list1

def randomSumZero(N):
    # @ N : an integer
    # @ return a list whose sum is zero
    i = 0
    list2 = generateNnumbers(N)
    sumoflist = sum(list2)
    while sumoflist != 0: # and i != 1000:
        i = i + 1
        list2 = generateNnumbers(N)
        sumoflist = sum(list2)

    #if sumoflist == 0:
    #    print "i : {} and list : {}".format(i, list2)
    #else:
    #    print "Not found!"
    print "i : {} and list : {}".format(i, list2)

if __name__ == '__main__':
    n = int(raw_input("Enter an integer : "))
    randomSumZero(n)
