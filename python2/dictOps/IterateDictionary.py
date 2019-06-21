# Program to iterate dictionary

class IterateDictionary():

    def __init__(self):
        self.initDict = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e'}

    def defaultMethod(self):
        print "By default dict iterate only keys"
        for key in self.initDict:
            print "%d -> %s" % (key, self.initDict[key])
        return True
    
    def iterateValues(self):
        print "Print Only Values of Dictionary"
        for value in self.initDict.values():
            print value
        return True

    def iterateKeysValues(self):
        print "Iterate key, value"
        for key,value in self.initDict.iteritems():
            print key, value
        return True

    def iterateBySet(self):
        print "Iterate by set"
        for item in self.initDict.items():
            print item
        return True


if __name__ == '__main__':
    obj1 = IterateDictionary()
    obj1.defaultMethod()
    obj1.iterateValues()
    obj1.iterateKeysValues()
    obj1.iterateBySet()
