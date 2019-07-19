# Maximum sum of a subset of a given array
from sys import maxsize

# Kadane's Algorithm
def maxSumSubset(arr):
	max_so_far = -maxsize - 1
	max_end_here = 0
	for i in range(len(arr)):
		max_end_here += arr[i]
		if max_end_here < 0:
			max_end_here = 0
		elif max_so_far < max_end_here:
			max_so_far = max_end_here

	return max_so_far

# Print the max sub-array in a given array
def printMaxSumSubset(arr):
	max_so_far = -maxsize - 1
	max_end_here = 0
	start = end = curr = 0
	for i in range(len(arr)):
		max_end_here += arr[i]
		
		if max_so_far < max_end_here:
			max_so_far = max_end_here
			start = curr
			end = i

		if max_end_here < 0:
			curr = i + 1
			max_end_here = 0
			
	return max_so_far, start, end

if __name__ == '__main__':
	#arr = [-2, 1, -3, 4, -1, 3, 2, -5, 4]
	#arr = [-3,-5,-1,-9,-3,-2,-4]
	arr = [-3,-5,-1,-9,-3,2,-4]
	print(maxSumSubset(arr))
	print(printMaxSumSubset(arr))