class NestedDict:

    def __init__(self, browser, **kwargs):

        self.browserDict = dict()
        self.browserDict[browser] = kwargs
        
    def displayDict(self):

        print("{:12} | {:>12} {:>12} {:>12}".format('Browser', 'Connected', 'Error5', 'Error8'))
        for key in self.browserDict.keys():
            print("\n{:12} | ".format(key), end=" ")
            for key2 in self.browserDict[key].keys():
                print("{:>12}".format(self.browserDict[key][key2]), end=" ")

    def addItem(self, browser, **kwargs):
        self.browserDict[browser] = kwargs

    def delItem(self, browser):
        del self.browserDict[browser]


if __name__ == '__main__':
    obj = NestedDict("Chrome", connected=2, Error5=0, Error8=1)

    obj.displayDict()

    print("\nAdd Firefox in the current object!")
    obj.addItem("Firefox", connected=5, Error5=2, Error8=3)
    
    print("\nAdd Explorer in the current object!")
    obj.addItem("Explorer", connected=5, Error5=2, Error8=3)
    
    print("\nAdd DDGo in the current object!")
    obj.addItem("DDGo", connected=5, Error5=2, Error8=3)
    
    print("\nAdd Opera in the current object!")
    obj.addItem("Opera", connected=5, Error5=2, Error8=3)

    print("\nAdd Safari in the current object!")
    obj.addItem("Safari", connected=5, Error5=2, Error8=3)

    obj.displayDict()

    print("\nDelete Opera from the current object!")
    obj.delItem('Opera')

    obj.displayDict()
