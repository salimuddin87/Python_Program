>>> stdout = "salim \n kabeer \n ansari \n year \n typeerror"
>>> print stdout
salim 
 kabeer 
 ansari 
 year 
 typeerror
>>> x = stdout.split('\n')
>>> print x
['salim ', ' kabeer ', ' ansari ', ' year ', ' typeerror']
>>> y = stdout.split('\n')[1:][:-1]
>>> print y
[' kabeer ', ' ansari ', ' year ']
