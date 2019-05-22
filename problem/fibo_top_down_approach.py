fibNum = []
def fibo(n):
    if n == 0 or n == 1:
        return n
    if n != 0:
        value = fibo(n-1) + fibo(n-2)
        fibNum.insert(n, value)
    return fibNum

print fibo(5)
