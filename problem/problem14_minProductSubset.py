import sys

def minProduct(arr):
    
    count_negative = 0
    count_zero = 0
    max_negative_num = -(sys.maxint - 1)
    min_positive_num = sys.maxint
    min_product = 1

    for i in range(0, len(arr)):

    	# Count number of zero
    	if arr[i] == 0:
    		count_zero += 1
    		continue

    	if arr[i] < 0:
    		count_negative += 1
    		max_negative_num = max(max_negative_num, arr[i])

    	if arr[i] > 0:
    		min_positive_num = min(min_positive_num, arr[i])

    	min_product *= arr[i]

    #Print all variables
    print "count_negative 	: ", count_negative
    print "count_zero 		: ", count_zero
    print "max_negative_num	: ", max_negative_num
    print "min_positive_num : ", min_positive_num
    print "min_product		: ", min_product
    
    # Either all item is zero or there is no negative num and atleast 1 zero.
    if (count_zero == len(arr)) or (count_negative == 0 and count_zero > 0):
    	return 0

    if count_negative == 0:
    	return min_positive_num

    # If there is even negative no
    #if count_negative % 2 == 0:
    if not (count_negative & 1) and count_negative != 0:
    	return (min_product/max_negative_num)
    else:
    	return min_product

if __name__ == '__main__':

	#arr = [-3,5,-6,1,-2,-4]
	#arr = [0,0,3,4,8,0]
	arr = [8,3,1,4,9,2]
	print arr
	print minProduct(arr)