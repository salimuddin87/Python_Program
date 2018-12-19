def rotLeft(a, d):
    b = [0] * len(a)
    for i in range(0, len(a)):
        nl = i - d
        print i,nl
        b[nl] = a[i]
        print "a = {}".format(a)
        print "b = {}".format(b)
    return b

a = [1,2,3,4,5]
d = 4
rotLeft(a, d)
