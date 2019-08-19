
def triplet(arr):
	#import pdb; pdb.set_trace()
	tempArr = sorted(arr)
	n = len(tempArr)

	for last in range(n-1, 2, -1):
		#print last
		i = 0
		j = last-1
		while i < j:
			sumOfTwo = tempArr[i] + tempArr[j]
			if sumOfTwo < tempArr[last]:
				i += 1
			elif sumOfTwo > tempArr[last]:
				j -= 1
			else:
				return (tempArr[i], tempArr[j], tempArr[last])
	return "Triplet not found!"

if __name__ == '__main__':
	arr1 = [5, 32, 1, 7, 10, 50, 19, 21, 2]
	arr2 = [5, 32, 1, 7, 10, 50, 19, 21, 0]

	print triplet(arr1)
	print triplet(arr2)