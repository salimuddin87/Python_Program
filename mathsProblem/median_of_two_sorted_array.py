# Median to two sorted array

def medianoftwosortedArray(A, B):
	#import pdb; pdb.set_trace()
	nA = len(A)
	nB = len(B)

	tl = nA + nB
	medIndex = 0
	even = False

	if tl % 2 == 0:
		medIndex = int(tl/2 - 1)
		even = True
	else:
		medIndex = int((tl-1)/2)

	i = j = count = 0
	while i < nA and j < nB:
		if A[i] < B[j]:
			i += 1
			count += 1
		else:
			j += 1
			count += 1
		if count == medIndex:
			if even:
				return (A[i] + B[j])/2
			return min(A[i], B[j])
	while i < nA:
		i += 1
		count += 1
		if count == medIndex:
			if even:
				return (A[i] + A[i+1])/2
			return A[i]

	while j < nB:
		j += 1
		count += 1
		if count == medIndex:
			if even:
				return (B[j] + B[j+1])/2
			return B[j]

if __name__ == '__main__':
	B = [1,3]
	A = [2,4,5,6,7,8,9]
	print(medianoftwosortedArray(A, B))