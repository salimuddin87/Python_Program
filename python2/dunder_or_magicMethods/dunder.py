"""
Dunder or magic methods in Python are the methods having two prefix and suffix
underscores in the method name. Dunder here means “Double Under (Underscores)”. 
These are commonly used for operator overloading.

"""
class string:
	"""docstring for string"""
	def __init__(self, str1): # Magic method
		self.str1 = str1

	def __str__(self):
		return ("Object String is : {}".format(self.str1))


if __name__ == '__main__':
	s = string("Hello")
	print(s)

"""
Output without __str__

	<__main__.string object at 0x7f4ed4ed3cc0>	

Output after defining __str__ (Magic method)
"""

"""
Binary Operator	Method
---------------------------------------
+	object.__add__(self, other)
-	object.__sub__(self, other)
*	object.__mul__(self, other)
//	object.__floordiv__(self, other)
/	object.__truediv__(self, other)
%	object.__mod__(self, other)
**	object.__pow__(self, other[, modulo])
<<	object.__lshift__(self, other)
>>	object.__rshift__(self, other)
&	object.__and__(self, other)
^	object.__xor__(self, other)
|	object.__or__(self, other)
---------------------------------------


Extended Operator	Method
---------------------------------------
+=	object.__iadd__(self, other)
-=	object.__isub__(self, other)
*=	object.__imul__(self, other)
/=	object.__idiv__(self, other)
//=	object.__ifloordiv__(self, other)
%=	object.__imod__(self, other)
**=	object.__ipow__(self, other[, modulo])
<<=	object.__ilshift__(self, other)
>>=	object.__irshift__(self, other)
&=	object.__iand__(self, other)
^=	object.__ixor__(self, other)
|=	object.__ior__(self, other)
---------------------------------------


Unary Operator	Method
---------------------------------------
-			object.__neg__(self)
+			object.__pos__(self)
abs()		object.__abs__(self)
~			object.__invert__(self)
complex()	object.__complex__(self)
int()		object.__int__(self)
long()		object.__long__(self)
float()		object.__float__(self)
oct()		object.__oct__(self)
hex()		object.__hex__(self
---------------------------------------


Comparison Operator	 Method
---------------------------------------
<	object.__lt__(self, other)
<=	object.__le__(self, other)
==	object.__eq__(self, other)
!=	object.__ne__(self, other)
>=	object.__ge__(self, other)
>	object.__gt__(self, other)
---------------------------------------
"""