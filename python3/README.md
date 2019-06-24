# Python 3 Tutorials

# Difference between Python2 and Python3
[https://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html]

1. Division operator

	print 7/5
	print -7/5

	Output in Python2 
	1
	-2

	Output in Python3
	1.4
	-1.4

2. Unicode:- In Python 2, implicit string type is ASCII. But in Python 3,
   implicit string type is Unicode.

	print type('default string type')
	print type(u'default string type')
	
	Output in Python2
	<type 'str'>
	<type 'unicode'>

	Output in Python3
	<type 'str'>
	<type 'str'>

3. xrange:- xrange() of python2 doesnot exist in python3. In Python3, the range
   function now does what xrange does in python2.

4. Error Handling:- In python3 "as" keyword is required.

	try:
	    trying to check error
	except NameError as err: 
	    print(err, 'Error caused')

5. __future__ module:- It will help in migration from python2 to python3.

	from __future__ import division
	print 7/5
	print -7/5

	Output :-
	1.4
	-1.4

	feature :- division, nested_scopes, generators, with_statement, 
		print_function

6. print function need parenthesis in python3.
