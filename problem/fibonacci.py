
def fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return (fibo(n-1) + fibo(n-2))

if __name__ == '__main__':
    n = int(raw_input("Enter a number : "))
    for i in range(0, n):
        print fibo(i),
