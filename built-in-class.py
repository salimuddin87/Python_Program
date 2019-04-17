# Inherit object as a base class

class ABC(object):
    """
    Class for testing purposes
    """

    def __init__(self, arg1, arg2):
        """
        Inside init of ABC
        """
        self.arg1 = arg1
        self.arg2 = arg2

    @classmethod
    def method1(self):
        """
        Inside method1 
        """
        print "self.arg1: ", self.arg1
        print "self.arg2: ", self.arg2

class XYZ(ABC):
    """
    Inside XYZ class
    """
    def __init__(self, x, y, z):
        """
        Inside init of XYZ
        """
        super(XYZ, self).__init__(x, y)
        self.z = z

    def method2(self):
        """
        Inside method 2
        """
        print "self.z : ", self.z


#obj = ABC(4, 5)
obj = XYZ(2, 3, 4)

print "obj.__doc__ : ", obj.__doc__
#print "obj.__name__ : ", obj.__name__
#print "obj.__bases__ : ", obj.__bases__
print "obj.__module__ : ", obj.__module__
print "obj.__dict__ : ", obj.__dict__
