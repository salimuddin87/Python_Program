import fibo

x = fibo.fib(1000)
print x
print type(x)

y = fibo.fib2(1000)
print y
print type(y)

print fibo.__name__

# Using a function often, assign it a local name
fib = fibo.fib
print fib(500)
