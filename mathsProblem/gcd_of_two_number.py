

# Time complexity is O(log(n))
def gcd(n, m):
	if n < m:
		n, m = m, n # swap n and m
	if m == 0:
		return n
	while m > 0:
		n = n % m
		n, m = m, n # swap n and m

	return n


if __name__ == '__main__':

	print(gcd(6, 9))
	print(gcd(9, 6))