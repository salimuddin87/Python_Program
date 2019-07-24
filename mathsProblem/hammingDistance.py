"""
Let f(x, y) be the hamming distance defined above.

A=[2, 4, 6]

We return,
f(2, 2) + f(2, 4) + f(2, 6) + 
f(4, 2) + f(4, 4) + f(4, 6) +
f(6, 2) + f(6, 4) + f(6, 6) = 

0 + 2 + 1
2 + 0 + 1
1 + 1 + 0 = 8
"""


def twoNumHamDistance(x, y):
	print("using bin")
	#res = list(bin(x^y))
	#return res.count('1')
	return bin(x^y).count('1')

def hammingDistance(A):
	n = len(A)
	if not n:
		return 0
	res = 0
	for i in range(0, n):
		for j in range(i+1, n):
			if A[i] != A[j]:
				res += 2 * twoNumHamDistance(A[i], A[j])
	return res

if __name__ == '__main__':
    
    print(hammingDistance([2, 4, 6]))	

"""
int hammingDistance(const int* A, int n1) {
    int i,j;
    long long sum=0;
    for(i=0;i<32;i++)
    {
        int count=0;
        for(j=0;j<n1;j++)
        {
            if((A[j] & (1<<i)))
                count++;
        }
        sum = sum + (long long)2*count*(n1-count);
    }
    sum = sum%1000000007;
    return sum;
}
"""