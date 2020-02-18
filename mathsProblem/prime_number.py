from math import sqrt

# Time complexity is O(sqrt(n))
def isPrime(num):
	if num <= 1:
		return False
	for i in range(2, int(sqrt(num)+1)):
		if num % i == 0:
			return False
	return True

if __name__ == '__main__':

	print(isPrime(10))
	print(isPrime(13))