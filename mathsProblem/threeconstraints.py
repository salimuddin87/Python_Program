"""
Given:
	A = [0,1,2,5]
	B = 2 (length of digits)
	C = 21 (max value of a number)

Output:
	5 (10, 11, 12, 15, 20)
"""
def length(C):
	l = 0
	c = C
	while c != 0:
	    c = int(c / 10)
	    l += 1
	return l 

def solution(A, B, C):
	if B > length(C) or B < length(C):
		return 0
	if B == length(C):
		pass

if __name__ == '__main__':
	A = [0,1,2,5]
	B = 2
	C = 21
	print(solution(A, B, C))

"""
Find solution of each cases seperately.

Case 1 : When B is greater than length of C
Case 2: When B is smaller than length of C
Case 3: When B is equal to length of C.

For Case 3

Let First(i) denote number formed by taking first i digits of C
Then try to find a relation between solution of (A, i, first(i)) 
and (A, i - 1, first(i - 1)) for i = 1 to i <= B

"""