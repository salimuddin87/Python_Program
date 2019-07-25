
def zigzagconversion(s, k):
	n = len(s)
	col = int(n / (k-1)) + 1
	res = [[0 for x in range(col)] for y in range(k)]
	
	i = j = l = 0
	reverseFlag = False
	while l < n:
		if not reverseFlag:
			res[i][j] = s[l]
			l += 1
			i += 1
			if i == k:
				i -= 2
				j += 1
				reverseFlag = True
		else:
			res[i][j] = s[l]
			l += 1
			i -= 1
			if i == -1:
				i += 2
				j += 1
				reverseFlag = False

	for i in range(k):
		print(res[i])
	
	newStr = ""
	for i in range(k):
		for j in range(col):
			if res[i][j]:
				newStr += res[i][j]
	return newStr


if __name__ == '__main__':
	s1 = "PAYPALISHIRING"
	s2 = "PAYPALISHIRINGEXPERIENCE"
	print(zigzagconversion(s1, 4))
	print(zigzagconversion(s2, 4))