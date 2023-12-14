# Program to iterate dictionary
class IterateDictionary:

    def __init__(self):
        self.initDict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

    def default_method(self):
        print("By default dict iterate only keys")
        for key in self.initDict.keys():
            print("%d -> %s" % (key, self.initDict[key]))
        return True
    
    def iterate_values(self):
        print("Print Only Values of Dictionary")
        for value in self.initDict.values():
            print(value)
        return True

    def iterate_keys_values(self):
        print("Iterate key, value")
        for key, value in self.initDict.items():
            print(key, value)
        return True

    def iterate_by_set(self):
        print("Iterate by set")
        for item in self.initDict.items():
            print(item)
        return True


if __name__ == '__main__':
    obj1 = IterateDictionary()
    obj1.default_method()
    obj1.iterate_values()
    obj1.iterate_keys_values()
    obj1.iterate_by_set()
