# spiral traversal in a 2d matrix

arr = [
	[1,2,3,4,13],
	[5,6,7,8,14],
	[9,10,11,12,15],
	[16,17,18,19,20]
]

def spiralTraversal(arr):
	row = len(arr)
	col = len(arr[0])
	i = 0 
	while i < int(row/2):
		j = i 
		print("\nTraverse right")
		for k in range(j, col-i):
			print(arr[i][k], end=" ")

		print("\nTraverse down")
		j = col - i - 1
		for k in range(i+1, row-i):
			print(arr[k][j], end=" ")

		print("\nTraverse left")
		j -= 1
		for k in range(j, i-1, -1):
			print(arr[j][k], end=" ")

		print("\nTraverse up")
		j -= 1
		for k in range(j, i, -1):
			print(arr[k][i], end=" ")

		i += 1

if __name__ == '__main__':
	spiralTraversal(arr)			