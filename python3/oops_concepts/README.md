# Base Overloading methods

* __init__ ( self [,args...] )
  Constructor (with any optional arguments)
  Sample Call : obj = className(args)

* __del__( self )
  Destructor, deletes an object
  Sample Call : del obj

* __repr__( self )
  Evaluable string representation
  Sample Call : repr(obj)

* __str__( self )
  Printable string representation
  Sample Call : str(obj)

* __cmp__ ( self, x )
  Object comparison
  Sample Call : cmp(obj, x)

Note:- A namespace is a mapping from names to objects.
