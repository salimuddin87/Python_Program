import sys

def maxProduct(arr):

	count_zero = 0
	count_negative = 0
	max_negative_num = -(sys.maxint -1)
	max_product = 1

	for i in range(0, len(arr)):

		if not arr[i]:
			count_zero += 1
			continue

		if arr[i] < 0:
			count_negative += 1
			max_negative_num = max(max_negative_num, arr[i])

		max_product *= arr[i]

	print "count_zero 		: ", count_zero
	print "count_negative	: ", count_negative
	print "max_negative_num : ", max_negative_num
	print "max_product 		: ", max_product

	# All item is zero
	if count_zero == len(arr):
		return 0

	# count negative is odd
	if count_negative & 1:
		# if there is one negative number and others are 0
		if (count_negative == 1) and (count_negative + count_zero == len(arr)):
			return 0
		
		return max_product / max_negative_num
	
	return max_product

if __name__ == '__main__':

	#arr = [3,4,1,7,2]
	#arr = [0,0,-2,0,0]
	arr = [-2,5,1,-4,-3]
	print arr
	print maxProduct(arr)