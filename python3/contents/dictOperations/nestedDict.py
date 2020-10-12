browserDict = {"GC": {"connected": 2, "Error5": 0, "Error8": 1},
               "MF": {"connected": 3, "Error5": 1, "Error8": 1},
               "IE": {"connected": 0, "Error5": 2, "Error8": 2},
               "DDG": {"connected": 1, "Error5": 3, "Error8": 3}
              }

def addItem(browser, c=0, e5=0, e8=0):
    browserDict[browser] = {"connected": c, "Error5": e5, "Error8": e8}

def delItem(browser):
    # To delete nested dict
    del browserDict[browser]

    # To delete an item of nested dict
    #del browserDict[browser]["connected"]
    #del browserDict[browser]["Error5"]
    #del browserDict[browser]["Error8"]

def displayOldWays():

    print("\n%8s | %12s %12s %12s" % ('Browser', 'Connected', 'Error5', 'Error8'))
    print("-" * 60)
    for dictOne in browserDict.keys():
        print("%8s | " % dictOne, end=" ")
        for item in browserDict[dictOne].keys():
            print("%12s" % browserDict[dictOne][item], end=" ")
        print("\n")

def displayNewWays():

    print("\n{:8} | {:>12} {:>12} {:>12}".format('Browser', 'Connected', 'Error5', 'Error8'))

    print("-" * 60)
    for dict1 in browserDict.keys():
        print("{:8} | ".format(dict1), end=" ")
        for item in browserDict[dict1].keys():
            print("{:>12}".format(browserDict[dict1][item]), end=" ")
        print("\n")

if __name__ == '__main__':

    displayOldWays()

    print("\nAdd Opera browser details from log")
    addItem('Opera', 0, 3, 2)
    print("\nAdd safari browser details from log")
    addItem('safari', 1, 2, 3)

    displayNewWays()

    print("\n Delete IE browser data")
    delItem('IE')

    displayNewWays()
