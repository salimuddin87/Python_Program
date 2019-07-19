# Maximum sum of a subset of a given array

# Kadane's Algorithm
def maxSumSubset(arr):
	max_so_far = 0
	max_end_here = 0
	for i in range(len(arr)):
		max_end_here += arr[i]
		if max_end_here < 0:
			max_end_here = 0
		if max_so_far < max_end_here:
			max_so_far = max_end_here

	return max_so_far

if __name__ == '__main__':
	arr = [-2, 1, -3, 4, -1, 3, 2, -5, 4]
	print(maxSumSubset(arr))