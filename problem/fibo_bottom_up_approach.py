#fibNum = []
def fibo(n):
    fibNum = []
    if n == 0 or n == 1:
        return n
    fibNum.append(0)
    fibNum.append(1)
    for i in range(2, n):
        fibNum.append(fibNum[i-1] + fibNum[i-2])
    return fibNum

print fibo(5)
