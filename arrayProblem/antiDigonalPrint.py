def printDiagonally(arr):
	n = len(arr)
	m = len(arr[0])-1
	res = []

	# for upper half of square matrix
	for i in range(n):
		res.append([])
		row = 0
		col = i
		while col >= 0:
			res[i].append(arr[row][col])
			row += 1
			col -= 1

	# for lower half of square matrix
	for i in range(1,n):
		res.append([])
		row = i
		col = m 
		while row < n:
			res[n+i-1].append(arr[row][col])
			row += 1
			col -= 1

	print res

if __name__ == "__main__":
	arr1 = [
	[1,2,3],
	[4,5,6],
	[7,8,9]]

	arr = [
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12]]

	printDiagonally(arr1)