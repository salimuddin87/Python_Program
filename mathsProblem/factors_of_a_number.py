from math import sqrt

# Time complexity is O(n)
def factorsmethod1(num):
	factors = []
	for i in range(1, num+1):
		if num % i == 0:
			factors.append(i)
	return factors

# Time complexity is O(sqrt(n))
def factorsmethod2(num):
    factors = []
    for i in range(1, int(sqrt(num)+1)):
        if num % i == 0:
            factors.append(i)
            if int(num/i) != int(sqrt(num)):
            	factors.append(int(num/i))
    factors.sort()
    return factors


if __name__ == '__main__':
    
    print(factorsmethod1(36))
    print(factorsmethod2(36))
