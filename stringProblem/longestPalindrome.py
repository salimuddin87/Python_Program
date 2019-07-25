# Find first longest palindrom in a given string.


def checkPalindrome(string):
	return string == string[::-1]
	
# By brute-force method
def findLargestPalindrome(givenStr):
	palinString = ""
	palinLength = 0
	staticCount = 0

	for i in range(0, len(givenStr)):
		for j in range(1, len(givenStr)):
			staticCount += 1			# For time complexity
			tempStr = givenStr[i:j+1]
			staticCount += len(tempStr) # For time complexity
			status = checkPalindrome(tempStr)
			if status is True and palinLength < len(tempStr):
				palinString = tempStr
				palinLength = len(tempStr)
	print("staticCount: {}".format(staticCount))
	return palinLength, palinString

# Dynamic programming
def findLargestPalindromeDynamic(givenStr):
	if not len(givenStr):
		return ""
	if len(givenStr) == 1:
		return givenStr

	startIndex = 0
	palinLength = 1
	sparseMatrix = [
		[0 for x in range(len(givenStr))]
		for y in range(len(givenStr))
	]

	# Each character is palindrome
	for i in range(len(givenStr)):
		sparseMatrix[i][i] = 1

	# Fill for palindrome of length 2
	i = 0
	while i < (len(givenStr)-1):
		if givenStr[i] == givenStr[i+1]:
			sparseMatrix[i][i+1] = 1
			startIndex = i
			palinLength = 2
		i += 1

	# Fill for palindrome of length > 2
	k = 3 # length of palindrome sub-string
	while k <= len(givenStr):
		i = 0
		while i < (len(givenStr) - k + 1):
			j = i + k - 1
			if sparseMatrix[i + 1][j - 1] and givenStr[i] == givenStr[j]:
				sparseMatrix[i][j] = 1
				if k > palinLength:
					startIndex = i
					palinLength = k
			i += 1
		k += 1

	for i in range(len(sparseMatrix)):
		print(sparseMatrix[i])
	print("\n")

	return (palinLength, givenStr[startIndex: startIndex + palinLength])

if __name__ == '__main__':
	#import pdb; pdb.set_trace()

	givenStr = "saaxyzyxsrtptrs"
	string = "ha"
	print(findLargestPalindrome(string))
	print(findLargestPalindromeDynamic(givenStr))
	print(findLargestPalindromeDynamic("b"))
	print(findLargestPalindromeDynamic("ab"))