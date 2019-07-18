"""
Given a binary matrix of 0,1.
	If a zero is found, mark that row and column with zero.
condition:
	1. you can not use if-else stmt
	2. you can not use turnary operator
	3. you can not use dictionary
"""
arr = [
	[1,1,1,1],
	[1,0,1,1],
	[1,1,0,1]
]

def specialSparseMatrix(arr):
	row = len(arr)
	col = len(arr[0])
	rowMatrix = []
	colMatrix = []
	for k in range(0, row):
		rowMatrix.append([])
		colMatrix.append([])

	print("\nPerform logical-and operation on rows")
	for i in range(0, row):
		status = 1
		for j in range(0, col):
			status &= arr[i][j]

		# Fill rows matrix with status
		for j in range(0, col):
			rowMatrix[i].append(status)

	print(rowMatrix)
	
	print("\nPerform logical-and operation on columns")
	for j in range(col):
		status = 1
		for i in range(row):
			status &= arr[i][j]
		# Fill columns with status
		for i in range(row):
			colMatrix[i].append(status)

	print(colMatrix)

	print("\nPerform logical-and between rowMatrix and colMatrix")
	for i in range(row):
		for j in range(col):
			arr[i][j] = rowMatrix[i][j] & colMatrix[i][j]

	print(arr)

if __name__ == '__main__':
	specialSparseMatrix(arr)
