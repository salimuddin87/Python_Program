"""
class SubClassName (ParentClass1[, ParentClass2, ...]):
   'Optional class documentation string'
   class_suite

You can use issubclass() or isinstance() functions to check a relationships of two classes and instances.
   - The issubclass(sub, sup) boolean function returns true if the given subclass sub is indeed a 
      subclass of the superclass sup.
   - The isinstance(obj, Class) boolean function returns true if obj is an instance of class Class
      or is an instance of a subclass of Class

"""

#!/usr/bin/python

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print "Calling parent constructor"

   def parentMethod(self):
      print 'Calling parent method'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "Parent attribute :", Parent.parentAttr

class Child(Parent): # define child class
   def __init__(self):
      print "Calling child constructor"

   def childMethod(self):
      print 'Calling child method'

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method
